"""Turn a Jekyll build into a portable school-upload ZIP.

The Jekyll build uses a unique base URL marker. This script replaces that
marker with a path relative to each generated file, so the site can work below
an unknown personal-homepage URL prefix.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site-school"
ARCHIVE = ROOT / "AIFuLab-school-upload.zip"
MARKER = "/__AIFU_BASE__/"
TEXT_SUFFIXES = {".html", ".css", ".js", ".json", ".xml", ".txt"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> int:
    if not (SITE / "index.html").is_file():
        fail("_site-school/index.html is missing")

    for path in SITE.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        depth = len(path.parent.relative_to(SITE).parts)
        prefix = "../" * depth or "./"
        text = path.read_text(encoding="utf-8")
        text = text.replace(MARKER, prefix)
        text = text.replace(MARKER.rstrip("/"), prefix.rstrip("/"))
        path.write_text(text, encoding="utf-8")

    for path in SITE.rglob("*.html"):
        if "__AIFU_BASE__" in path.read_text(encoding="utf-8"):
            fail(f"base URL marker remains in {path.relative_to(SITE)}")

    if ARCHIVE.exists():
        ARCHIVE.unlink()
    with ZipFile(ARCHIVE, "w", ZIP_DEFLATED) as archive:
        for path in sorted(SITE.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(SITE))

    with ZipFile(ARCHIVE) as archive:
        if "index.html" not in archive.namelist():
            fail("ZIP root does not contain index.html")

    print(f"OK: created {ARCHIVE.name} with index.html at ZIP root")
    return 0


if __name__ == "__main__":
    sys.exit(main())
