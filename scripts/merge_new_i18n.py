#!/usr/bin/env python3
"""Merge draft i18n_*.json batches into i18n/articles.json for the 13 new articles."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = Path(__file__).resolve().parent / "_draft_articles"
ART = ROOT / "i18n" / "articles.json"

NEW = [
    "where-to-stay-syros-areas-compared",
    "seven-day-syros-itinerary-villa-base",
    "getting-around-syros-car-rental-bus",
    "kini-restaurants-sunset-dining",
    "syros-in-may-june-september",
    "things-to-do-on-syros",
    "ano-syros-ermoupoli-walking-guide",
    "day-trips-from-syros-tinos-mykonos",
    "pet-friendly-syros-villa-stay",
    "packing-meltemi-wind-guide-syros",
    "grocery-self-catering-delfini-kini",
    "winter-year-round-syros",
    "multi-gen-group-villa-syros",
]
LANGS = ("el", "fr", "de", "it", "he")
REQUIRED = (
    "title",
    "description",
    "keywords",
    "kicker",
    "hero_alt",
    "hero_caption",
    "mid_alt",
    "mid_caption",
    "body",
)


def wc(html: str) -> int:
    return len(re.sub(r"<[^>]+>", " ", html or "").split())


def load_lang(lang: str) -> dict:
    merged: dict = {}
    for path in sorted(DRAFT.glob(f"i18n_{lang}_*.json")):
        merged.update(json.loads(path.read_text(encoding="utf-8")))
    single = DRAFT / f"i18n_{lang}.json"
    if single.exists():
        merged.update(json.loads(single.read_text(encoding="utf-8")))
    remaining = DRAFT / "i18n_remaining.json"
    if remaining.exists():
        rem = json.loads(remaining.read_text(encoding="utf-8"))
        if isinstance(rem.get(lang), dict):
            merged.update(rem[lang])
    return merged


def main() -> None:
    art = json.loads(ART.read_text(encoding="utf-8"))
    report = []
    missing = []
    for lang in LANGS:
        pack = load_lang(lang)
        for slug in NEW:
            if slug not in pack:
                missing.append(f"{lang}/{slug}")
                continue
            entry = pack[slug]
            for key in REQUIRED:
                if key not in entry or not str(entry[key]).strip():
                    # mid_* may be empty
                    if key in ("mid_alt", "mid_caption"):
                        entry.setdefault(key, "")
                        continue
                    missing.append(f"{lang}/{slug}.{key}")
            if "Translation pending" in entry.get("body", ""):
                missing.append(f"{lang}/{slug}:still-pending")
            art.setdefault(slug, {})
            art[slug][lang] = {k: entry.get(k, "") for k in REQUIRED}
            report.append(f"{lang} {slug}: {wc(entry.get('body',''))} words")

    if missing:
        print("MISSING/INCOMPLETE:")
        for m in missing:
            print(" ", m)
        raise SystemExit(1)

    ART.write_text(json.dumps(art, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("merged ok")
    for line in report:
        print(line)


if __name__ == "__main__":
    main()
