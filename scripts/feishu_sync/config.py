from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from .utils import require_env


@dataclass(frozen=True)
class MediaRoute:
    field: str
    folder: str
    slug_key: str
    truncate_words: int = 0


@dataclass(frozen=True)
class SyncTask:
    name: str
    table_name: str
    output_file: str
    converter: str
    media: MediaRoute | None = None


@dataclass(frozen=True)
class SyncSettings:
    app_token: str
    skip_sample_row: bool
    tasks: list[SyncTask]


def load_app_token(config_file: str = "feishu_config.yml") -> str:
    config_path = Path(config_file)
    if not config_path.exists():
        raise FileNotFoundError(f"找不到配置文件: {config_file}")

    with config_path.open("r", encoding="utf-8") as handle:
        raw_config = yaml.safe_load(handle) or {}

    env_name = (raw_config.get("app_token_env") or "").strip()
    if env_name:
        return require_env(env_name)

    raw_token = str(raw_config.get("app_token") or "").strip()
    if raw_token.startswith("${") and raw_token.endswith("}"):
        return require_env(raw_token[2:-1].strip())

    if raw_token and "填入你的" not in raw_token:
        return raw_token

    raise ValueError("配置缺少可用的 app_token，请设置 app_token_env 或 app_token")


def load_settings(config_file: str = "feishu_config.yml") -> SyncSettings:
    config_path = Path(config_file)
    if not config_path.exists():
        raise FileNotFoundError(f"找不到配置文件: {config_file}")

    with config_path.open("r", encoding="utf-8") as handle:
        raw_config = yaml.safe_load(handle) or {}

    app_token = load_app_token(config_file)

    raw_tables = raw_config.get("tables") or {}
    if not raw_tables:
        raise ValueError("配置缺少 tables 同步任务")

    sync_config = raw_config.get("sync") or {}
    tasks: list[SyncTask] = []

    for name, task_config in raw_tables.items():
        table_name = task_config.get("table_name")
        output_file = task_config.get("output_file")
        converter = task_config.get("converter") or name

        if not table_name or not output_file:
            raise ValueError(f"同步任务 {name} 缺少 table_name 或 output_file")

        media = None
        raw_media = task_config.get("media")
        if raw_media:
            media = MediaRoute(
                field=raw_media["field"],
                folder=raw_media["folder"],
                slug_key=raw_media["slug_key"],
                truncate_words=int(raw_media.get("truncate_words", 0) or 0),
            )

        tasks.append(
            SyncTask(
                name=name,
                table_name=table_name,
                output_file=output_file,
                converter=converter,
                media=media,
            )
        )

    return SyncSettings(
        app_token=app_token,
        skip_sample_row=bool(sync_config.get("skip_sample_row", True)),
        tasks=tasks,
    )
