from __future__ import annotations

import argparse
import hashlib
import mimetypes
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlparse

THEME_FALLBACKS = {
    "cyan": "blue",
}

DEFAULT_TEAM_AVATAR = "/assets/images/team/default-avatar.svg"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="将仓库中的独立 mock 数据写入飞书多维表。",
    )
    parser.add_argument(
        "--config-file",
        default="feishu_config.yml",
        help="飞书同步配置文件路径，默认 feishu_config.yml",
    )
    parser.add_argument(
        "--data-file",
        default="mock_data/feishu_seed.yml",
        help="独立 mock 数据文件路径，默认 mock_data/feishu_seed.yml",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="确认清空当前受管数据表中的所有记录，并改写为 mock 数据。",
    )
    return parser.parse_args()


class MockFeishuSeeder:
    def __init__(self, config_file: str, data_file: str) -> None:
        from feishu_sync.config import load_settings
        from feishu_sync.utils import require_env

        self.repo_root = Path(__file__).resolve().parent.parent
        self.settings = load_settings(config_file)
        self.data_file = self.resolve_repo_path(data_file)
        self.app_id = require_env("FEISHU_APP_ID")
        self.app_secret = require_env("FEISHU_APP_SECRET")
        self.base_url = "https://open.feishu.cn/open-apis"
        self.tenant_access_token: str | None = None
        self.table_map: dict[str, str] = {}
        self.proxies = {"http": None, "https": None}
        self.schema_registry = self.build_schema_registry()
        self.mock_data = self._load_mock_data()

    @staticmethod
    def build_schema_registry() -> dict:
        from init_feishu_table import (
            NewsTableSchema,
            PeopleTableSchema,
            PositionsTableSchema,
            PublicationsTableSchema,
            ResearchTableSchema,
        )

        return {
            "team": PeopleTableSchema(),
            "news": NewsTableSchema(),
            "publications": PublicationsTableSchema(),
            "research": ResearchTableSchema(),
            "positions": PositionsTableSchema(),
        }

    def seed(self) -> None:
        self.authenticate()
        self.load_table_map()

        print("=" * 60)
        print("🧪 LV Group - Mock 数据写入飞书")
        print("=" * 60)
        print("ℹ️ 当前脚本会保留示例行，并用 mock 数据覆盖各表原有记录。")
        print("ℹ️ 当前脚本会同步文本内容，并尽量上传 Avatar / Image 附件。")

        for task in self.settings.tasks:
            schema = self.schema_registry.get(task.name)
            if not schema:
                print(f"⏭️ 跳过未注册 schema 的任务: {task.name}")
                continue

            table_id = self.table_map.get(task.table_name)
            if not table_id:
                raise RuntimeError(
                    f"未找到飞书数据表 [{task.table_name}]。请先运行 python scripts/init_feishu_table.py"
                )

            records = self.mock_data.get(task.name)
            if not isinstance(records, list):
                raise RuntimeError(
                    f"mock 数据文件缺少 {task.name} 数组: {self.data_file}"
                )

            print(f"\n📋 正在改写数据表: {task.table_name}")
            existing_ids = self.list_record_ids(table_id)
            if existing_ids:
                print(f"   🗑️ 清空现有记录 {len(existing_ids)} 条...")
                self.delete_records(table_id, existing_ids)

            print("   🌱 写入示例行...")
            self.create_record(table_id, schema, schema.sample_record)

            created_count = 0
            for source_record in records:
                converted_record = self.convert_record(task.name, source_record)
                final_fields = self.attach_media_fields(
                    task_name=task.name,
                    task=task,
                    source_record=source_record,
                    fields=converted_record,
                )
                self.create_record(table_id, schema, final_fields)
                created_count += 1

            print(f"   ✅ 已写入 {created_count} 条 mock 记录 + 1 条示例行")

        print("\n" + "=" * 60)
        print("🎉 Mock 数据已写入飞书多维表。")
        print("=" * 60)

    def resolve_repo_path(self, path_like: str | Path) -> Path:
        path = Path(path_like)
        if path.is_absolute():
            return path
        return self.repo_root / path

    def _load_mock_data(self) -> dict:
        import yaml

        if not self.data_file.exists():
            raise FileNotFoundError(f"找不到 mock 数据文件: {self.data_file}")

        with self.data_file.open("r", encoding="utf-8") as handle:
            payload = yaml.safe_load(handle) or {}

        if not isinstance(payload, dict):
            raise ValueError("mock 数据文件必须是一个顶层字典。")

        return payload

    def authenticate(self) -> None:
        print("⏳ 正在请求飞书授权...")
        payload = self.request(
            "POST",
            f"{self.base_url}/auth/v3/tenant_access_token/internal",
            json={"app_id": self.app_id, "app_secret": self.app_secret},
            use_auth=False,
        )
        self.tenant_access_token = payload["tenant_access_token"]
        print("✅ 授权成功！")

    def load_table_map(self) -> None:
        print("⏳ 正在读取数据表结构...")
        payload = self.request(
            "GET",
            f"{self.base_url}/bitable/v1/apps/{self.settings.app_token}/tables",
        )
        self.table_map = {
            item["name"]: item["table_id"]
            for item in payload.get("items", [])
        }
        print(f"✅ 已发现 {len(self.table_map)} 张数据表。")

    def list_record_ids(self, table_id: str) -> list[str]:
        record_ids: list[str] = []
        page_token = ""

        while True:
            payload = self.request(
                "GET",
                f"{self.base_url}/bitable/v1/apps/{self.settings.app_token}/tables/{table_id}/records",
                params={"page_size": 100, "page_token": page_token},
            )
            for item in payload.get("items", []):
                record_id = item.get("record_id")
                if record_id:
                    record_ids.append(record_id)

            if not payload.get("has_more"):
                break
            page_token = payload.get("page_token", "")

        return record_ids

    def delete_records(self, table_id: str, record_ids: list[str]) -> None:
        for record_id in record_ids:
            self.request(
                "DELETE",
                f"{self.base_url}/bitable/v1/apps/{self.settings.app_token}/tables/{table_id}/records/{record_id}",
            )

    def create_record(self, table_id: str, schema, fields: dict) -> None:
        self.request(
            "POST",
            f"{self.base_url}/bitable/v1/apps/{self.settings.app_token}/tables/{table_id}/records",
            json={"fields": self.prepare_fields(schema, fields)},
        )

    def prepare_fields(self, schema, fields: dict) -> dict:
        link_fields = {
            field["field_name"]
            for field in schema.fields
            if field.get("type") == 15
        }
        number_fields = {
            field["field_name"]
            for field in schema.fields
            if field.get("type") == 2
        }

        processed: dict = {}
        for key, value in fields.items():
            if value in (None, "", [], {}):
                continue

            if key in number_fields:
                number = self.number_or_none(value)
                if number is None:
                    continue
                processed[key] = number
                continue

            if key in link_fields:
                link = self.clean_text(value)
                if not link or link == "#":
                    continue
                processed[key] = {"link": link, "text": link}
                continue

            processed[key] = value

        return processed

    def convert_record(self, task_name: str, record: dict) -> dict:
        converter = getattr(self, f"convert_{task_name}", None)
        if not converter:
            raise RuntimeError(f"未实现 mock 转换器: {task_name}")
        return converter(record)

    def attach_media_fields(self, task_name: str, task, source_record: dict, fields: dict) -> dict:
        if not task.media:
            return fields

        source_value = self.resolve_media_source_value(task_name, task, source_record)
        if not source_value or source_value == "#":
            return fields

        try:
            media_payload = self.resolve_media_payload(
                task_name=task_name,
                source_record=source_record,
                source_value=source_value,
            )
            file_token = self.upload_media(media_payload)
            fields[task.media.field] = [{"file_token": file_token}]
            print(f"   🖼️ 已上传附件 {task.media.field}: {media_payload['name']}")
        except Exception as exc:
            label = self.record_label(task_name, source_record)
            print(f"   ⚠️ 跳过附件 {task.media.field} [{label}]: {exc}")
        return fields

    def resolve_media_source_value(self, task_name: str, task, source_record: dict) -> str:
        source_value = self.clean_text(source_record.get(task.media.field.lower()))
        if source_value:
            return source_value

        if task_name == "team" and task.media.field == "Avatar":
            return DEFAULT_TEAM_AVATAR

        return ""

    def resolve_media_payload(
        self,
        *,
        task_name: str,
        source_record: dict,
        source_value: str,
    ) -> dict:
        if source_value.startswith("http://") or source_value.startswith("https://"):
            return self.fetch_remote_media(task_name, source_record, source_value)
        return self.read_local_media(task_name, source_record, source_value)

    def read_local_media(
        self,
        task_name: str,
        source_record: dict,
        source_value: str,
    ) -> dict:
        file_path = self.resolve_local_asset_path(source_value)
        if not file_path.exists():
            raise FileNotFoundError(f"找不到本地附件: {file_path}")

        content = file_path.read_bytes()
        content_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
        return {
            "name": file_path.name,
            "content": content,
            "content_type": content_type,
            "task_name": task_name,
            "label": self.record_label(task_name, source_record),
        }

    def fetch_remote_media(
        self,
        task_name: str,
        source_record: dict,
        source_value: str,
    ) -> dict:
        import requests

        response = requests.get(
            source_value,
            timeout=30,
            proxies=self.proxies,
        )
        if response.status_code != 200:
            raise RuntimeError(
                f"下载远程附件失败: HTTP {response.status_code} -> {source_value}"
            )

        content_type = (response.headers.get("Content-Type") or "").split(";")[0].strip()
        file_name = self.infer_remote_filename(
            task_name=task_name,
            source_record=source_record,
            source_value=source_value,
            content_type=content_type,
        )
        return {
            "name": file_name,
            "content": response.content,
            "content_type": content_type or "application/octet-stream",
            "task_name": task_name,
            "label": self.record_label(task_name, source_record),
        }

    def resolve_local_asset_path(self, source_value: str) -> Path:
        if source_value.startswith("/"):
            return self.repo_root / source_value.lstrip("/")
        return (self.data_file.parent / source_value).resolve()

    def infer_remote_filename(
        self,
        *,
        task_name: str,
        source_record: dict,
        source_value: str,
        content_type: str,
    ) -> str:
        from feishu_sync.utils import sanitize_filename

        url_name = Path(unquote(urlparse(source_value).path)).name
        suffix = Path(url_name).suffix.lower()
        if not suffix:
            suffix = mimetypes.guess_extension(content_type or "") or ""
        if suffix == ".jpe":
            suffix = ".jpg"

        base_name = sanitize_filename(self.record_label(task_name, source_record))
        return f"{base_name}{suffix}" if suffix else base_name

    def record_label(self, task_name: str, source_record: dict) -> str:
        if task_name == "team":
            return (
                self.nested_text(source_record, "name", "en")
                or self.nested_text(source_record, "name", "zh")
                or "team-member"
            )
        return (
            self.nested_text(source_record, "title", "en")
            or self.nested_text(source_record, "title", "zh")
            or task_name
        )

    def upload_media(self, media_payload: dict) -> str:
        import requests

        if not self.tenant_access_token:
            raise RuntimeError("尚未完成飞书鉴权")

        content = media_payload["content"]
        content_type = media_payload.get("content_type") or "application/octet-stream"
        parent_type = "bitable_image" if content_type.startswith("image/") else "bitable_file"
        checksum = hashlib.md5(content).hexdigest()

        response = requests.post(
            f"{self.base_url}/drive/v1/medias/upload_all",
            headers={"Authorization": f"Bearer {self.tenant_access_token}"},
            data={
                "file_name": media_payload["name"],
                "parent_type": parent_type,
                "parent_node": self.settings.app_token,
                "size": str(len(content)),
                "checksum": checksum,
            },
            files={
                "file": (
                    media_payload["name"],
                    content,
                    content_type,
                )
            },
            timeout=60,
            proxies=self.proxies,
        )
        payload = response.json()
        if payload.get("code") != 0:
            raise RuntimeError(
                f"上传附件失败 [{media_payload['label']}]: {payload.get('msg')} (code={payload.get('code')})"
            )
        file_token = payload.get("data", {}).get("file_token")
        if not file_token:
            raise RuntimeError(f"上传附件失败 [{media_payload['label']}]: 未返回 file_token")
        return file_token

    def convert_team(self, record: dict) -> dict:
        destination = record.get("destination") or record.get("dest") or {}
        links = record.get("links") or {}

        return self.compact(
            {
                "Name_zh": self.nested_text(record, "name", "zh"),
                "Name_en": self.nested_text(record, "name", "en"),
                "Group_ID": self.clean_text(record.get("group_id")),
                "Rank": self.int_or_none(record.get("rank")),
                "Admission_Year": self.int_or_none(record.get("year")),
                "Title_zh": self.nested_text(record, "title", "zh"),
                "Title_en": self.nested_text(record, "title", "en"),
                "Role_zh": self.nested_text(record, "role", "zh"),
                "Role_en": self.nested_text(record, "role", "en"),
                "Bio_zh": self.nested_text(record, "bio", "zh"),
                "Bio_en": self.nested_text(record, "bio", "en"),
                "Email": self.clean_text(record.get("email")),
                "Dest_zh": self.clean_text(destination.get("zh")),
                "Dest_en": self.clean_text(destination.get("en")),
                "Link_Homepage": self.clean_text(links.get("homepage")),
                "Link_Scholar": self.clean_text(links.get("scholar")),
                "Link_GitHub": self.clean_text(links.get("github")),
                "Link_LinkedIn": self.clean_text(links.get("linkedin")),
                "Link_Zhihu": self.clean_text(links.get("zhihu")),
            }
        )

    def convert_news(self, record: dict) -> dict:
        category = record.get("category") or {}
        return self.compact(
            {
                "Date": self.date_to_millis(record.get("date")),
                "Category_zh": self.clean_text(category.get("zh")),
                "Category_en": self.clean_text(category.get("en")),
                "Title_zh": self.nested_text(record, "title", "zh"),
                "Title_en": self.nested_text(record, "title", "en"),
                "Desc_zh": self.nested_text(record, "description", "zh"),
                "Desc_en": self.nested_text(record, "description", "en"),
                "Link": self.clean_text(record.get("link")),
            }
        )

    def convert_publications(self, record: dict) -> dict:
        links = record.get("links") or {}
        abstract = record.get("abstract") or {}
        return self.compact(
            {
                "Title_zh": self.nested_text(record, "title", "zh"),
                "Title_en": self.nested_text(record, "title", "en"),
                "Authors": self.clean_text(record.get("authors")),
                "Type": self.clean_text(record.get("type")),
                "Venue": self.clean_text(record.get("venue")),
                "Year": self.int_or_none(record.get("year")),
                "Highlight": self.clean_text(record.get("highlight")),
                "Abstract_zh": self.clean_text(abstract.get("zh")),
                "Abstract_en": self.clean_text(abstract.get("en")),
                "Link_Paper": self.clean_text(links.get("paper")),
                "Link_Code": self.clean_text(links.get("code")),
                "Link_Project": self.clean_text(links.get("project")),
                "Link_Video": self.clean_text(links.get("video")),
            }
        )

    def convert_research(self, record: dict) -> dict:
        points = record.get("points") or {}
        return self.compact(
            {
                "Title_zh": self.nested_text(record, "title", "zh"),
                "Title_en": self.nested_text(record, "title", "en"),
                "Icon": self.clean_text(record.get("icon")),
                "Desc_zh": self.nested_text(record, "description", "zh"),
                "Desc_en": self.nested_text(record, "description", "en"),
                "Points_zh": self.lines_text(points.get("zh")),
                "Points_en": self.lines_text(points.get("en")),
            }
        )

    def convert_positions(self, record: dict) -> dict:
        tags = record.get("tags") or {}
        raw_theme = self.clean_text(record.get("theme"))
        theme = THEME_FALLBACKS.get(raw_theme, raw_theme)

        return self.compact(
            {
                "Title_zh": self.nested_text(record, "title", "zh"),
                "Title_en": self.nested_text(record, "title", "en"),
                "Dept_zh": self.nested_text(record, "department", "zh"),
                "Dept_en": self.nested_text(record, "department", "en"),
                "Count_zh": self.nested_text(record, "count", "zh"),
                "Count_en": self.nested_text(record, "count", "en"),
                "Theme": theme,
                "Icon": self.clean_text(record.get("icon")),
                "Desc_zh": self.nested_text(record, "description", "zh"),
                "Desc_en": self.nested_text(record, "description", "en"),
                "Tags_zh": self.tags_text(tags.get("zh")),
                "Tags_en": self.tags_text(tags.get("en")),
                "Link": self.clean_text(record.get("link")),
            }
        )

    def request(
        self,
        method: str,
        url: str,
        *,
        params: dict | None = None,
        json: dict | None = None,
        use_auth: bool = True,
    ) -> dict:
        import requests

        headers = {"Content-Type": "application/json; charset=utf-8"}
        if use_auth:
            if not self.tenant_access_token:
                raise RuntimeError("尚未完成飞书鉴权")
            headers["Authorization"] = f"Bearer {self.tenant_access_token}"

        response = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            json=json,
            timeout=30,
            proxies=self.proxies,
        )

        payload = response.json()
        if payload.get("code") != 0:
            raise RuntimeError(
                f"飞书接口调用失败: {payload.get('msg')} (code={payload.get('code')})"
            )

        data = payload.get("data")
        if isinstance(data, dict):
            return data
        return payload

    @staticmethod
    def clean_text(value) -> str:
        if value in (None, "None"):
            return ""
        return str(value).strip()

    @classmethod
    def nested_text(cls, record: dict, key: str, subkey: str) -> str:
        nested = record.get(key) or {}
        if not isinstance(nested, dict):
            return ""
        return cls.clean_text(nested.get(subkey))

    @classmethod
    def compact(cls, data: dict) -> dict:
        return {
            key: value
            for key, value in data.items()
            if value not in (None, "", [], {})
        }

    @classmethod
    def int_or_none(cls, value):
        text = cls.clean_text(value)
        if not text:
            return None
        try:
            return int(float(text))
        except (TypeError, ValueError):
            return None

    @classmethod
    def number_or_none(cls, value):
        text = cls.clean_text(value)
        if not text:
            return None
        try:
            number = float(text)
        except (TypeError, ValueError):
            return None
        if number.is_integer():
            return int(number)
        return number

    @classmethod
    def lines_text(cls, value) -> str:
        if isinstance(value, list):
            return "\n".join(cls.clean_text(item) for item in value if cls.clean_text(item))
        return cls.clean_text(value)

    @classmethod
    def tags_text(cls, value) -> str:
        if isinstance(value, list):
            return ", ".join(cls.clean_text(item) for item in value if cls.clean_text(item))
        return cls.clean_text(value)

    @classmethod
    def date_to_millis(cls, value) -> int | None:
        text = cls.clean_text(value)
        if not text:
            return None

        for fmt in ("%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d", "%Y-%m", "%Y.%m", "%Y/%m"):
            try:
                parsed = datetime.strptime(text, fmt)
                return int(parsed.timestamp() * 1000)
            except ValueError:
                continue

        raise ValueError(f"无法解析新闻日期: {text}")


def main() -> None:
    args = parse_args()
    if not args.yes:
        print("❌ 此操作会清空飞书中当前受管表的记录。请追加 --yes 确认执行。")
        raise SystemExit(1)

    try:
        seeder = MockFeishuSeeder(
            config_file=args.config_file,
            data_file=args.data_file,
        )
        seeder.seed()
    except Exception as exc:
        print(f"❌ 写入 mock 数据失败: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
