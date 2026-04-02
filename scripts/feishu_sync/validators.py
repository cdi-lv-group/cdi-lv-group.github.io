from __future__ import annotations

from dataclasses import dataclass, field
import re

ALLOWED_GROUP_IDS = {
    "professor",
    "associate_prof",
    "assistant_prof",
    "researchers",
    "phd",
    "master",
    "undergrad",
    "interns",
    "alumni",
}
ALLOWED_POSITION_THEMES = {"slate", "blue", "cyan", "emerald", "violet"}
ALLOWED_PUBLICATION_TYPES = {"conference", "journal", "preprint", "workshop", "book"}
EMPTY_LITERALS = {"", "#", "none", "null", "n/a", "na", "nil"}
DEFAULT_TEAM_AVATAR = "/assets/images/team/default-avatar.svg"


@dataclass
class ValidationReport:
    task_name: str
    total_records: int
    valid_records: list[dict]
    reason_counts: dict[str, int] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    aborted: bool = False

    @property
    def dropped_records(self) -> int:
        return self.total_records - len(self.valid_records)


def validate_records(task_name: str, records: list[dict]) -> ValidationReport:
    validator = _VALIDATORS.get(task_name)
    if not validator:
        return ValidationReport(task_name=task_name, total_records=len(records), valid_records=records)

    valid_records: list[dict] = []
    reason_counts: dict[str, int] = {}

    for record in records:
        clean_record, reason = validator(record)
        if clean_record is None:
            reason_counts[reason] = reason_counts.get(reason, 0) + 1
            continue
        valid_records.append(clean_record)

    report = ValidationReport(
        task_name=task_name,
        total_records=len(records),
        valid_records=valid_records,
        reason_counts=reason_counts,
    )

    if reason_counts:
        reason_summary = ", ".join(
            f"{reason} x{count}" for reason, count in sorted(reason_counts.items())
        )
        report.warnings.append(f"已丢弃 {report.dropped_records} 条异常记录：{reason_summary}")

    if report.total_records == 0:
        report.aborted = True
        report.errors.append("数据表返回空结果，已中止写入以保护现有 YAML。")
        return report

    if not valid_records:
        report.aborted = True
        report.errors.append("所有记录都未通过校验，已中止写入以保护现有 YAML。")
        return report

    invalid_ratio = report.dropped_records / report.total_records
    if report.total_records >= 4 and invalid_ratio > 0.45:
        report.aborted = True
        report.errors.append(
            f"异常记录比例过高 ({report.dropped_records}/{report.total_records})，已中止写入。"
        )

    return report


def _validate_team(record: dict) -> tuple[dict | None, str]:
    name = _normalize_bilingual(record.get("name"))
    title = _normalize_bilingual(record.get("title"))
    role = _normalize_bilingual(record.get("role"), fill_missing=False)
    bio = _normalize_bilingual(record.get("bio"), fill_missing=True)
    destination = _normalize_bilingual(record.get("destination"), fill_missing=True)
    group_id = _normalize_group_id(record.get("group_id"))
    if not group_id:
        return None, "group_id 缺失或非法"
    if not _has_bilingual_value(name):
        return None, "name 缺失"
    if not _has_bilingual_value(title):
        return None, "title 缺失"

    clean_record = {
        "name": name,
        "group_id": group_id,
        "rank": _normalize_int(record.get("rank"), default=99),
        "year": _normalize_int(record.get("year")),
        "title": title,
        "role": role,
        "avatar": _clean_text(record.get("avatar")) or DEFAULT_TEAM_AVATAR,
        "bio": bio,
        "email": _clean_email(record.get("email")),
        "destination": destination,
        "links": _clean_link_map(record.get("links")),
    }
    return clean_record, ""


def _validate_publication(record: dict) -> tuple[dict | None, str]:
    title = _normalize_bilingual(record.get("title"))
    abstract = _normalize_bilingual(record.get("abstract"), fill_missing=True)
    authors = _clean_text(record.get("authors"))
    venue = _clean_text(record.get("venue"))
    year = _normalize_year(record.get("year"))
    if not _has_bilingual_value(title):
        return None, "title 缺失"
    if not authors:
        return None, "authors 缺失"
    if not venue:
        return None, "venue 缺失"
    if year is None:
        return None, "year 缺失或非法"

    pub_type = _clean_text(record.get("type")).lower()
    if pub_type and pub_type not in ALLOWED_PUBLICATION_TYPES:
        pub_type = ""

    clean_record = {
        "title": title,
        "authors": authors,
        "type": pub_type,
        "venue": venue,
        "year": year,
        "highlight": _clean_text(record.get("highlight")),
        "image": _clean_text(record.get("image")),
        "abstract": abstract,
        "links": _clean_link_map(record.get("links")),
    }
    return clean_record, ""


