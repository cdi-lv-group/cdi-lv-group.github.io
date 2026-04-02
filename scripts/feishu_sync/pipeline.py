from __future__ import annotations

from datetime import datetime
from pathlib import Path

import yaml

from .config import SyncTask, load_settings
from .converters import (
    convert_news,
    convert_positions,
    convert_publications,
    convert_research,
    convert_team,
)
from .reader import FeishuReader
from .utils import require_env
from .validators import ValidationReport, validate_records

CONVERTERS = {
    "team": convert_team,
    "publications": convert_publications,
    "research": convert_research,
    "positions": convert_positions,
    "news": convert_news,
}


def run_sync(config_file: str = "feishu_config.yml") -> None:
    settings = load_settings(config_file)
    app_id = require_env("FEISHU_APP_ID")
    app_secret = require_env("FEISHU_APP_SECRET")
    failed_tasks: list[str] = []

    print("=" * 60)
    print("🚀 LV Group - 飞书全量数据同步引擎")
    print("=" * 60)

    reader = FeishuReader(settings=settings, app_id=app_id, app_secret=app_secret)
    reader.authenticate()
    reader.load_table_map()

    print("\n[4/4] 转换数据并写入 YAML 文件...")
    for task in settings.tasks:
        raw_records = reader.fetch_records(task)
        records = raw_records[1:] if settings.skip_sample_row and len(raw_records) > 1 else raw_records
        converter = CONVERTERS.get(task.converter)
        if not converter:
            raise RuntimeError(f"未注册的转换器: {task.converter}")

        clean_data = converter(records)
        validation = validate_records(task.name, clean_data)
        _log_validation_status(task, validation)
        if validation.aborted:
            failed_tasks.append(f"{task.table_name}: {'; '.join(validation.errors)}")
            continue

        _log_media_status(task, validation.valid_records)
        _write_yaml(task, validation.valid_records)

    print("\n" + "=" * 60)
    if failed_tasks:
        print("⚠️ 有数据表因校验失败被保护性跳过：")
        for item in failed_tasks:
            print(f"   - {item}")
        raise RuntimeError("部分数据表未通过校验，现有 YAML 已保留。")

    print("🎉 全量同步完成！")
    print("=" * 60)


def _log_media_status(task: SyncTask, clean_data: list[dict]) -> None:
    if not task.media:
        return

    key = task.media.field.lower()
    print(f"\n🔍 [{task.table_name}] 媒体资产映射：")
    for item in clean_data:
        display_name = (
            item.get("name", {}).get("en")
            or item.get("title", {}).get("en")
            or "Unknown"
        )
        display_name = display_name[:20] + ".." if len(display_name) > 20 else display_name
        asset_path = item.get(key) if key in item else item.get("avatar") or item.get("image")
        status = "✅" if asset_path else "⚠️ 未配图"
        print(f"   {status} {display_name.ljust(22)} -> {asset_path}")


def _log_validation_status(task: SyncTask, report: ValidationReport) -> None:
    print(
        f"    🧪 校验结果: 保留 {len(report.valid_records)}/{report.total_records} 条"
    )
    for warning in report.warnings:
        print(f"    ⚠️ {warning}")
    for error in report.errors:
        print(f"    ❌ {error}")


def _write_yaml(task: SyncTask, data: list[dict]) -> None:
    output_path = Path(task.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as handle:
        handle.write(f"# Auto-generated from Feishu Bitable: {task.table_name}\n")
        handle.write(f"# Sync Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        yaml.safe_dump(
            data,
            handle,
            allow_unicode=True,
            sort_keys=False,
            indent=2,
            default_flow_style=False,
        )

    print(f"    💾 数据已更新: {task.output_file}")


def main() -> None:
    try:
        run_sync()
    except Exception as exc:
        print(f"❌ 同步失败: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
