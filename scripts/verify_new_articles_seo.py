#!/usr/bin/env python3
"""Verify SEO + language fluency markers for the 13 new articles across locales."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
LANGS = ("en", "el", "fr", "de", "it", "he")
LOCALES = {
    "en": "en_GB",
    "el": "el_GR",
    "fr": "fr_FR",
    "de": "de_DE",
    "it": "it_IT",
    "he": "he_IL",
}
# Rough English fingerprint — if a non-EN page body is mostly these, it's not translated
EN_MARKERS = (
    "Choosing where to stay",
    "A week on Syros works best",
    "Syros looks small on a map",
    "Kini is where many Syros evenings",
    "Peak August on any Cycladic",
    "Syros is not an island you",
    "Ermoupoli and Ano Syros are the same skyline",
    "One reason travellers underestimate Syros",
    "Travelling with a dog on a Greek island",
    "The meltemi is the summer northerly",
    "A west-coast villa week gets better",
    "Most Cycladic islands thin out",
    "Group trips fail on islands",
)


def main() -> int:
    errors = []
    warns = []
    for lang in LANGS:
        for slug in NEW:
            path = ROOT / lang / "Articles" / slug / "index.html"
            if not path.exists():
                errors.append(f"missing {path}")
                continue
            html = path.read_text(encoding="utf-8")
            title = re.search(r"<title>(.*?)</title>", html, re.S)
            desc = re.search(r'name="description" content="([^"]*)"', html)
            og_title = re.search(r'property="og:title" content="([^"]*)"', html)
            og_desc = re.search(r'property="og:description" content="([^"]*)"', html)
            og_img = re.search(r'property="og:image" content="([^"]*)"', html)
            og_loc = re.search(r'property="og:locale" content="([^"]*)"', html)
            tw = re.search(r'name="twitter:card" content="([^"]*)"', html)
            canon = re.search(r'rel="canonical" href="([^"]*)"', html)
            hreflang = re.findall(r'rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html)
            body_m = re.search(
                r'<div class="svs-article">(.*?)<section class="svs-sources"', html, re.S
            )
            body = body_m.group(1) if body_m else ""
            wc = len(re.sub(r"<[^>]+>", " ", body).split())

            if not title or "Sea View Serenity" not in title.group(1):
                errors.append(f"{lang}/{slug}: bad title")
            if not desc or len(desc.group(1)) < 50:
                errors.append(f"{lang}/{slug}: weak description")
            if not og_title or not og_img:
                errors.append(f"{lang}/{slug}: missing og title/image")
            if og_loc and og_loc.group(1) != LOCALES[lang]:
                errors.append(f"{lang}/{slug}: og:locale {og_loc.group(1)}")
            if tw and tw.group(1) != "summary_large_image":
                warns.append(f"{lang}/{slug}: twitter card {tw.group(1)}")
            if not canon or f"/{lang}/Articles/{slug}/" not in canon.group(1):
                errors.append(f"{lang}/{slug}: canonical")
            langs_present = {h for h, _ in hreflang}
            if not {"en", "el", "fr", "de", "it", "he", "x-default"} <= langs_present:
                errors.append(f"{lang}/{slug}: incomplete hreflang {langs_present}")
            if wc < 500:
                warns.append(f"{lang}/{slug}: short body ({wc})")
            if lang != "en":
                # title/desc should not be identical English stubs for key phrases
                if title and title.group(1).startswith("Where to Stay on Syros:"):
                    errors.append(f"{lang}/{slug}: EN title still present")
                if any(m in body for m in EN_MARKERS):
                    errors.append(f"{lang}/{slug}: EN body fingerprint still present")
                if 'lang="' in html[:200] and f'lang="{lang}"' not in html[:120]:
                    errors.append(f"{lang}/{slug}: html lang attr")

            # sharing image should be absolute https
            if og_img and not og_img.group(1).startswith("https://seaviewserenity.gr/Articles/media/"):
                errors.append(f"{lang}/{slug}: og:image path {og_img.group(1)}")

            print(f"ok-check {lang}/{slug} wc={wc} desc_len={len(desc.group(1)) if desc else 0}")

    print("---")
    if warns:
        print("WARNINGS:")
        for w in warns:
            print(" ", w)
    if errors:
        print("ERRORS:")
        for e in errors:
            print(" ", e)
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
