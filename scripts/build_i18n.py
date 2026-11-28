#!/usr/bin/env python3
"""Build /en /el /fr /de /it /he locale trees for Sea View Serenity."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ["en", "el", "fr", "de", "it", "he"]
SITE = "https://seaviewserenity.gr"
UI = json.loads((ROOT / "i18n" / "ui.json").read_text(encoding="utf-8"))
ART_I18N = json.loads((ROOT / "i18n" / "articles.json").read_text(encoding="utf-8"))
LEGAL = json.loads((ROOT / "i18n" / "legal.json").read_text(encoding="utf-8"))
LANG_NAMES = UI["language_names"]

import sys as _sys

_sys.path.insert(0, str(Path(__file__).resolve().parent))
from seo import (  # noqa: E402
    SITE as SEO_SITE,
    breadcrumb_ld,
    lodging_ld,
    organization_ld,
    seo_head,
    webpage_ld,
    website_ld,
    og_locale as seo_og_locale,
    hreflang_links as seo_hreflang_links,
    DEFAULT_OG_IMAGE,
)

# Home photos from original Site.pro (only files present in the repo mirror)
HOME_HERO_IMG = "/gallery_gen/d9a25b075f62f8d817a4f599e5f5010c_fit.png"
HOME_WELCOME_IMG = "/gallery_gen/c0901f857a87ad3da5b8c683d0235ea7_fit.png"
HOME_VIEW_IMG = "/gallery_gen/6fa96ad5387e85756c23e25cd3d92b6f_fit.png"
HOME_AMENITIES_IMG = "/gallery_gen/27ead61515651f1d2332b229a59fe91b_fit.png"
# Full Airbnb listing gallery (labels + descriptions in i18n/carousel.json)
HOME_CAROUSEL = json.loads((ROOT / "i18n" / "carousel.json").read_text(encoding="utf-8"))

# Villa photos from original Site.pro
VILLA_HERO_IMG = "/gallery_gen/3b28058ac52b3397cb232a1976b9713c_fit.png"
VILLA_BEDROOMS_IMG = "/gallery_gen/9c6da47c9cdd25d963f8ee8945686e53_fit.png"
VILLA_BATHROOMS_IMG = "/gallery_gen/99a8d7bd813690de25cbe2bb5c3a45c3_fit.png"
VILLA_DINNER_IMG = "/Articles/media/villa-dining-living.jpg"
VILLA_LIVING_IMG = "/gallery_gen/36e253b50e0f85dd754b90e310611360_fit.png"
VILLA_KITCHEN_IMG = "/gallery_gen/53c40bb5e4411ffb3c88abd37c52f3b0_fit.png"
VILLA_WORKSPACE_IMG = "/gallery/villa/workspace-desk.jpg"


def home_carousel_html(ui: dict, lang: str = "en") -> str:
    slides = []
    dots = []
    gallery = esc(ui.get("home_gallery", "Gallery"))
    total = len(HOME_CAROUSEL)
    for i, item in enumerate(HOME_CAROUSEL):
        eager = ' loading="eager" fetchpriority="high"' if i == 0 else ' loading="lazy"'
        hidden = "false" if i == 0 else "true"
        active = " is-active" if i == 0 else ""
        current = ' aria-current="true"' if i == 0 else ' aria-current="false"'
        labels = item.get("label") or {}
        descs = item.get("description") or {}
        caption = esc(labels.get(lang) or labels.get("en") or f"{i + 1}")
        description = esc(descs.get(lang) or descs.get("en") or "")
        slide_alt = f"{caption} — {esc(ui['brand'])}"
        src = item["src"]
        desc_html = (
            f'<p class="svs-carousel__caption-desc">{description}</p>' if description else ""
        )
        slides.append(
            f'<div class="svs-carousel__slide" aria-hidden="{hidden}">'
            f'<img src="{src}" alt="{slide_alt}"{eager} width="1200" height="900" />'
            f'<div class="svs-carousel__caption">'
            f'<p class="svs-carousel__caption-label">{caption}</p>'
            f"{desc_html}"
            f"</div></div>"
        )
        dots.append(
            f'<button type="button" class="svs-carousel__dot{active}" '
            f'data-svs-carousel-dot aria-label="{caption}"{current}></button>'
        )
    # Dense galleries use the counter + arrows instead of 40+ dots.
    dots_html = (
        f'<div class="svs-carousel__dots" role="group" aria-label="{gallery}">'
        f'{"".join(dots)}</div>'
        if total <= 12
        else ""
    )
    return f'''
    <section class="svs-shell svs-carousel-section svs-reveal" data-reveal-delay="0.15" aria-labelledby="home-gallery-title">
      <h2 id="home-gallery-title" class="svs-carousel-section__title">{gallery}</h2>
      <div class="svs-carousel svs-reveal--zoom" data-svs-carousel data-interval="4500" aria-roledescription="carousel" aria-label="{gallery}">
        <div class="svs-carousel__viewport">
          <div class="svs-carousel__track">
            {"".join(slides)}
          </div>
        </div>
        <button type="button" class="svs-carousel__nav svs-carousel__nav--prev" data-svs-carousel-prev aria-label="{esc(ui.get("carousel_prev", "Previous"))}">‹</button>
        <button type="button" class="svs-carousel__nav svs-carousel__nav--next" data-svs-carousel-next aria-label="{esc(ui.get("carousel_next", "Next"))}">›</button>
        <p class="svs-carousel__count" data-svs-carousel-count aria-live="polite"><span data-svs-carousel-index>1</span> / {total}</p>
        {dots_html}
      </div>
    </section>'''


# Image map per article (shared media at /Articles/media/)
# Heroes = index thumbnails: prefer unique Syros place photos; villa only when the piece is house-led.
ARTICLE_MEDIA = {
    "where-to-stay-syros-areas-compared": ("syros-ano-ermoupoli.jpg", "syros-delfini-beach.jpg"),
    "best-time-to-visit-syros-seaside-holiday": ("syros-posidonia-coast.jpg", "syros-asteria-beach.jpg"),
    "how-to-get-to-syros-from-athens-ferry-flight": ("syros-from-ferry.jpg", "syros-ferry-port.jpg"),
    "seaside-accommodation-syros-delfini-beach": ("syros-delfini-beach.jpg", "villa-bedroom-sea-view.jpg"),
    "syros-vs-santorini-mykonos-calmer-cyclades": ("syros-ermoupoli-view.jpg", "syros-harbour.jpg"),
    "things-to-do-on-syros": ("syros-ermoupoli-pano.jpg", "syros-kini-beach.jpg"),
    "kini-delfini-galissas-syros-beaches-guide": ("syros-galissas-beach.jpg", "syros-delfini-beach.jpg"),
    "getting-around-syros-car-rental-bus": ("syros-ferry-port.jpg", "syros-harbour.jpg"),
    "seven-day-syros-itinerary-villa-base": ("syros-kini-beach.jpg", "syros-ano-syros-view.jpg"),
    "kini-restaurants-sunset-dining": ("syros-kini-sunset.jpg", "syros-kini-beach.jpg"),
    "syros-food-guide-for-villa-guests": ("loukoumi-coffee-real.jpg", "villa-kitchen.jpg"),
    "family-vacation-syros-seaside-house": ("syros-asteria-beach.jpg", "syros-galissas-beach.jpg"),
    "ermoupoli-and-beach-day-syros-itinerary": ("syros-ermoupoli-street.jpg", "syros-delfini-beach.jpg"),
    "day-trips-from-syros-tinos-mykonos": ("tinos-sunset-over-syros.jpg", "syros-from-ferry.jpg"),
    "syros-in-may-june-september": ("syros-harbour.jpg", "syros-kini-sunset.jpg"),
    "packing-meltemi-wind-guide-syros": ("syros-agathopes-beach.jpg", "syros-galissas-beach.jpg"),
    "pet-friendly-syros-villa-stay": ("syros-finikas-bay.jpg", "syros-delfini-beach.jpg"),
    "grocery-self-catering-delfini-kini": ("syros-miaouli-square.jpg", "villa-kitchen.jpg"),
    "ano-syros-ermoupoli-walking-guide": ("syros-ano-syros-view.jpg", "syros-ermoupoli-street.jpg"),
    "greece-vacation-rental-checklist-before-you-book": ("villa-bedroom-bougainvillea.jpg", "syros-from-ferry.jpg"),
    "greece-short-term-rentals-2026-what-travellers-want": ("syros-megas-gyalos.jpg", "villa-dining-living.jpg"),
    "digital-nomad-syros-delfini-remote-work": ("villa-workspace-desk.jpg", "syros-delfini-beach.jpg"),
    "winter-year-round-syros": ("villa-living-fireplace.jpg", "syros-ermoupoli-view.jpg"),
    "multi-gen-group-villa-syros": ("villa-bedroom-sea-view.jpg", "syros-galissas-beach.jpg"),
}

# Hero alt/caption aligned to ARTICLE_MEDIA (proper-noun heavy so all locales stay accurate)
ARTICLE_HERO_COPY = {
    "where-to-stay-syros-areas-compared": (
        "Ano Syros and Ermoupoli on the Syros hillside",
        "Ano Syros above Ermoupoli — two bases, one island capital. Photo: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).",
    ),
    "best-time-to-visit-syros-seaside-holiday": (
        "Coastal path and sea near Posidonia on Syros",
        "West-coast light on Syros — useful when you are choosing months, not just beaches. Photo: Kevin Stroup / Wikimedia Commons (CC BY 3.0).",
    ),
    "how-to-get-to-syros-from-athens-ferry-flight": (
        "Ermoupoli seen from the ferry approach to Syros",
        "Arriving by sea: Ermoupoli from the ferry. Photo: Zde / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "seaside-accommodation-syros-delfini-beach": (
        "Delfini Beach cove on the west coast of Syros",
        "Delfini Beach — the quiet west-coast cove that defines a seaside stay. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "syros-vs-santorini-mykonos-calmer-cyclades": (
        "View over Ermoupoli, capital of Syros",
        "Ermoupoli — a working Cycladic capital, not a postcard strip. Photo: Zacharias Mitzelos / Wikimedia Commons (CC0).",
    ),
    "things-to-do-on-syros": (
        "Wide panorama of Ermoupoli on Syros",
        "Ermoupoli panorama — town, harbour and hills in one frame. Photo: Zacharias Mitzelos / Wikimedia Commons (CC0).",
    ),
    "kini-delfini-galissas-syros-beaches-guide": (
        "Galissas beach bay on Syros",
        "Galissas — a wide, easy west-coast bay. Photo: Olavfin / Wikimedia Commons (public domain).",
    ),
    "getting-around-syros-car-rental-bus": (
        "Ferry in the port of Syros",
        "Syros port — where ferry logistics and island roads meet. Photo: Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "seven-day-syros-itinerary-villa-base": (
        "Kini beach on the west coast of Syros",
        "Kini — a natural day-two or sunset stop on a villa week. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "kini-restaurants-sunset-dining": (
        "Sunset over Kini bay on Syros",
        "Kini at sundown — tavernas face the water. Photo: ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
    ),
    "syros-food-guide-for-villa-guests": (
        "Greek coffee and loukoumi",
        "Loukoumi and coffee — Syros flavours to bring back to the house. Photo: E4024 / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "family-vacation-syros-seaside-house": (
        "Asteria beach in Ermoupoli, Syros",
        "Asteria, Ermoupoli — a town beach that works with children. Photo: Leeturtle / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "ermoupoli-and-beach-day-syros-itinerary": (
        "Street in Ermoupoli, Syros",
        "Ermoupoli streets — neoclassical town before an afternoon swim. Photo: ElioQoshi / Wikimedia Commons (CC BY 3.0).",
    ),
    "day-trips-from-syros-tinos-mykonos": (
        "Sunset over Syros seen from the port of Tinos",
        "Syros on the horizon from Tinos — the short-hop island logic. Photo: Jules Verne Times Two / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "syros-in-may-june-september": (
        "Syros harbour and waterfront",
        "Ermoupoli harbour in the shoulder months — capital life without peak crowds. Photo: Rberteig / Wikimedia Commons (CC BY 2.0).",
    ),
    "packing-meltemi-wind-guide-syros": (
        "Agathopes beach on the south coast of Syros",
        "South-coast bays like Agathopes sit more sheltered when the meltemi works the exposed shores. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "pet-friendly-syros-villa-stay": (
        "Finikas bay on Syros",
        "Finikas — a calmer bay rhythm for a low-key stay with a dog; always ask us first and check local beach rules. Photo via Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "grocery-self-catering-delfini-kini": (
        "Miaouli Square in Ermoupoli, Syros",
        "Miaouli Square — Ermoupoli’s centre for a proper restock during a west-coast villa week. Photo: Zacharias Mitzelos / Wikimedia Commons (CC0).",
    ),
    "ano-syros-ermoupoli-walking-guide": (
        "Rooftops of Ermoupoli from Ano Syros",
        "Ermoupoli from Ano Syros — the classic two-town walk. Photo: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0).",
    ),
    "greece-vacation-rental-checklist-before-you-book": (
        "Bedroom with bougainvillea at Sea View Serenity",
        "Before you book any Greek villa — light, layout and outdoor space matter as much as the listing photos.",
    ),
    "greece-short-term-rentals-2026-what-travellers-want": (
        "Megas Gyalos beach on Syros",
        "A Syros beach base still beats a generic rental grid — travellers want place, not only amenities. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "digital-nomad-syros-delfini-remote-work": (
        "Workspace desk with sea-facing light at Sea View Serenity",
        "A quiet desk near Delfini — remote weeks need shade, bandwidth and a swim after work.",
    ),
    "winter-year-round-syros": (
        "Living room fireplace at Sea View Serenity",
        "Syros in the cooler months — a real capital town outside, a warm house base inside.",
    ),
    "multi-gen-group-villa-syros": (
        "Sea-view bedroom at Sea View Serenity",
        "Room to spread out — multi-gen weeks need sleeping space and a shared table more than hotel corridors.",
    ),
}

# Topic tags for Articles index filter (search also uses title + description)
ARTICLE_TOPICS = {
    "digital-nomad-syros-delfini-remote-work": ("stay", "tips"),
    "seaside-accommodation-syros-delfini-beach": ("stay",),
    "syros-vs-santorini-mykonos-calmer-cyclades": ("plan",),
    "best-time-to-visit-syros-seaside-holiday": ("plan",),
    "greece-short-term-rentals-2026-what-travellers-want": ("tips",),
    "how-to-get-to-syros-from-athens-ferry-flight": ("plan",),
    "family-vacation-syros-seaside-house": ("stay",),
    "ermoupoli-and-beach-day-syros-itinerary": ("town", "plan"),
    "syros-food-guide-for-villa-guests": ("food",),
    "greece-vacation-rental-checklist-before-you-book": ("tips",),
    "kini-delfini-galissas-syros-beaches-guide": ("beaches",),
    "where-to-stay-syros-areas-compared": ("stay",),
    "seven-day-syros-itinerary-villa-base": ("plan",),
    "getting-around-syros-car-rental-bus": ("plan",),
    "kini-restaurants-sunset-dining": ("food",),
    "syros-in-may-june-september": ("plan",),
    "things-to-do-on-syros": ("plan",),
    "ano-syros-ermoupoli-walking-guide": ("town",),
    "day-trips-from-syros-tinos-mykonos": ("plan",),
    "pet-friendly-syros-villa-stay": ("stay",),
    "packing-meltemi-wind-guide-syros": ("beaches", "tips"),
    "grocery-self-catering-delfini-kini": ("food",),
    "winter-year-round-syros": ("plan",),
    "multi-gen-group-villa-syros": ("stay",),
}

# Canonical publish/update dates — spread across 2026 (avoid Nov 7 pile-up)
ARTICLE_DATES = {
    "where-to-stay-syros-areas-compared": ("2026-02-12", "2026-11-12"),
    "best-time-to-visit-syros-seaside-holiday": ("2026-02-26", "2026-11-21"),
    "how-to-get-to-syros-from-athens-ferry-flight": ("2026-03-12", "2026-11-21"),
    "seaside-accommodation-syros-delfini-beach": ("2026-03-26", "2026-11-21"),
    "syros-vs-santorini-mykonos-calmer-cyclades": ("2026-04-09", "2026-11-21"),
    "things-to-do-on-syros": ("2026-04-23", "2026-11-19"),
    "kini-delfini-galissas-syros-beaches-guide": ("2026-05-07", "2026-11-21"),
    "getting-around-syros-car-rental-bus": ("2026-05-21", "2026-11-15"),
    "seven-day-syros-itinerary-villa-base": ("2026-06-04", "2026-11-14"),
    "kini-restaurants-sunset-dining": ("2026-06-18", "2026-11-16"),
    "syros-food-guide-for-villa-guests": ("2026-07-02", "2026-11-21"),
    "family-vacation-syros-seaside-house": ("2026-07-16", "2026-11-21"),
    "ermoupoli-and-beach-day-syros-itinerary": ("2026-07-30", "2026-11-21"),
    "day-trips-from-syros-tinos-mykonos": ("2026-08-13", "2026-11-21"),
    "syros-in-may-june-september": ("2026-08-27", "2026-11-18"),
    "packing-meltemi-wind-guide-syros": ("2026-09-10", "2026-11-23"),
    "pet-friendly-syros-villa-stay": ("2026-09-17", "2026-11-22"),
    "grocery-self-catering-delfini-kini": ("2026-09-24", "2026-11-24"),
    "ano-syros-ermoupoli-walking-guide": ("2026-10-08", "2026-11-20"),
    "greece-vacation-rental-checklist-before-you-book": ("2026-10-15", "2026-11-21"),
    "greece-short-term-rentals-2026-what-travellers-want": ("2026-10-22", "2026-11-21"),
    "digital-nomad-syros-delfini-remote-work": ("2026-11-05", "2026-11-21"),
    "winter-year-round-syros": ("2026-11-12", "2026-11-25"),
    "multi-gen-group-villa-syros": ("2026-11-19", "2026-11-26"),
}

# English article fallbacks extracted from current EN HTML at build time
EN_SOURCES: dict[str, str] = {}
EN_META: dict[str, dict] = {}


def extract_en_articles() -> None:
    base = ROOT / "en" / "Articles"
    for slug_dir in sorted(base.iterdir()):
        if not slug_dir.is_dir():
            continue
        slug = slug_dir.name
        html = (slug_dir / "index.html").read_text(encoding="utf-8")
        title = re.search(r"<title>(.*?)</title>", html, re.S)
        desc = re.search(r'name="description" content="([^"]*)"', html)
        kw = re.search(r'name="keywords" content="([^"]*)"', html)
        body_m = re.search(r'<div class="svs-article">(.*?)<section class="svs-sources"', html, re.S)
        sources_m = re.search(r'(<section class="svs-sources".*?</section>)', html, re.S)
        hero_alt = re.search(r'class="svs-figure svs-hero-figure[^"]*"\s*>\s*<img[^>]*alt="([^"]*)"', html, re.S)
        hero_cap = re.search(r'class="svs-figure svs-hero-figure[^"]*"\s*>.*?<figcaption>(.*?)</figcaption>', html, re.S)
        # second figure
        figs = re.findall(r'<figure class="svs-figure(?! svs-hero)[^"]*">\s*<img[^>]*alt="([^"]*)"[^>]*>\s*<figcaption>(.*?)</figcaption>', html, re.S)
        mid_alt = figs[0][0] if figs else ""
        mid_cap = figs[0][1] if figs else ""
        body = body_m.group(1) if body_m else ""
        pub_default, mod_default = ARTICLE_DATES.get(slug, ("2026-06-01", "2026-11-21"))
        # Keep all inline figures — EN bodies are the photo-illustrated source of truth
        EN_META[slug] = {
            "title": re.sub(r"\s*\|\s*Sea View Serenity\s*$", "", title.group(1) if title else slug),
            "description": desc.group(1) if desc else "",
            "keywords": kw.group(1) if kw else "",
            "kicker": "Articles · Syros & seaside stays",
            "body": body.strip(),
            "hero_alt": hero_alt.group(1) if hero_alt else "",
            "hero_caption": hero_cap.group(1) if hero_cap else "",
            "mid_alt": mid_alt,
            "mid_caption": mid_cap,
            "published": pub_default,
            "modified": mod_default,
        }
        if sources_m:
            EN_SOURCES[slug] = sources_m.group(1)


def hreflang_links(path_after_locale: str) -> str:
    """path_after_locale like '' or 'Articles/' or 'The-Villa/'"""
    return seo_hreflang_links(path_after_locale)


def lang_switcher(lang: str, path_after_locale: str, aria: str) -> str:
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lang_switcher import lang_dropdown

    return lang_dropdown(lang, path_after_locale, aria, LANG_NAMES, sitepro=False)


def css_links() -> str:
    """Articles-prototype stylesheet stack for shell pages."""
    import sys
    from pathlib import Path as _P
    sys.path.insert(0, str(_P(__file__).resolve().parent))
    from site_chrome import css_head_links
    return css_head_links(articles=True)


def js_v() -> str:
    import sys
    from pathlib import Path as _P
    sys.path.insert(0, str(_P(__file__).resolve().parent))
    from site_chrome import CSS_V
    return CSS_V


def site_chrome(lang: str, ui: dict, active: str, path_after: str, switcher: str = "", nav: str = "") -> str:
    """Articles-style top nav — site-wide norm."""
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_chrome import build_chrome, site_chrome_with_switcher, nav_html as shared_nav

    if switcher and nav:
        return site_chrome_with_switcher(lang, ui, active, path_after, switcher, nav)
    return build_chrome(lang, ui, active, path_after, LANG_NAMES)


def _word_count_html(html: str) -> int:
    return len(re.sub(r"<[^>]+>", " ", html or "").split())


def article_page(lang: str, slug: str) -> str:
    ui = UI[lang]
    en_meta = dict(EN_META[slug])
    if lang == "en":
        meta = en_meta
    else:
        meta = dict(ART_I18N[slug][lang])
        # Prefer translated body when it is still substantial; otherwise use the
        # expanded English body so photos and depth are not lost mid-migration.
        if _word_count_html(meta.get("body", "")) < 700:
            meta = {
                **meta,
                "body": en_meta["body"],
                "hero_alt": meta.get("hero_alt") or en_meta.get("hero_alt", ""),
                "hero_caption": meta.get("hero_caption") or en_meta.get("hero_caption", ""),
                "mid_alt": meta.get("mid_alt") or en_meta.get("mid_alt", ""),
                "mid_caption": meta.get("mid_caption") or en_meta.get("mid_caption", ""),
            }
    # translations sometimes append brand to title — keep h1 clean
    meta["title"] = re.sub(r"\s*\|\s*Sea View Serenity\s*$", "", meta["title"]).strip()
    hero, mid = ARTICLE_MEDIA[slug]
    if slug in ARTICLE_HERO_COPY:
        meta["hero_alt"], meta["hero_caption"] = ARTICLE_HERO_COPY[slug]
    book = f"/{lang}/Book-now/"
    villa = f"/{lang}/The-Villa/"
    body = (
        meta["body"]
        .replace('href="BOOK"', f'href="{book}"')
        .replace("href='BOOK'", f'href="{book}"')
        .replace('href="/en/Book-now/"', f'href="{book}"')
        .replace('href="/en/The-Villa/"', f'href="{villa}"')
        .replace('href="/en/Articles/', f'href="/{lang}/Articles/')
    )
    # Only inject the legacy mid image when the body has no inline figures yet
    if '<figure class="svs-figure"' not in body:
        mid_fig = f'''<figure class="svs-figure">
  <img src="/Articles/media/{mid}" alt="{meta.get("mid_alt","")}" loading="lazy" width="1200" height="675" />
  <figcaption>{meta.get("mid_caption","")}</figcaption>
</figure>
'''
        if "<h2>" in body:
            m = re.search(r"<h2>.*?</h2>\s*<p>.*?</p>", body, re.S)
            if m:
                i = m.end()
                body = body[:i] + "\n" + mid_fig + body[i:]
            else:
                body = mid_fig + body
        else:
            body = mid_fig + body

    sources = EN_SOURCES.get(slug, "")
    # localize sources heading only
    sources = sources.replace("Sources &amp; citations", ui["articles_sources"]).replace(
        "Sources & citations", ui["articles_sources"]
    )

    # related links
    others = [s for s in ARTICLE_MEDIA if s != slug]
    idx = sum(ord(c) for c in slug) % len(others)
    pick = (others[idx:] + others[:idx])[:5]
    related_items = []
    for o in pick:
        if lang == "en":
            ot = EN_META[o]["title"]
        else:
            ot = ART_I18N[o][lang]["title"]
        related_items.append(f'      <li><a href="/{lang}/Articles/{o}/">{ot}</a></li>')
    related = f'<div class="svs-related"><h2>{ui["articles_more"]}</h2><ul>\n' + "\n".join(related_items) + "\n    </ul></div>"

    canonical = f"{SITE}/{lang}/Articles/{slug}/"
    title = meta["title"] + " | Sea View Serenity"
    path_after = f"Articles/{slug}/"
    rtl_attr = ' dir="rtl"' if lang == "he" else ""
    fonts = "Roboto:400,500,700|Open+Sans:400,600,700"
    if lang == "he":
        fonts = "Heebo:400,600,700|Open+Sans:400,600,700"

    hero_url = f"{SITE}/Articles/media/{hero}"
    published = en_meta.get("published") or ARTICLE_DATES.get(slug, ("2026-06-01", "2026-11-21"))[0]
    modified = en_meta.get("modified") or ARTICLE_DATES.get(slug, (published, published))[1]
    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": meta["title"],
        "description": meta["description"],
        "datePublished": published,
        "dateModified": modified,
        "inLanguage": lang,
        "author": {"@type": "Organization", "name": "Sea View Serenity hosts", "@id": f"{SITE}/#organization"},
        "publisher": organization_ld(),
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "image": [
            {
                "@type": "ImageObject",
                "url": hero_url,
                "width": 1200,
                "height": 675,
            }
        ],
        "keywords": meta.get("keywords", ""),
        "articleSection": "Travel",
        "about": {"@id": f"{SITE}/#lodging"},
    }
    crumbs = breadcrumb_ld(
        [
            (ui["nav_home"], f"{SITE}/{lang}/"),
            (ui["nav_articles"], f"{SITE}/{lang}/Articles/"),
            (meta["title"], canonical),
        ]
    )

    nav = nav_html(lang, ui, "articles")
    switcher = lang_switcher(lang, path_after, ui["switcher_aria"])
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_footer import site_footer

    foot = site_footer(lang, ui)
    head_seo = seo_head(
        lang=lang,
        title=title,
        description=meta["description"],
        canonical=canonical,
        path_after=path_after,
        og_type="article",
        og_image=hero_url,
        og_image_alt=meta.get("hero_alt") or meta["title"],
        og_image_w=1200,
        og_image_h=675,
        keywords=meta.get("keywords", ""),
        article_published=f"{published}T00:00:00+02:00",
        article_modified=f"{modified}T00:00:00+02:00",
        json_ld=[organization_ld(), article_ld, crumbs],
    )

    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl_attr}>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
{head_seo}
  <link href="https://fonts.googleapis.com/css?family={fonts}&display=swap" rel="stylesheet" />
{css_links()}
</head>
<body class="svs-articles">
  {site_chrome(lang, ui, "articles", path_after, switcher, nav)}
  <main>
    <div class="svs-shell svs-hero svs-hero--article">
      <p class="svs-kicker">{esc(meta.get("kicker") or ui["articles_kicker"])}</p>
      <h1>{esc(meta["title"])}</h1>
      <p class="svs-meta">{esc(ui["articles_meta_by"])} · {esc(ui["articles_meta_updated"])} {modified} · {esc(ui["articles_meta_read"])}</p>
    </div>
    <figure class="svs-figure svs-hero-figure svs-shell">
  <img src="/Articles/media/{hero}" alt="{esc(meta.get("hero_alt",""))}" loading="lazy" width="1200" height="675" />
  <figcaption>{meta.get("hero_caption","")}</figcaption>
</figure>
    <article class="svs-article-wrap">
      <div class="svs-article">
{body}
{sources}
{related}
      </div>
    </article>
  </main>
  {foot}
  <script src="/js/site-header.js?v={js_v()}" defer></script>
  <script src="/js/lang-switcher.js?v={js_v()}" defer></script>
</body>
</html>
'''


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def og_locale(lang: str) -> str:
    return seo_og_locale(lang)


def nav_html(lang: str, ui: dict, active: str) -> str:
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_chrome import nav_html as shared_nav

    return shared_nav(lang, ui, active)


def _topic_label(ui: dict, key: str) -> str:
    return ui.get(
        f"articles_filter_{key}",
        {
            "stay": "Stay & villa",
            "beaches": "Beaches",
            "plan": "Planning",
            "food": "Food",
            "town": "Town & culture",
            "tips": "Practical tips",
        }.get(key, key),
    )


def _format_card_date(lang: str, iso_day: str) -> str:
    """Locale-friendly short date for article cards (e.g. 20 Nov 2026)."""
    months = {
        "en": ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"),
        "el": ("Ιαν", "Φεβ", "Μαρ", "Απρ", "Μαΐ", "Ιουν", "Ιουλ", "Αυγ", "Σεπ", "Οκτ", "Νοε", "Δεκ"),
        "fr": ("janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."),
        "de": ("Jan.", "Feb.", "März", "Apr.", "Mai", "Juni", "Juli", "Aug.", "Sept.", "Okt.", "Nov.", "Dez."),
        "it": ("gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"),
        "he": ("ינו׳", "פבר׳", "מרץ", "אפר׳", "מאי", "יונ׳", "יול׳", "אוג׳", "ספט׳", "אוק׳", "נוב׳", "דצמ׳"),
    }
    try:
        y, m, d = iso_day[:10].split("-")
        mon = months.get(lang, months["en"])[int(m) - 1]
        day = str(int(d))
        if lang == "de":
            return f"{day}. {mon} {y}"
        if lang == "he":
            return f"{day} ב{mon} {y}"
        return f"{day} {mon} {y}"
    except Exception:
        return iso_day[:10]


def articles_index(lang: str) -> str:
    ui = UI[lang]
    # Newest published first — standard practice for an articles index
    ordered = sorted(
        ARTICLE_MEDIA.items(),
        key=lambda item: EN_META.get(item[0], {}).get("published", "1970-01-01"),
        reverse=True,
    )
    cards = []
    for slug, (hero, _) in ordered:
        if lang == "en":
            meta = dict(EN_META[slug])
        else:
            meta = dict(ART_I18N[slug][lang])
        meta["title"] = re.sub(r"\s*\|\s*Sea View Serenity\s*$", "", meta["title"]).strip()
        topics = ARTICLE_TOPICS.get(slug, ("plan",))
        topics_attr = " ".join(topics)
        topic_labels = [_topic_label(ui, t) for t in topics]
        published = (
            (EN_META.get(slug) or {}).get("published")
            or ARTICLE_DATES.get(slug, ("2026-06-01",))[0]
            or meta.get("published")
            or "2026-06-01"
        )
        published = published[:10]
        date_label = _format_card_date(lang, published)
        # Search index: title, description, keywords, topic ids + localized labels, date
        search_parts = [
            meta["title"],
            meta.get("description", ""),
            meta.get("keywords", ""),
            topics_attr,
            " ".join(topic_labels),
            published,
            date_label,
            slug.replace("-", " "),
        ]
        search_blob = esc(" ".join(p for p in search_parts if p))
        tags_html = "".join(
            f'<li><span class="svs-card-tag">{esc(label)}</span></li>' for label in topic_labels
        )
        cards.append(
            f'''    <a class="svs-card" href="/{lang}/Articles/{slug}/" data-svs-article-card data-topics="{topics_attr}" data-published="{published}" data-search="{search_blob}">
      <div class="svs-card-media">
        <img src="/Articles/media/{hero}" alt="{esc(meta["title"])}" loading="lazy" width="640" height="400" />
        <time class="svs-card-date" datetime="{published}">{esc(date_label)}</time>
      </div>
      <ul class="svs-card-tags" aria-label="{esc(ui.get("articles_filter_label", "Topics"))}">{tags_html}</ul>
      <h2>{esc(meta["title"])}</h2>
      <p>{esc(meta["description"])}</p>
      <span class="svs-card-link">{esc(ui["articles_read"])}</span>
    </a>'''
        )
    topic_keys = (
        ("all", ui.get("articles_filter_all", "All")),
        ("stay", ui.get("articles_filter_stay", "Stay & villa")),
        ("beaches", ui.get("articles_filter_beaches", "Beaches")),
        ("plan", ui.get("articles_filter_plan", "Planning")),
        ("food", ui.get("articles_filter_food", "Food")),
        ("town", ui.get("articles_filter_town", "Town & culture")),
        ("tips", ui.get("articles_filter_tips", "Practical tips")),
    )
    topic_btns = []
    for key, label in topic_keys:
        active = " is-active" if key == "all" else ""
        pressed = "true" if key == "all" else "false"
        topic_btns.append(
            f'<button type="button" class="svs-articles-filter__topic{active}" '
            f'data-svs-topic="{key}" aria-pressed="{pressed}">{esc(label)}</button>'
        )
    filter_bar = f'''    <div class="svs-articles-filter" data-svs-articles-filter>
      <label class="svs-articles-filter__search">
        <span class="svs-articles-filter__search-label">{esc(ui.get("articles_search_label", "Search articles"))}</span>
        <input type="search" data-svs-articles-search autocomplete="off"
          placeholder="{esc(ui.get("articles_search_placeholder", "Search by topic, beach, ferry…"))}"
          aria-label="{esc(ui.get("articles_search_label", "Search articles"))}" />
      </label>
      <div class="svs-articles-filter__topics" role="group" aria-label="{esc(ui.get("articles_filter_label", "Filter by topic"))}">
        {"".join(topic_btns)}
      </div>
      <p class="svs-articles-filter__status" data-svs-articles-status aria-live="polite"></p>
    </div>'''
    canonical = f"{SITE}/{lang}/Articles/"
    rtl_attr = ' dir="rtl"' if lang == "he" else ""
    fonts = "Heebo:400,600,700|Open+Sans:400,600,700" if lang == "he" else "Roboto:400,500,700|Open+Sans:400,600,700"
    switcher = lang_switcher(lang, "Articles/", ui["switcher_aria"])
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_footer import site_footer

    foot = site_footer(lang, ui)
    og_img = f"{SITE}/Articles/media/villa-bedroom-balcony.jpg"
    head_seo = seo_head(
        lang=lang,
        title=ui["articles_index_title"],
        description=ui["articles_index_description"],
        canonical=canonical,
        path_after="Articles/",
        og_image=og_img,
        og_image_alt=ui.get("og_image_alt_articles") or ui["articles_index_h1"],
        og_image_w=1200,
        og_image_h=675,
        keywords="Syros, Delfini Beach, Cyclades, Greece vacation rental, seaside house",
        json_ld=[
            organization_ld(),
            website_ld(lang),
            webpage_ld(
                lang=lang,
                name=ui["articles_index_title"],
                description=ui["articles_index_description"],
                url=canonical,
                page_type="CollectionPage",
            ),
            breadcrumb_ld(
                [
                    (ui["nav_home"], f"{SITE}/{lang}/"),
                    (ui["nav_articles"], canonical),
                ]
            ),
        ],
    )
    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl_attr}>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
{head_seo}
  <link href="https://fonts.googleapis.com/css?family={fonts}&display=swap" rel="stylesheet" />
{css_links()}
</head>
<body class="svs-articles">
  {site_chrome(lang, ui, "articles", "Articles/", switcher, nav_html(lang, ui, "articles"))}
  <main class="svs-shell">
    <div class="svs-hero">
      <p class="svs-kicker">{esc(ui["articles_kicker"])}</p>
      <h1>{esc(ui["articles_index_h1"]).replace(chr(10), "<br />")}</h1>
      <p class="svs-lede">{esc(ui["articles_index_lede"])}</p>
    </div>
    <figure class="svs-figure svs-hero-figure">
  <img src="/Articles/media/villa-bedroom-balcony.jpg" alt="{esc(ui.get("og_image_alt_articles") or ui["brand"])}" loading="lazy" width="1200" height="675" />
  <figcaption>{esc(ui["articles_ready_text"])}</figcaption>
</figure>
{filter_bar}
    <section class="svs-grid" data-svs-articles-grid aria-label="Article list">
{chr(10).join(cards)}
    </section>
    <p class="svs-articles-filter__empty" data-svs-articles-empty hidden>{esc(ui.get("articles_filter_empty", "No articles match that search."))}</p>
    <div class="svs-callout" style="margin-bottom:2.5rem">
      <strong>{esc(ui["articles_ready_title"])}</strong>
      {esc(ui["articles_ready_text"])}
      <a class="svs-cta" href="/{lang}/Book-now/">{esc(ui["nav_book"])}</a>
    </div>
  </main>
  {foot}
  <script src="/js/site-header.js?v={js_v()}" defer></script>
  <script src="/js/articles-filter.js?v={js_v()}" defer></script>
  <script src="/js/lang-switcher.js?v={js_v()}" defer></script>
</body>
</html>
'''


def marketing_page(lang: str, page: str) -> str:
    """Home / Villa / Book — Articles shell prototype (Home keeps full-bleed hero)."""
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_footer import site_footer

    ui = UI[lang]
    rtl_attr = ' dir="rtl"' if lang == "he" else ""
    fonts = "Heebo:400,600,700|Open+Sans:400,600,700" if lang == "he" else "Roboto:400,500,700|Open+Sans:400,600,700"
    body_class = "svs-articles"
    og_image = f"{SITE}/Articles/media/villa-terrace-sunset.jpg"

    if page == "home":
        active, path_after = "home", ""
        canonical = f"{SITE}/{lang}/"
        title, desc = ui["home_title"], ui["home_description"]
        body_class = "svs-articles svs-page-home"
        og_image = f"{SITE}{HOME_HERO_IMG}"
        book = f"/{lang}/Book-now/"
        cta = esc(ui["home_book_cta"])
        hero_lede = ui.get("home_hero_lede") or desc
        body = f'''
    <section class="svs-bleed-hero" aria-label="{esc(ui["brand"])}">
      <div class="svs-bleed-hero__stage" aria-hidden="true">
        <img class="svs-bleed-hero__media" src="{HOME_HERO_IMG}" alt="{esc(ui.get("og_image_alt_home") or ui["brand"])}" width="1448" height="1086" loading="eager" fetchpriority="high" />
      </div>
      <div class="svs-bleed-hero__scrim" aria-hidden="true"></div>
      <div class="svs-bleed-hero__glow" aria-hidden="true"></div>
      <div class="svs-bleed-hero__content svs-shell">
        <h1 class="svs-brand svs-reveal svs-reveal--fade" data-reveal-delay="0.15">{esc(ui["home_h1"])}</h1>
        <p class="svs-lede svs-reveal" data-reveal-delay="0.4">{esc(hero_lede)}</p>
        <p class="svs-reveal svs-reveal--zoom" data-reveal-delay="0.65"><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <a class="svs-bleed-hero__scroll" href="#welcome" aria-label="{esc(ui["scroll_cue"])}">
        <span class="svs-bleed-hero__scroll-mouse" aria-hidden="true"><span class="svs-bleed-hero__scroll-wheel"></span></span>
        <span>{esc(ui["scroll_cue"])}</span>
        <span class="svs-bleed-hero__scroll-line" aria-hidden="true"></span>
      </a>
    </section>
    <section class="svs-shell svs-home-block svs-reveal" data-reveal-delay="0.05" id="welcome">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["home_welcome_h2"])}</h2>
        <p>{esc(ui["home_welcome_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{HOME_WELCOME_IMG}" alt="{esc(ui["home_welcome_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1448" height="1086" />
      </figure>
    </section>
    <section class="svs-shell svs-home-block svs-home-block--flip svs-reveal" data-reveal-delay="0.08">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["home_view_h2"])}</h2>
        <p>{esc(ui["home_view_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{HOME_VIEW_IMG}" alt="{esc(ui["home_view_h2"])} — {esc(ui["brand"])}, Syros" loading="lazy" width="1448" height="1086" />
      </figure>
    </section>
    <section class="svs-shell svs-home-block svs-reveal" data-reveal-delay="0.08">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["home_amenities_h2"])}</h2>
        <p>{esc(ui["home_amenities_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{HOME_AMENITIES_IMG}" alt="{esc(ui["home_amenities_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1536" height="1024" />
      </figure>
    </section>
{home_carousel_html(ui, lang)}'''
    elif page == "villa":
        active, path_after = "villa", "The-Villa/"
        canonical = f"{SITE}/{lang}/The-Villa/"
        title, desc = ui["villa_title"], ui["villa_description"]
        og_image = f"{SITE}{VILLA_HERO_IMG}"
        book = f"/{lang}/Book-now/"
        cta = esc(ui["villa_cta"])
        body = f'''
    <div class="svs-shell svs-hero">
      <p class="svs-kicker svs-reveal svs-reveal--fade" data-reveal-delay="0.1">{esc(ui["brand"])}</p>
      <h1 class="svs-reveal svs-reveal--fade" data-reveal-delay="0.25">{esc(ui["villa_h1"])}</h1>
      <p class="svs-lede svs-reveal" data-reveal-delay="0.45">{esc(ui["villa_intro"])}</p>
      <p class="svs-reveal svs-reveal--zoom" data-reveal-delay="0.7" style="margin-top:1rem"><a class="svs-cta" href="{book}">{cta}</a></p>
    </div>
    <figure class="svs-figure svs-hero-figure svs-shell svs-reveal svs-reveal--zoom" data-reveal-delay="0.35">
      <img src="{VILLA_HERO_IMG}" alt="{esc(ui.get("og_image_alt_villa") or ui["villa_h1"])}" loading="eager" width="1448" height="1086" />
    </figure>
    <section class="svs-shell svs-home-block svs-reveal" data-reveal-delay="0.05">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["villa_bedrooms_h2"])}</h2>
        <p>{esc(ui["villa_bedrooms_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{VILLA_BEDROOMS_IMG}" alt="{esc(ui["villa_bedrooms_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1448" height="1086" />
      </figure>
    </section>
    <section class="svs-shell svs-home-block svs-home-block--flip svs-reveal" data-reveal-delay="0.08">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["villa_bathrooms_h2"])}</h2>
        <p>{esc(ui["villa_bathrooms_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{VILLA_BATHROOMS_IMG}" alt="{esc(ui["villa_bathrooms_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1448" height="1086" />
      </figure>
    </section>
    <section class="svs-shell svs-home-block svs-reveal" data-reveal-delay="0.08">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["villa_dinner_h2"])}</h2>
        <p>{esc(ui["villa_dinner_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{VILLA_DINNER_IMG}" alt="{esc(ui["villa_dinner_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1600" height="1066" />
      </figure>
    </section>
    <section class="svs-shell svs-home-block svs-home-block--flip svs-reveal" data-reveal-delay="0.08">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["villa_living_h2"])}</h2>
        <p>{esc(ui["villa_living_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{VILLA_LIVING_IMG}" alt="{esc(ui["villa_living_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1448" height="1086" />
      </figure>
    </section>
    <section class="svs-shell svs-home-block svs-reveal" data-reveal-delay="0.08">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["villa_kitchen_h2"])}</h2>
        <p>{esc(ui["villa_kitchen_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{VILLA_KITCHEN_IMG}" alt="{esc(ui["villa_kitchen_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1448" height="1086" />
      </figure>
    </section>
    <section class="svs-shell svs-home-block svs-home-block--flip svs-reveal" data-reveal-delay="0.08">
      <div class="svs-home-block__copy">
        <h2>{esc(ui["villa_workspace_h2"])}</h2>
        <p>{esc(ui["villa_workspace_p"])}</p>
        <p><a class="svs-cta" href="{book}">{cta}</a></p>
      </div>
      <figure class="svs-home-block__media">
        <img src="{VILLA_WORKSPACE_IMG}" alt="{esc(ui["villa_workspace_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1440" height="1211" />
      </figure>
    </section>'''
    else:  # book
        active, path_after = "book", "Book-now/"
        canonical = f"{SITE}/{lang}/Book-now/"
        title, desc = ui["book_title"], ui["book_description"]
        og_image = f"{SITE}/gallery_gen/813a875966b2335423d49b510d298d8c_fit.png"
        body = f'''
    <div class="svs-shell svs-hero">
      <p class="svs-kicker svs-reveal svs-reveal--fade" data-reveal-delay="0.1">{esc(ui["brand"])}</p>
      <h1 class="svs-reveal svs-reveal--fade" data-reveal-delay="0.25">{esc(ui["book_h1"])}</h1>
      <p class="svs-lede svs-reveal" data-reveal-delay="0.45">{esc(ui["book_intro"])}</p>
    </div>
    <section class="svs-shell svs-book-hero svs-reveal" data-reveal-delay="0.2" aria-label="{esc(ui["book_platforms_title"])}">
      <div class="svs-book-hero-media">
        <img src="/gallery_gen/813a875966b2335423d49b510d298d8c_fit.png" alt="{esc(ui["brand"])}" loading="eager" width="1200" height="675" />
      </div>
      <div class="svs-book-hero-panel">
        <p class="svs-kicker">{esc(ui["book_platforms_title"])}</p>
        <h2>{esc(ui["book_platforms_title"])}</h2>
        <p>{esc(ui["book_platforms_lede"])}</p>
        <div class="svs-book-platforms">
          <a class="svs-book-platform" href="https://www.booking.com/hotel/gr/sea-view-serenity.el.html" target="_blank" rel="noopener">
            <span class="svs-book-platform-logo"><img src="/gallery_gen/b695a04a5a807d8bc319519be3e32a78_608x152_80x67_765x305_crop.png" alt="Booking.com" width="180" height="48" loading="lazy" /></span>
            <span class="svs-book-platform-label">{esc(ui["book_on"])} Booking.com</span>
          </a>
          <a class="svs-book-platform" href="https://www.airbnb.com/rooms/1116489236524222235" target="_blank" rel="noopener">
            <span class="svs-book-platform-logo"><img src="/gallery_gen/981fbd136d9f99a100faff1cea3a540a_268x84_fit.png" alt="Airbnb" width="140" height="44" loading="lazy" /></span>
            <span class="svs-book-platform-label">{esc(ui["book_on"])} Airbnb</span>
          </a>
          <a class="svs-book-platform" href="https://www.vrbo.com/en-gb/p11962377" target="_blank" rel="noopener">
            <span class="svs-book-platform-logo"><img src="/gallery_gen/ee79e1c39b6e9cf0b84b093a4b3b89dd_656x226_0x112_656x464_crop.png" alt="Vrbo" width="140" height="48" loading="lazy" /></span>
            <span class="svs-book-platform-label">{esc(ui["book_on"])} Vrbo</span>
          </a>
        </div>
      </div>
    </section>
    <section class="svs-shell svs-book-direct svs-reveal" data-reveal-delay="0.1">
      <div class="svs-book-direct-copy">
        <h2>{esc(ui["book_direct_title"])}</h2>
        <p>{esc(ui["book_direct_lede"])}</p>
        <p class="svs-book-address"><strong>Delfini Beach, Ano Syros 81400, Syros, Greece</strong></p>
      </div>
      <div class="svs-book-contacts">
        <a class="svs-book-contact" href="https://api.whatsapp.com/send?phone=306937027555" target="_blank" rel="noopener">
          <span class="svs-book-contact-title">{esc(ui["book_whatsapp"])}</span>
          <span>+30 693 702 7555</span>
        </a>
        <a class="svs-book-contact" href="https://www.instagram.com/seaviewserenityatsyros/" target="_blank" rel="noopener">
          <span class="svs-book-contact-title">{esc(ui["book_instagram"])}</span>
          <span>@seaviewserenityatsyros</span>
        </a>
        <a class="svs-book-contact" href="mailto:info@seaviewserenity.gr">
          <span class="svs-book-contact-title">Email</span>
          <span>info@seaviewserenity.gr</span>
        </a>
        <a class="svs-book-contact" href="https://maps.app.goo.gl/z3p1PRkGuHZF1TBDA" target="_blank" rel="noopener">
          <span class="svs-book-contact-title">Maps</span>
          <span>{esc(ui["book_maps"])}</span>
        </a>
      </div>
    </section>
    <section class="svs-shell svs-book-form-section svs-reveal" data-reveal-delay="0.1" aria-label="{esc(ui["book_form_title"])}">
      <div class="svs-book-form-intro">
        <h2>{esc(ui["book_form_title"])}</h2>
        <p>{esc(ui["book_form_lede"])}</p>
      </div>
      <form class="svs-book-form" data-contact-form data-success="{esc(ui["book_form_success"])}" data-error="{esc(ui["book_form_error"])}" data-sending="{esc(ui["book_form_sending"])}" novalidate>
        <input type="hidden" name="lang" value="{lang}" />
        <label class="svs-book-form__hp" aria-hidden="true">Company<input type="text" name="company" tabindex="-1" autocomplete="off" /></label>
        <div class="svs-book-form__grid">
          <label class="svs-book-form__field">
            <span>{esc(ui["book_form_name"])}</span>
            <input type="text" name="name" required autocomplete="name" maxlength="120" />
          </label>
          <label class="svs-book-form__field">
            <span>{esc(ui["book_form_email"])}</span>
            <input type="email" name="email" required autocomplete="email" maxlength="254" />
          </label>
          <label class="svs-book-form__field">
            <span>{esc(ui["book_form_phone"])}</span>
            <input type="tel" name="phone" autocomplete="tel" maxlength="60" />
          </label>
          <label class="svs-book-form__field">
            <span>{esc(ui["book_form_dates"])}</span>
            <input type="text" name="dates" maxlength="120" />
          </label>
          <label class="svs-book-form__field">
            <span>{esc(ui["book_form_guests"])}</span>
            <input type="text" name="guests" maxlength="40" />
          </label>
          <label class="svs-book-form__field svs-book-form__field--full">
            <span>{esc(ui["book_form_message"])}</span>
            <textarea name="message" required rows="5" maxlength="4000"></textarea>
          </label>
        </div>
        <div class="svs-book-form__actions">
          <button class="svs-cta" type="submit">{esc(ui["book_form_submit"])}</button>
          <p class="svs-book-form__status" data-contact-status hidden></p>
        </div>
      </form>
    </section>
    <section class="svs-shell svs-book-map svs-reveal" data-reveal-delay="0.1" aria-label="{esc(ui["book_map_title"])}">
      <div class="svs-book-map-head">
        <div>
          <h2>{esc(ui["book_map_title"])}</h2>
          <p>{esc(ui["book_map_lede"])}</p>
        </div>
        <a class="svs-cta" href="https://maps.app.goo.gl/z3p1PRkGuHZF1TBDA" target="_blank" rel="noopener">{esc(ui["book_map_cta"])}</a>
      </div>
      <div class="svs-book-map-frame">
        <iframe
          title="{esc(ui["book_map_title"])} — Sea View Serenity"
          src="https://www.google.com/maps?q=Sea+View+Serenity+Villa+at+Delfini+Beach+Syros@37.4584631,24.9024781&z=15&hl={lang}&output=embed"
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"
          allowfullscreen
        ></iframe>
      </div>
      <p class="svs-book-map-note">
        <a href="https://www.google.com/maps/place/Sea+View+Serenity+Villa+at+Delfini+Beach+Syros/@37.4584631,24.9024781,17z" target="_blank" rel="noopener">{esc(ui["book_map_cta"])}</a>
        · Delfini Beach, Ano Syros 81400, Syros, Greece
      </p>
    </section>'''

    switcher = lang_switcher(lang, path_after, ui["switcher_aria"])
    page_title = title if "Sea View Serenity" in title else f"{title} | Sea View Serenity"
    foot = site_footer(lang, ui)

    if page == "home":
        og_alt = ui.get("og_image_alt_home") or title
        og_w, og_h = 1448, 1086
        crumbs = breadcrumb_ld([(ui["nav_home"], canonical)])
        ld = [
            organization_ld(),
            website_ld(lang),
            lodging_ld(lang, desc),
            webpage_ld(lang=lang, name=page_title, description=desc, url=canonical),
            crumbs,
        ]
        kw = "Syros villa, Delfini Beach, seaside house Syros, Cyclades holiday rental, Sea View Serenity"
    elif page == "villa":
        og_alt = ui.get("og_image_alt_villa") or title
        og_w, og_h = 1448, 1086
        crumbs = breadcrumb_ld(
            [(ui["nav_home"], f"{SITE}/{lang}/"), (ui["nav_villa"], canonical)]
        )
        ld = [
            organization_ld(),
            lodging_ld(lang, desc),
            webpage_ld(lang=lang, name=page_title, description=desc, url=canonical),
            crumbs,
        ]
        kw = "Syros villa rooms, Delfini Beach house, kitchen, parking, sea view bedrooms"
    else:
        og_alt = ui.get("og_image_alt_book") or title
        og_w, og_h = 1448, 1086
        crumbs = breadcrumb_ld(
            [(ui["nav_home"], f"{SITE}/{lang}/"), (ui["nav_book"], canonical)]
        )
        ld = [
            organization_ld(),
            lodging_ld(lang, desc),
            webpage_ld(lang=lang, name=page_title, description=desc, url=canonical),
            crumbs,
        ]
        kw = "book Syros villa, Delfini Beach rental, Airbnb Syros, Booking.com Syros"

    head_seo = seo_head(
        lang=lang,
        title=page_title,
        description=desc,
        canonical=canonical,
        path_after=path_after,
        og_image=og_image,
        og_image_alt=og_alt,
        og_image_w=og_w,
        og_image_h=og_h,
        keywords=kw,
        json_ld=ld,
    )
    v = js_v()
    home_hero_script = (
        f'  <script src="/js/home-hero.js?v={v}" defer></script>\n' if page == "home" else ""
    )
    contact_script = (
        f'  <script src="/js/contact-form.js?v={v}" defer></script>\n' if page == "book" else ""
    )
    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl_attr}>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
{head_seo}
  <link href="https://fonts.googleapis.com/css?family={fonts}&display=swap" rel="stylesheet" />
{css_links()}
</head>
<body class="{body_class}">
  {site_chrome(lang, ui, active, path_after, switcher, nav_html(lang, ui, active))}
  <main>
{body}
  </main>
  {foot}
  <script src="/js/site-header.js?v={v}" defer></script>
  <script src="/js/reveal.js?v={v}" defer></script>
  <script src="/js/home-carousel.js?v={v}" defer></script>
{home_hero_script}{contact_script}  <script src="/js/lang-switcher.js?v={v}" defer></script>
</body>
</html>
'''


def legal_page(lang: str, kind: str) -> str:
    """kind: 'terms' | 'cookies'"""
    ui = UI[lang]
    L = LEGAL[lang]
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_footer import site_footer

    if kind == "terms":
        path_after = "Terms/"
        title, desc, h1, updated, body = (
            L["terms_title"],
            L["terms_description"],
            L["terms_h1"],
            L["terms_updated"],
            L["terms_body"],
        )
        active = "home"
    else:
        path_after = "Cookies/"
        title, desc, h1, updated, body = (
            L["cookies_title"],
            L["cookies_description"],
            L["cookies_h1"],
            L["cookies_updated"],
            L["cookies_body"],
        )
        active = "home"

    sections = "\n".join(
        f"      <h2>{esc(block['h2'])}</h2>\n      <p>{esc(block['p'])}</p>" for block in body
    )
    canonical = f"{SITE}/{lang}/{path_after}"
    rtl_attr = ' dir="rtl"' if lang == "he" else ""
    fonts = (
        "Heebo:400,600,700|Open+Sans:400,600,700"
        if lang == "he"
        else "Roboto:400,500,700|Open+Sans:400,600,700"
    )
    switcher = lang_switcher(lang, path_after, ui["switcher_aria"])
    foot = site_footer(lang, ui)
    other = "Cookies" if kind == "terms" else "Terms"
    other_label = L["cookies_nav"] if kind == "terms" else L["terms_nav"]
    page_title = title if "Sea View Serenity" in title else f"{title} | Sea View Serenity"
    head_seo = seo_head(
        lang=lang,
        title=page_title,
        description=desc,
        canonical=canonical,
        path_after=path_after,
        og_image=DEFAULT_OG_IMAGE,
        og_image_alt=ui.get("og_image_alt_home") or ui["brand"],
        robots="index, follow",
        json_ld=[
            organization_ld(),
            webpage_ld(lang=lang, name=page_title, description=desc, url=canonical),
            breadcrumb_ld(
                [
                    (ui["nav_home"], f"{SITE}/{lang}/"),
                    (h1, canonical),
                ]
            ),
        ],
    )
    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl_attr}>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
{head_seo}
  <link href="https://fonts.googleapis.com/css?family={fonts}&display=swap" rel="stylesheet" />
{css_links()}
</head>
<body class="svs-articles">
  {site_chrome(lang, ui, active, path_after, switcher, nav_html(lang, ui, active))}
  <main class="svs-shell">
    <div class="svs-hero svs-hero--article">
      <p class="svs-kicker">{esc(L["legal_heading"])}</p>
      <h1>{esc(h1)}</h1>
      <p class="svs-meta">{esc(updated)}</p>
    </div>
    <article class="svs-article-wrap">
      <div class="svs-article">
{sections}
        <p class="svs-meta" style="margin-top:2rem"><a href="/{lang}/{other}/">{esc(other_label)}</a></p>
      </div>
    </article>
  </main>
  {foot}
  <script src="/js/site-header.js?v={js_v()}" defer></script>
  <script src="/js/lang-switcher.js?v={js_v()}" defer></script>
</body>
</html>
'''


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_sitemap() -> None:
    """Multilingual sitemap with xhtml:link hreflang annotations."""
    lastmod = "2026-11-21"
    paths = [
        ("", "1.0", "weekly"),
        ("The-Villa/", "0.9", "weekly"),
        ("Book-now/", "0.95", "weekly"),
        ("Articles/", "0.85", "weekly"),
        ("Terms/", "0.3", "yearly"),
        ("Cookies/", "0.3", "yearly"),
    ]
    for slug in ARTICLE_MEDIA:
        paths.append((f"Articles/{slug}/", "0.75", "monthly"))

    def loc_for(lang: str, path: str) -> str:
        return f"{SITE}/{lang}/" if path == "" else f"{SITE}/{lang}/{path}"

    def xhtml_links(path: str) -> str:
        lines = []
        for loc in LOCALES:
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="{loc}" href="{loc_for(loc, path)}" />'
            )
        lines.append(
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{loc_for("en", path)}" />'
        )
        return "\n".join(lines)

    urls = []
    for path, priority, freq in paths:
        for lang in LOCALES:
            urls.append(
                "  <url>\n"
                f"    <loc>{loc_for(lang, path)}</loc>\n"
                f"    <lastmod>{lastmod}</lastmod>\n"
                f"    <changefreq>{freq}</changefreq>\n"
                f"    <priority>{priority}</priority>\n"
                f"{xhtml_links(path)}\n"
                "  </url>"
            )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")


def build_vercel() -> None:
    redirects = [
        {"source": "/", "destination": "/en/", "permanent": False},
        {"source": "/The-Villa", "destination": "/en/The-Villa/", "permanent": True},
        {"source": "/The-Villa/", "destination": "/en/The-Villa/", "permanent": True},
        {"source": "/Book-now", "destination": "/en/Book-now/", "permanent": True},
        {"source": "/Book-now/", "destination": "/en/Book-now/", "permanent": True},
        {"source": "/book-now", "destination": "/en/Book-now/", "permanent": True},
        {"source": "/book-now/", "destination": "/en/Book-now/", "permanent": True},
        {"source": "/Articles", "destination": "/en/Articles/", "permanent": True},
        {"source": "/Articles/", "destination": "/en/Articles/", "permanent": True},
        {"source": "/Terms", "destination": "/en/Terms/", "permanent": True},
        {"source": "/Terms/", "destination": "/en/Terms/", "permanent": True},
        {"source": "/Cookies", "destination": "/en/Cookies/", "permanent": True},
        {"source": "/Cookies/", "destination": "/en/Cookies/", "permanent": True},
    ]
    for slug in ARTICLE_MEDIA:
        redirects.append(
            {
                "source": f"/Articles/{slug}",
                "destination": f"/en/Articles/{slug}/",
                "permanent": True,
            }
        )
        redirects.append(
            {
                "source": f"/Articles/{slug}/",
                "destination": f"/en/Articles/{slug}/",
                "permanent": True,
            }
        )
    cfg = {
        "cleanUrls": True,
        "trailingSlash": True,
        "redirects": redirects,
        "headers": [
            {
                "source": "/gallery/(.*)",
                "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}],
            },
            {
                "source": "/gallery_gen/(.*)",
                "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}],
            },
            {
                "source": "/Articles/media/(.*)",
                "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}],
            },
            {
                "source": "/(.*)",
                "headers": [
                    {"key": "X-Content-Type-Options", "value": "nosniff"},
                    {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                    {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
                ],
            },
        ],
    }
    (ROOT / "vercel.json").write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    extract_en_articles()

    for lang in LOCALES:
        write(ROOT / lang / "index.html", marketing_page(lang, "home"))
        write(ROOT / lang / "The-Villa" / "index.html", marketing_page(lang, "villa"))
        write(ROOT / lang / "Book-now" / "index.html", marketing_page(lang, "book"))
        write(ROOT / lang / "Articles" / "index.html", articles_index(lang))
        for slug in ARTICLE_MEDIA:
            write(ROOT / lang / "Articles" / slug / "index.html", article_page(lang, slug))
        write(ROOT / lang / "Terms" / "index.html", legal_page(lang, "terms"))
        write(ROOT / lang / "Cookies" / "index.html", legal_page(lang, "cookies"))
        print("built", lang)

    # Root index redirect fallback for static hosts without vercel
    write(
        ROOT / "index.html",
        """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Sea View Serenity | Seaside House near Delfini Beach, Syros</title>
  <meta name="description" content="Sea View Serenity — seaside house on Syros, a 10-minute walk from Delfini Beach. Choose your language to continue." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://seaviewserenity.gr/en/" />
  <link rel="alternate" hreflang="en" href="https://seaviewserenity.gr/en/" />
  <link rel="alternate" hreflang="el" href="https://seaviewserenity.gr/el/" />
  <link rel="alternate" hreflang="fr" href="https://seaviewserenity.gr/fr/" />
  <link rel="alternate" hreflang="de" href="https://seaviewserenity.gr/de/" />
  <link rel="alternate" hreflang="it" href="https://seaviewserenity.gr/it/" />
  <link rel="alternate" hreflang="he" href="https://seaviewserenity.gr/he/" />
  <link rel="alternate" hreflang="x-default" href="https://seaviewserenity.gr/en/" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <meta http-equiv="refresh" content="0; url=/en/" />
  <script>location.replace('/en/' + location.search + location.hash);</script>
</head>
<body>
  <h1>Sea View Serenity</h1>
  <p>Seaside house near Delfini Beach, Syros.</p>
  <ul>
    <li><a href="/en/" hreflang="en">English</a></li>
    <li><a href="/el/" hreflang="el">Ελληνικά</a></li>
    <li><a href="/fr/" hreflang="fr">Français</a></li>
    <li><a href="/de/" hreflang="de">Deutsch</a></li>
    <li><a href="/it/" hreflang="it">Italiano</a></li>
    <li><a href="/he/" hreflang="he">עברית</a></li>
  </ul>
</body>
</html>
""",
    )

    build_sitemap()
    build_vercel()
    print("sitemap + vercel updated")


if __name__ == "__main__":
    main()