def _validate_research(record: dict) -> tuple[dict | None, str]:
    title = _normalize_bilingual(record.get("title"))
    description = _normalize_bilingual(record.get("description"))
    if not _has_bilingual_value(title):
        return None, "title 缺失"
    if not _has_bilingual_value(description):
        return None, "description 缺失"

    clean_record = {
        "icon": _clean_text(record.get("icon")) or "✦",
        "title": title,
        "description": description,
        "points": {
            "zh": _clean_list((record.get("points") or {}).get("zh")),
            "en": _clean_list((record.get("points") or {}).get("en")),
        },
        "image": _clean_text(record.get("image")),
    }
    return clean_record, ""


def _validate_position(record: dict) -> tuple[dict | None, str]:
    title = _normalize_bilingual(record.get("title"))
    department = _normalize_bilingual(record.get("department"))
    description = _normalize_bilingual(record.get("description"))
    if not _has_bilingual_value(title):
        return None, "title 缺失"
    if not _has_bilingual_value(department):
        return None, "department 缺失"
    if not _has_bilingual_value(description):
        return None, "description 缺失"

    theme = _clean_text(record.get("theme")).lower()
    if theme not in ALLOWED_POSITION_THEMES:
        theme = "blue"

    clean_record = {
        "title": title,
        "department": department,
        "count": _normalize_bilingual(record.get("count"), fill_missing=True),
        "theme": theme,
        "icon": _clean_text(record.get("icon")) or "✦",
        "description": description,
        "tags": {
            "zh": _clean_list((record.get("tags") or {}).get("zh")),
            "en": _clean_list((record.get("tags") or {}).get("en")),
        },
        "link": _clean_link(record.get("link")),
    }
    return clean_record, ""


def _validate_news(record: dict) -> tuple[dict | None, str]:
    title = _normalize_bilingual(record.get("title"))
    if not _has_bilingual_value(title):
        return None, "title 缺失"

    date_value = _clean_date(record.get("date"))
    if not date_value:
        return None, "date 缺失或非法"

    category = _normalize_bilingual(record.get("category"), fill_missing=True)
    if not _has_bilingual_value(category):
        category = {"zh": "实验室动态", "en": "Lab Event"}

    clean_record = {
        "date": date_value,
        "category": category,
        "title": title,
        "description": _normalize_bilingual(record.get("description"), fill_missing=True),
        "link": _clean_link(record.get("link")),
    }
    return clean_record, ""


def _normalize_bilingual(value, *, fill_missing: bool = True) -> dict[str, str]:
    if isinstance(value, dict):
        zh = _clean_text(value.get("zh"))
        en = _clean_text(value.get("en"))
    else:
        text = _clean_text(value)
        zh = text
        en = text

    if fill_missing:
        if not zh and en:
            zh = en
        if not en and zh:
            en = zh

    return {"zh": zh, "en": en}


def _has_bilingual_value(value: dict[str, str]) -> bool:
    return bool(value.get("zh") or value.get("en"))


def _normalize_group_id(value) -> str:
    group_id = _clean_text(value).lower()
    if group_id == "intern":
        group_id = "interns"
    if group_id in ALLOWED_GROUP_IDS:
        return group_id
    return ""


def _normalize_int(value, default: int | None = None) -> int | None:
    if value in (None, ""):
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _normalize_year(value) -> int | None:
    year = _normalize_int(value)
    if year is None:
        return None
    if 1900 <= year <= 2100:
        return year
    return None


def _clean_email(value) -> str:
    email = _clean_text(value).lower()
    if email and "@" in email:
        return email
    return ""


def _clean_link(value) -> str:
    link = _clean_text(value)
    if not link:
        return ""
    return link


def _clean_link_map(value) -> dict[str, str]:
    if not isinstance(value, dict):
        return {}
    return {
        key: clean_value
        for key, raw_value in value.items()
        if (clean_value := _clean_link(raw_value))
    }


def _clean_list(value) -> list[str]:
    if not value:
        return []
    items = value if isinstance(value, list) else [value]
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        clean_item = _clean_text(item)
        if not clean_item or clean_item in seen:
            continue
        seen.add(clean_item)
        result.append(clean_item)
    return result


def _clean_date(value) -> str:
    date_text = _clean_text(value)
    if not date_text:
        return ""
    if re.fullmatch(r"\d{4}\.\d{2}\.\d{2}", date_text):
        return date_text.replace(".", "-")
    if re.fullmatch(r"\d{4}\.\d{2}", date_text):
        return date_text.replace(".", "-")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_text):
        return date_text
    if re.fullmatch(r"\d{4}-\d{2}", date_text):
        return date_text
    return ""


def _clean_text(value) -> str:
    if value is None:
        return ""

    text = str(value).replace("\u200b", "").strip()
    if not text:
        return ""

    lowered = text.lower()
    if lowered in EMPTY_LITERALS:
        return ""

    for marker in (
        "🔴[必填]",
        "⚪[选填]",
        "🔴 [必填]",
        "⚪ [选填]",
        "[必填]",
        "[选填]",
    ):
        text = text.replace(marker, "")

    text = re.sub(r"^(?:示例[:：]|example[:：])\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^[🔴⚪]\s*", "", text)
    return text.strip()


_VALIDATORS = {
    "team": _validate_team,
    "publications": _validate_publication,
    "research": _validate_research,
    "positions": _validate_position,
    "news": _validate_news,
}
