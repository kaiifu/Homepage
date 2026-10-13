"""Render a local QA preview of the Jekyll source with python-liquid.

This is not the production build. GitHub Pages remains the production Jekyll
builder. The script adapts the small Jekyll-specific subset used by this site so
the pages can be visually checked on machines without Ruby.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml

try:
    from liquid import DictLoader, Environment
except ModuleNotFoundError as exc:  # pragma: no cover - environment guidance
    raise SystemExit(
        "python-liquid is required for preview QA. Install it in a temporary "
        "directory and add that directory to PYTHONPATH."
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / ".preview" / "Homepage"
PAGES = [
    "index.html",
    "research.html",
    "team.html",
    "outputs.html",
    "teaching.html",
    "opportunities.html",
    "contact.html",
    "cv.html",
]


def split_front_matter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    _, raw, body = text.split("---\n", 2)
    return yaml.safe_load(raw) or {}, body


def adapt_jekyll_syntax(source: str) -> str:
    """Adapt Jekyll include arguments and include scope for python-liquid."""

    def include_replacement(match: re.Match[str]) -> str:
        filename = match.group(1)
        raw_args = match.group(2).strip()
        converted = []
        for key, value in re.findall(r"([A-Za-z_][\w-]*)=([^\s]+)", raw_args):
            converted.append(f"{key}: {value}")
        suffix = ", " + ", ".join(converted) if converted else ""
        return "{% include '" + filename + "'" + suffix + " %}"

    source = re.sub(r"{%\s*include\s+([^\s%]+)(.*?)%}", include_replacement, source)
    source = source.replace("include.item", "item").replace("include.person", "person")
    return source


def load_site() -> dict[str, Any]:
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    data = {
        path.stem: yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in (ROOT / "_data").glob("*.yml")
    }
    config["data"] = data
    return config


def output_path(permalink: str) -> Path:
    if permalink == "/":
        return OUTPUT / "index.html"
    return OUTPUT / permalink.strip("/") / "index.html"


def main() -> int:
    site = load_site()
    baseurl = str(site.get("baseurl", "")).rstrip("/")

    templates: dict[str, str] = {}
    for directory in ("_includes", "_layouts"):
        for path in (ROOT / directory).glob("*.html"):
            _, body = split_front_matter(path.read_text(encoding="utf-8"))
            templates[path.name] = adapt_jekyll_syntax(body)

    env = Environment(loader=DictLoader(templates))

    def relative_url(value: Any) -> str:
        raw = str(value or "")
        if raw.startswith(("http://", "https://", "mailto:", "#")):
            return raw
        return f"{baseurl}/{raw.lstrip('/')}" if raw != "/" else f"{baseurl}/"

    env.add_filter("relative_url", relative_url)

    if OUTPUT.parent.exists():
        shutil.rmtree(OUTPUT.parent)
    OUTPUT.mkdir(parents=True)

    default_template = env.get_template("default.html")
    page_template = env.get_template("page.html")

    rendered_count = 0
    for filename in PAGES:
        source = (ROOT / filename).read_text(encoding="utf-8")
        page, body = split_front_matter(source)
        page["url"] = page["permalink"]

        content = env.from_string(adapt_jekyll_syntax(body)).render(site=site, page=page)
        if page.get("layout") != "default":
            content = page_template.render(site=site, page=page, content=content)
        html = default_template.render(site=site, page=page, content=content)

        destination = output_path(page["permalink"])
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(html, encoding="utf-8")
        rendered_count += 1

    for source, destination in (
        (ROOT / "assets" / "css" / "aifu.css", OUTPUT / "assets" / "css" / "aifu.css"),
        (ROOT / "assets" / "js" / "aifu.js", OUTPUT / "assets" / "js" / "aifu.js"),
        (ROOT / "images" / "photo1.jpg", OUTPUT / "images" / "photo1.jpg"),
    ):
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    print(f"OK: rendered {rendered_count} pages to {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

