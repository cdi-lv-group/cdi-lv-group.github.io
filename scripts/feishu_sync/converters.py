from __future__ import annotations

from datetime import datetime

DEFAULT_TEAM_AVATAR = "/assets/images/team/default-avatar.svg"


def _get_text(field) -> str:
    if field in (None, "None"):
        return ""
    return str(field).strip()


def _get_option(field) -> str:
    if isinstance(field, dict):
        return _get_text(field.get("text") or field.get("name"))
    if isinstance(field, list) and field:
        return _get_option(field[0])
    return _get_text(field)


def _get_link(field) -> str:
    if isinstance(field, dict):
        return _get_text(field.get("link") or field.get("text"))
    return _get_text(field)


def _safe_int(value, default: int | None = None) -> int | None:
    text = _get_text(value)
    if not text:
        return default
    try:
        return int(float(text))
    except (TypeError, ValueError):
        return default


def _split_lines(field) -> list[str]:
    return [line.strip() for line in _get_text(field).splitlines() if line.strip()]


def _split_tags(field) -> list[str]:
    return [part.strip() for part in _get_text(field).replace("，", ",").split(",") if part.strip()]


def _compact_links(links: dict[str, str]) -> dict[str, str]:
    return {key: value for key, value in links.items() if value}


def _format_date(field) -> str:
    if isinstance(field, (int, float)):
        return datetime.fromtimestamp(field / 1000).strftime("%Y-%m-%d")
    text = _get_text(field)
    if not text:
        return ""
    if "." in text:
        return text.replace(".", "-")
    return text


def convert_team(records: list[dict]) -> list[dict]:
    people = []
    for record in records:
        avatar = _get_text(record.get("local_avatar_path")) or DEFAULT_TEAM_AVATAR
        item = {
            "name": {
                "zh": _get_text(record.get("Name_zh")),
                "en": _get_text(record.get("Name_en")),
            },
            "group_id": _get_option(record.get("Group_ID")),
            "rank": _safe_int(record.get("Rank"), 99),
            "year": _safe_int(record.get("Admission_Year")),
            "title": {
                "zh": _get_text(record.get("Title_zh")),
                "en": _get_text(record.get("Title_en")),
            },
            "role": {
                "zh": _get_text(record.get("Role_zh")),
                "en": _get_text(record.get("Role_en")),
            },
            "avatar": avatar,
            "bio": {
                "zh": _get_text(record.get("Bio_zh")),
                "en": _get_text(record.get("Bio_en")),
            },
            "email": _get_text(record.get("Email")),
            "destination": {
                "zh": _get_text(record.get("Dest_zh")),
                "en": _get_text(record.get("Dest_en")),
            },
            "links": _compact_links(
                {
                    "homepage": _get_link(record.get("Link_Homepage")),
                    "github": _get_link(record.get("Link_GitHub")),
                    "scholar": _get_link(record.get("Link_Scholar")),
                    "linkedin": _get_link(record.get("Link_LinkedIn")),
                    "zhihu": _get_link(record.get("Link_Zhihu")),
                }
            ),
        }
        people.append(item)

    return sorted(
        people,
        key=lambda item: (
            item.get("rank", 99),
            -(item.get("year") or 0),
            item.get("name", {}).get("en", ""),
        ),
    )


def convert_publications(records: list[dict]) -> list[dict]:
    publications = []
    for record in records:
        publications.append(
            {
                "title": {
                    "zh": _get_text(record.get("Title_zh")),
                    "en": _get_text(record.get("Title_en")),
                },
                "authors": _get_text(record.get("Authors")),
                "type": _get_option(record.get("Type")),
                "venue": _get_text(record.get("Venue")),
                "year": _safe_int(record.get("Year")),
                "highlight": _get_text(record.get("Highlight")),
                "image": _get_text(record.get("local_image_path")),
                "abstract": {
                    "zh": _get_text(record.get("Abstract_zh")),
                    "en": _get_text(record.get("Abstract_en")),
                },
                "links": _compact_links(
                    {
                        "paper": _get_link(record.get("Link_Paper")),
                        "code": _get_link(record.get("Link_Code")),
                        "project": _get_link(record.get("Link_Project")),
                        "video": _get_link(record.get("Link_Video")),
                    }
                ),
            }
        )

    return sorted(
        publications,
        key=lambda item: (item.get("year", 0), item.get("title", {}).get("en", "")),
        reverse=True,
    )


def convert_research(records: list[dict]) -> list[dict]:
    research_areas = []
    for record in records:
        research_areas.append(
            {
                "icon": _get_text(record.get("Icon")),
                "title": {
                    "zh": _get_text(record.get("Title_zh")),
                    "en": _get_text(record.get("Title_en")),
                },
                "description": {
                    "zh": _get_text(record.get("Desc_zh")),
                    "en": _get_text(record.get("Desc_en")),
                },
                "points": {
                    "zh": _split_lines(record.get("Points_zh")),
                    "en": _split_lines(record.get("Points_en")),
                },
                "image": _get_text(record.get("local_image_path")),
            }
        )
    return research_areas


def convert_positions(records: list[dict]) -> list[dict]:
    positions = []
    for record in records:
        positions.append(
            {
                "title": {
                    "zh": _get_text(record.get("Title_zh")),
                    "en": _get_text(record.get("Title_en")),
                },
                "department": {
                    "zh": _get_text(record.get("Dept_zh")),
                    "en": _get_text(record.get("Dept_en")),
                },
                "count": {
                    "zh": _get_text(record.get("Count_zh")),
                    "en": _get_text(record.get("Count_en")),
                },
                "theme": _get_option(record.get("Theme")) or "blue",
                "icon": _get_text(record.get("Icon")),
                "description": {
                    "zh": _get_text(record.get("Desc_zh")),
                    "en": _get_text(record.get("Desc_en")),
                },
                "tags": {
                    "zh": _split_tags(record.get("Tags_zh")),
                    "en": _split_tags(record.get("Tags_en")),
                },
                "link": _get_link(record.get("Link")),
            }
        )
    return positions


def convert_news(records: list[dict]) -> list[dict]:
    news_items = []
    for record in records:
        news_items.append(
            {
                "date": _format_date(record.get("Date")),
                "category": {
                    "zh": _get_option(record.get("Category_zh")),
                    "en": _get_option(record.get("Category_en")),
                },
                "title": {
                    "zh": _get_text(record.get("Title_zh")),
                    "en": _get_text(record.get("Title_en")),
                },
                "description": {
                    "zh": _get_text(record.get("Desc_zh")),
                    "en": _get_text(record.get("Desc_en")),
                },
                "link": _get_link(record.get("Link")),
            }
        )

    return sorted(news_items, key=lambda item: item.get("date", ""), reverse=True)
