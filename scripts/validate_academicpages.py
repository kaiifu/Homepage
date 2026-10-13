"""Structural checks for the AIFu Lab Academic Pages source."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PAGES = {
    "about.md": "/",
    "research.md": "/research/",
    "team.md": "/team/",
    "outputs.md": "/outputs/",
    "teaching.md": "/teaching/",
    "opportunities.md": "/opportunities/",
    "contact.md": "/contact/",
    "cv.md": "/cv/",
    "404.md": "/404.html",
}

EXPECTED_NAV = {
    "/research/",
    "/team/",
    "/outputs/",
    "/teaching/",
    "/opportunities/",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {path.relative_to(ROOT)}: {exc}")


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"missing front matter: {path.relative_to(ROOT)}")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError:
        fail(f"incomplete front matter: {path.relative_to(ROOT)}")
    parsed = yaml.safe_load(raw)
    if not isinstance(parsed, dict):
        fail(f"front matter is not a mapping: {path.relative_to(ROOT)}")
    return parsed


def main() -> int:
    config = load_yaml(ROOT / "_config.yml")
    if config.get("title") != "AIFu Lab":
        fail("site title must be AIFu Lab")
    if config.get("baseurl") != "/Homepage":
        fail("GitHub Pages baseurl must be /Homepage")

    navigation = load_yaml(ROOT / "_data" / "navigation.yml")
    nav_urls = {item["url"] for item in navigation.get("main", [])}
    if nav_urls != EXPECTED_NAV:
        fail("navigation does not match the five primary inner pages")

    for filename, permalink in PAGES.items():
        path = ROOT / "_pages" / filename
        if not path.is_file():
            fail(f"missing page: _pages/{filename}")
        if front_matter(path).get("permalink") != permalink:
            fail(f"wrong permalink in _pages/{filename}")

    outputs = load_yaml(ROOT / "_data" / "outputs.yml")
    if len(outputs.get("journals", [])) != 14:
        fail("expected 14 migrated journal articles")
    if len(outputs.get("conferences", [])) != 5:
        fail("expected 5 migrated conference papers")

    avatar = config.get("author", {}).get("avatar")
    if avatar and not (ROOT / "images" / avatar).is_file():
        fail(f"missing author avatar: images/{avatar}")

    members = load_yaml(ROOT / "_data" / "members.yml")
    people = [members.get("leader", {})]
    for group in ("graduate_students", "undergraduate_students", "alumni"):
        people.extend(members.get(group, []) or [])
    for person in people:
        photo = person.get("photo")
        if photo and not (ROOT / photo.lstrip("/")).is_file():
            fail(f"missing member photo: {photo}")

    required_theme_paths = (
        "_layouts/default.html",
        "_layouts/single.html",
        "_includes/masthead.html",
        "_sass/layout/_aifu.scss",
        "_sass/vendor/font-awesome/fontawesome.scss",
        "_sass/vendor/breakpoint/_breakpoint.scss",
        "_sass/vendor/susy/_susy.scss",
        "assets/css/main.scss",
        "assets/js/main.min.js",
        "Gemfile",
        "LICENSE",
    )
    for relative in required_theme_paths:
        if not (ROOT / relative).is_file():
            fail(f"missing Academic Pages file: {relative}")

    for path in (ROOT / "_sass").rglob("*.scss"):
        if "math.div" in path.read_text(encoding="utf-8"):
            fail(f"legacy GitHub Pages Sass cannot compile math.div: {path.relative_to(ROOT)}")

    print("OK: Academic Pages source, 9 pages, 5 navigation items, 14 journals, 5 conferences")
    return 0


if __name__ == "__main__":
    sys.exit(main())
