"""Static checks for the AIFu Lab Jekyll source tree."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
PREVIEW = ROOT / ".preview" / "Homepage"
EXPECTED_PAGES = {
    "index.html": "/",
    "research.html": "/research/",
    "team.html": "/team/",
    "outputs.html": "/outputs/",
    "teaching.html": "/teaching/",
    "opportunities.html": "/opportunities/",
    "contact.html": "/contact/",
    "cv.html": "/cv/",
}
SOURCE_FILES = [
    *ROOT.glob("*.html"),
    *ROOT.glob("_layouts/*.html"),
    *ROOT.glob("_includes/*.html"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.name} has no YAML front matter")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError:
        fail(f"{path.name} has incomplete YAML front matter")
    parsed = yaml.safe_load(raw)
    if not isinstance(parsed, dict):
        fail(f"{path.name} front matter is not a mapping")
    return parsed


def check_yaml() -> dict[str, object]:
    loaded: dict[str, object] = {}
    for path in sorted((ROOT / "_data").glob("*.yml")):
        try:
            loaded[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            fail(f"invalid YAML in {path.relative_to(ROOT)}: {exc}")
    if not loaded:
        fail("no data files found")
    return loaded


def check_pages(data: dict[str, object]) -> None:
    for filename, permalink in EXPECTED_PAGES.items():
        path = ROOT / filename
        if not path.exists():
            fail(f"missing page: {filename}")
        meta = front_matter(path)
        if meta.get("permalink") != permalink:
            fail(f"{filename} permalink should be {permalink!r}")

    navigation = data.get("navigation")
    if not isinstance(navigation, list):
        fail("navigation.yml must contain a list")
    nav_urls = {item.get("url") for item in navigation if isinstance(item, dict)}
    if nav_urls != set(EXPECTED_PAGES.values()):
        fail("navigation URLs do not match the eight expected pages")


def check_content(data: dict[str, object]) -> None:
    members = data.get("members")
    if not isinstance(members, dict) or not members.get("leader"):
        fail("members.yml must define the group leader")

    outputs = data.get("outputs")
    if not isinstance(outputs, dict):
        fail("outputs.yml must contain a mapping")
    if len(outputs.get("journals", [])) != 14:
        fail("expected 14 migrated journal articles")
    if len(outputs.get("conferences", [])) != 5:
        fail("expected 5 migrated conference papers")

    site_data = data.get("site")
    if not isinstance(site_data, dict):
        fail("site.yml must contain a mapping")
    photo = site_data.get("leader", {}).get("photo", "")
    photo_path = ROOT / str(photo).lstrip("/")
    if not photo_path.is_file():
        fail(f"leader photo not found: {photo}")


def check_templates() -> None:
    stale_phrases = ("A PhD Student", "Currently, I am a PhD student", "ece.kaifu@my.cityu.edu.hk")
    for path in SOURCE_FILES:
        if path.name == "index-demo.html":
            continue
        text = path.read_text(encoding="utf-8")
        if text.count("{{") != text.count("}}"):
            fail(f"unbalanced Liquid output delimiters in {path.relative_to(ROOT)}")
        if text.count("{%") != text.count("%}"):
            fail(f"unbalanced Liquid tag delimiters in {path.relative_to(ROOT)}")
        for phrase in stale_phrases:
            if phrase in text:
                fail(f"stale identity phrase in {path.relative_to(ROOT)}: {phrase}")
        if re.search(r'(?:href|src)="/(?!/)', text):
            fail(f"root-absolute asset/link bypasses relative_url in {path.relative_to(ROOT)}")


def check_preview_if_present() -> int:
    if not PREVIEW.exists():
        return 0

    html_files = sorted(PREVIEW.rglob("*.html"))
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        if "{{" in text or "{%" in text:
            fail(f"unrendered Liquid remains in {path.relative_to(ROOT)}")

        for raw_url in re.findall(r'(?:href|src)="([^"]+)"', text):
            parsed = urlsplit(raw_url)
            if parsed.scheme or parsed.netloc or raw_url.startswith(("mailto:", "#")):
                continue
            if not parsed.path.startswith("/Homepage/"):
                fail(f"preview link is not baseurl-safe in {path.relative_to(ROOT)}: {raw_url}")

            relative = parsed.path.removeprefix("/Homepage/")
            target = PREVIEW / relative
            if parsed.path.endswith("/"):
                target = target / "index.html"
            if not target.is_file():
                fail(f"broken preview link in {path.relative_to(ROOT)}: {raw_url}")
    return len(html_files)


def main() -> int:
    data = check_yaml()
    check_pages(data)
    check_content(data)
    check_templates()
    preview_pages = check_preview_if_present()
    print(
        "OK: 8 pages, 6 data files, 14 journals, 5 conferences, "
        "balanced Liquid delimiters, and baseurl-safe internal links"
        + (f"; {preview_pages} rendered preview pages have no broken local links" if preview_pages else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

