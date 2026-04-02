from __future__ import annotations

import os
import re


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"未找到环境变量 {name}")
    return value


def sanitize_filename(name: str) -> str:
    if not name:
        return "default"
    normalized = str(name).strip().replace(" ", "_")
    return re.sub(r"[^a-zA-Z0-9_\-]", "", normalized).lower() or "default"
