#!/usr/bin/env python3
"""Validate the static site without adding a build dependency."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class AssetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, str]] = []
        self.form_actions: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag in {"img", "script", "iframe"} and values.get("src"):
            self.references.append((tag, values["src"] or ""))
        if tag == "link" and values.get("href"):
            self.references.append((tag, values["href"] or ""))
        if tag == "form" and values.get("action"):
            self.form_actions.append(values["action"] or "")


def is_local_reference(reference: str) -> bool:
    parsed = urlparse(reference)
    return not parsed.scheme and not reference.startswith(("#", "//"))


def main() -> None:
    html = INDEX.read_text(encoding="utf-8")
    parser = AssetParser()
    parser.feed(html)

    missing = []
    for tag, reference in parser.references:
        if not is_local_reference(reference):
            continue
        path = (ROOT / reference.split("?", 1)[0]).resolve()
        if not path.is_relative_to(ROOT) or not path.exists():
            missing.append(f"{tag}: {reference}")

    if missing:
        raise SystemExit("Missing local assets:\n" + "\n".join(missing))
    if parser.form_actions:
        raise SystemExit(f"Server-side form actions are unsupported: {parser.form_actions}")
    if "347-471-7778" in html or "3474717778" in html:
        raise SystemExit("Personal phone number found in public HTML")
    if (ROOT / "projects").exists() or (ROOT / "resume").exists():
        raise SystemExit("Private player documents must not be published")

    print(f"Validated {len(parser.references)} asset references")


if __name__ == "__main__":
    main()
