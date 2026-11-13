#!/usr/bin/env python3
"""Shared language dropdown (flag + arrow) for Site.pro and Articles shells."""
from __future__ import annotations

LOCALES = ["en", "el", "fr", "de", "it", "he"]

# Flag emoji + short code shown on the closed control
LANG_META = {
    "en": {"flag": "🇬🇧", "code": "EN"},
    "el": {"flag": "🇬🇷", "code": "EL"},
    "fr": {"flag": "🇫🇷", "code": "FR"},
    "de": {"flag": "🇩🇪", "code": "DE"},
    "it": {"flag": "🇮🇹", "code": "IT"},
    "he": {"flag": "🇮🇱", "code": "HE"},
}


def lang_dropdown(lang: str, path_after: str, aria: str, lang_names: dict, *, sitepro: bool = False) -> str:
    """Compact flag switcher for top-nav right."""
    cur = LANG_META[lang]
    opts = []
    for loc in LOCALES:
        href = f"/{loc}/{path_after}" if path_after else f"/{loc}/"
        meta = LANG_META[loc]
        selected = ' aria-current="true"' if loc == lang else ""
        opts.append(
            f'<a class="svs-lang-dd__option" href="{href}" hreflang="{loc}"{selected}>'
            f'<span class="svs-lang-dd__flag" aria-hidden="true">{meta["flag"]}</span>'
            f'<span class="svs-lang-dd__name">{lang_names[loc]}</span>'
            f"</a>"
        )
    cls = "svs-lang-dd svs-lang-dd--sitepro" if sitepro else "svs-lang-dd"
    return (
        f'<details class="{cls}">'
        f'<summary class="svs-lang-dd__btn" aria-label="{aria}">'
        f'<span class="svs-lang-dd__flag" aria-hidden="true">{cur["flag"]}</span>'
        f'<span class="svs-lang-dd__code">{cur["code"]}</span>'
        f'<span class="svs-lang-dd__arrow" aria-hidden="true"></span>'
        f"</summary>"
        f'<div class="svs-lang-dd__menu" role="list">{"".join(opts)}</div>'
        f"</details>"
    )
