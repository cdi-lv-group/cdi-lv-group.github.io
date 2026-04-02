from __future__ import annotations

import glob
import os
from pathlib import Path

import requests

from .config import SyncSettings, SyncTask
from .utils import sanitize_filename


class FeishuReader:
    def __init__(self, settings: SyncSettings, app_id: str, app_secret: str):
        self.settings = settings
        self.app_id = app_id
        self.app_secret = app_secret
        self.base_url = "https://open.feishu.cn/open-apis"
        self.tenant_access_token: str | None = None
        self.table_map: dict[str, str] = {}
        self.proxies = {"http": None, "https": None}

    def authenticate(self) -> None:
        print("⏳ [1/4] 正在请求飞书 API 授权...")
        response = requests.post(
            f"{self.base_url}/auth/v3/tenant_access_token/internal",
            json={"app_id": self.app_id, "app_secret": self.app_secret},
            proxies=self.proxies,
            timeout=10,
        )
        payload = response.json()
        if payload.get("code") != 0:
            raise RuntimeError(f"授权失败: {payload.get('msg')}")

        self.tenant_access_token = payload.get("tenant_access_token")
        print("✅ 授权成功！")

    def _headers(self) -> dict[str, str]:
        if not self.tenant_access_token:
            raise RuntimeError("尚未完成飞书鉴权")

        return {
            "Authorization": f"Bearer {self.tenant_access_token}",
            "Content-Type": "application/json; charset=utf-8",
        }

    def load_table_map(self) -> None:
        print("⏳ [2/4] 获取数据表结构...")
        response = requests.get(
            f"{self.base_url}/bitable/v1/apps/{self.settings.app_token}/tables",
            headers=self._headers(),
            proxies=self.proxies,
            timeout=15,
        )
        payload = response.json()
        if payload.get("code") != 0:
            raise RuntimeError(f"获取表结构失败: {payload.get('msg')}")

        self.table_map = {
            item["name"]: item["table_id"]
            for item in payload.get("data", {}).get("items", [])
        }
        print(f"📊 成功找到 {len(self.table_map)} 个数据表。")

    def fetch_records(self, task: SyncTask) -> list[dict]:
        table_id = self.table_map.get(task.table_name)
        if not table_id:
            print(f"⚠️ 未找到数据表：{task.table_name}")
            return []

        url = f"{self.base_url}/bitable/v1/apps/{self.settings.app_token}/tables/{table_id}/records"
        records: list[dict] = []
        page_token = ""
        has_more = True

        print(f"\n📥 [3/4] 拉取与处理：{task.table_name}")

        while has_more:
            response = requests.get(
                url,
                headers=self._headers(),
                params={"page_size": 100, "page_token": page_token},
                proxies=self.proxies,
                timeout=30,
            )
            payload = response.json()
            if payload.get("code") != 0:
                raise RuntimeError(f"拉取 {task.table_name} 失败: {payload.get('msg')}")

            data = payload.get("data", {})
            for item in data.get("items", []):
                record = item.get("fields", {})
                self._attach_media_path(task, record)
                records.append(record)

            has_more = bool(data.get("has_more"))
            page_token = data.get("page_token", "")

        return records

    def _attach_media_path(self, task: SyncTask, record: dict) -> None:
        if not task.media:
            return

        media_items = record.get(task.media.field)
        if not isinstance(media_items, list) or not media_items:
            return

        media = media_items[0]
        file_token = media.get("file_token")
        download_url = media.get("url")
        original_name = media.get("name", "")
        if not file_token or not download_url:
            return

        raw_slug = str(record.get(task.media.slug_key, ""))
        if task.media.truncate_words:
            raw_slug = "_".join(raw_slug.split()[: task.media.truncate_words])

        local_path = self._sync_media(
            file_token=file_token,
            download_url=download_url,
            slug=sanitize_filename(raw_slug),
            folder=task.media.folder,
            original_filename=original_name,
        )
        if local_path:
            record[f"local_{task.media.field.lower()}_path"] = local_path

    def _sync_media(
        self,
        file_token: str,
        download_url: str,
        slug: str,
        folder: str,
        original_filename: str,
    ) -> str:
        extension = Path(original_filename).suffix.lower() or ".jpg"
        token_suffix = file_token[:8].lower()
        save_dir = Path("assets/images") / folder
        save_name = f"{slug}_{token_suffix}{extension}"
        save_path = save_dir / save_name

        save_dir.mkdir(parents=True, exist_ok=True)
        if save_path.exists():
            return f"/{save_path.as_posix()}"

        for old_file in glob.glob(str(save_dir / f"{slug}_*.*")):
            try:
                os.remove(old_file)
                print(f"      🗑️ 清理旧图: {Path(old_file).name}")
            except OSError:
                pass

        if self._download_media(download_url, save_path):
            return f"/{save_path.as_posix()}"
        return ""

    def _download_media(self, download_url: str, save_path: Path) -> bool:
        print(f"      ⬇️ 下载图片: {save_path.name} ...", end="", flush=True)
        response = requests.get(
            download_url,
            headers=self._headers(),
            proxies=self.proxies,
            timeout=30,
        )
        if response.status_code != 200:
            print(f" [失败: HTTP {response.status_code}]")
            return False

        save_path.write_bytes(response.content)
        print(" [成功]")
        return True
