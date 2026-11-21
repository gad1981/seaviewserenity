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
# Original slideshow slides that exist locally + home section photos
HOME_CAROUSEL = [
    "/gallery_gen/9c6da47c9cdd25d963f8ee8945686e53_fit.png",
    "/gallery_gen/36e253b50e0f85dd754b90e310611360_fit.png",
    "/gallery_gen/53c40bb5e4411ffb3c88abd37c52f3b0_fit.png",
    HOME_HERO_IMG,
    HOME_WELCOME_IMG,
    HOME_VIEW_IMG,
    HOME_AMENITIES_IMG,
]

# Villa photos from original Site.pro
VILLA_HERO_IMG = "/gallery_gen/3b28058ac52b3397cb232a1976b9713c_fit.png"
VILLA_BEDROOMS_IMG = "/gallery_gen/9c6da47c9cdd25d963f8ee8945686e53_fit.png"
VILLA_BATHROOMS_IMG = "/gallery_gen/99a8d7bd813690de25cbe2bb5c3a45c3_fit.png"
VILLA_DINNER_IMG = "/gallery_gen/3b28058ac52b3397cb232a1976b9713c_fit.png"
VILLA_LIVING_IMG = "/gallery_gen/36e253b50e0f85dd754b90e310611360_fit.png"
VILLA_KITCHEN_IMG = "/gallery_gen/53c40bb5e4411ffb3c88abd37c52f3b0_fit.png"


def home_carousel_html(ui: dict) -> str:
    slides = []
    dots = []
    label = esc(ui.get("home_gallery", "Gallery"))
    for i, src in enumerate(HOME_CAROUSEL):
        eager = ' loading="eager" fetchpriority="high"' if i == 0 else ' loading="lazy"'
        hidden = "false" if i == 0 else "true"
        active = " is-active" if i == 0 else ""
        current = ' aria-current="true"' if i == 0 else ' aria-current="false"'
        slide_alt = f"{label} — {i + 1}"
        slides.append(
            f'<div class="svs-carousel__slide" aria-hidden="{hidden}">'
            f'<img src="{src}" alt="{slide_alt}"{eager} width="1448" height="1086" /></div>'
        )
        dots.append(
            f'<button type="button" class="svs-carousel__dot{active}" '
            f'data-svs-carousel-dot aria-label="{i + 1}"{current}></button>'
        )
    return f'''
    <section class="svs-shell svs-carousel svs-reveal svs-reveal--zoom" data-reveal-delay="0.15" data-svs-carousel data-interval="3000" aria-roledescription="carousel" aria-label="{label}">
      <div class="svs-carousel__viewport">
        <div class="svs-carousel__track">
          {"".join(slides)}
        </div>
      </div>
      <button type="button" class="svs-carousel__nav svs-carousel__nav--prev" data-svs-carousel-prev aria-label="Previous">‹</button>
      <button type="button" class="svs-carousel__nav svs-carousel__nav--next" data-svs-carousel-next aria-label="Next">›</button>
      <div class="svs-carousel__dots" role="group" aria-label="{label}">
        {"".join(dots)}
      </div>
    </section>'''


# Image map per article (shared media at /Articles/media/)
ARTICLE_MEDIA = {
    "seaside-accommodation-syros-delfini-beach": ("villa-bedroom-sea-view.jpg", "villa-terrace-sunset.jpg"),
    "syros-vs-santorini-mykonos-calmer-cyclades": ("syros-ermoupoli-view.jpg", "villa-terrace-sunset.jpg"),
    "best-time-to-visit-syros-seaside-holiday": ("villa-terrace-sunset.jpg", "syros-delfini-beach.jpg"),
    "greece-short-term-rentals-2026-what-travellers-want": ("villa-dining-living.jpg", "villa-kitchen.jpg"),
    "how-to-get-to-syros-from-athens-ferry-flight": ("syros-from-ferry.jpg", "syros-harbour.jpg"),
    "family-vacation-syros-seaside-house": ("syros-galissas-beach.jpg", "villa-bedroom-balcony.jpg"),
    "ermoupoli-and-beach-day-syros-itinerary": ("syros-ermoupoli-view.jpg", "syros-delfini-beach.jpg"),
    "syros-food-guide-for-villa-guests": ("loukoumi-coffee-real.jpg", "villa-kitchen.jpg"),
    "greece-vacation-rental-checklist-before-you-book": ("villa-living-fireplace.jpg", "villa-kitchen.jpg"),
    "kini-delfini-galissas-syros-beaches-guide": ("syros-delfini-beach.jpg", "syros-galissas-beach.jpg"),
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
        hero_alt = re.search(r'class="svs-figure svs-hero-figure">\s*<img[^>]*alt="([^"]*)"', html, re.S)
        hero_cap = re.search(r'class="svs-figure svs-hero-figure">.*?<figcaption>(.*?)</figcaption>', html, re.S)
        # second figure
        figs = re.findall(r'<figure class="svs-figure(?! svs-hero)[^"]*">\s*<img[^>]*alt="([^"]*)"[^>]*>\s*<figcaption>(.*?)</figcaption>', html, re.S)
        mid_alt = figs[0][0] if figs else ""
        mid_cap = figs[0][1] if figs else ""
        body = body_m.group(1) if body_m else ""
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
    book = f"/{lang}/Book-now/"
    villa = f"/{lang}/The-Villa/"
    body = (
        meta["body"]
        .replace('href="BOOK"', f'href="{book}"')
        .replace("href='BOOK'", f'href="{book}"')
        .replace('href="/en/Book-now/"', f'href="{book}"')
        .replace('href="/en/The-Villa/"', f'href="{villa}"')
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
    published = "2026-11-07"
    modified = "2026-11-21"
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
      <p class="svs-meta">{esc(ui["articles_meta_by"])} · {esc(ui["articles_meta_updated"])} 2026-11-21 · {esc(ui["articles_meta_read"])}</p>
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


def articles_index(lang: str) -> str:
    ui = UI[lang]
    cards = []
    for slug, (hero, _) in ARTICLE_MEDIA.items():
        if lang == "en":
            meta = dict(EN_META[slug])
        else:
            meta = dict(ART_I18N[slug][lang])
        meta["title"] = re.sub(r"\s*\|\s*Sea View Serenity\s*$", "", meta["title"]).strip()
        cards.append(
            f'''    <a class="svs-card" href="/{lang}/Articles/{slug}/">
      <div class="svs-card-media"><img src="/Articles/media/{hero}" alt="{esc(meta["title"])}" loading="lazy" width="640" height="400" /></div>
      <p class="svs-kicker">Guide</p>
      <h2>{esc(meta["title"])}</h2>
      <p>{esc(meta["description"])}</p>
      <span class="svs-card-link">{esc(ui["articles_read"])}</span>
    </a>'''
        )
    canonical = f"{SITE}/{lang}/Articles/"
    rtl_attr = ' dir="rtl"' if lang == "he" else ""
    fonts = "Heebo:400,600,700|Open+Sans:400,600,700" if lang == "he" else "Roboto:400,500,700|Open+Sans:400,600,700"
    switcher = lang_switcher(lang, "Articles/", ui["switcher_aria"])
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_footer import site_footer

    foot = site_footer(lang, ui)
    og_img = f"{SITE}/Articles/media/villa-terrace-sunset.jpg"
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
      <h1>{esc(ui["articles_index_h1"])}</h1>
      <p class="svs-lede">{esc(ui["articles_index_lede"])}</p>
    </div>
    <figure class="svs-figure svs-hero-figure">
  <img src="/Articles/media/villa-terrace-sunset.jpg" alt="{esc(ui.get("og_image_alt_articles") or ui["brand"])}" loading="lazy" width="1200" height="675" />
  <figcaption>{esc(ui["articles_ready_text"])}</figcaption>
</figure>
    <section class="svs-grid" aria-label="Article list">
{chr(10).join(cards)}
    </section>
    <div class="svs-callout" style="margin-bottom:2.5rem">
      <strong>{esc(ui["articles_ready_title"])}</strong>
      {esc(ui["articles_ready_text"])}
      <a class="svs-cta" href="/{lang}/Book-now/">{esc(ui["nav_book"])}</a>
    </div>
  </main>
  {foot}
  <script src="/js/site-header.js?v={js_v()}" defer></script>
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
        body = f'''
    <section class="svs-bleed-hero" aria-label="{esc(ui["brand"])}">
      <img class="svs-bleed-hero__media" src="{HOME_HERO_IMG}" alt="{esc(ui.get("og_image_alt_home") or ui["brand"])}" width="1448" height="1086" loading="eager" fetchpriority="high" />
      <div class="svs-bleed-hero__scrim" aria-hidden="true"></div>
      <div class="svs-bleed-hero__content svs-shell">
        <h1 class="svs-brand svs-reveal svs-reveal--fade" data-reveal-delay="0.2">{esc(ui["home_h1"])}</h1>
        <p class="svs-lede svs-reveal" data-reveal-delay="0.45">{esc(desc)}</p>
        <p class="svs-reveal svs-reveal--zoom" data-reveal-delay="0.7"><a class="svs-cta" href="{book}">{cta}</a></p>
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
{home_carousel_html(ui)}'''
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
        <img src="{VILLA_DINNER_IMG}" alt="{esc(ui["villa_dinner_h2"])} — {esc(ui["brand"])}" loading="lazy" width="1448" height="1086" />
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
        <a class="svs-book-contact" href="https://maps.app.goo.gl/z3p1PRkGuHZF1TBDA" target="_blank" rel="noopener">
          <span class="svs-book-contact-title">Maps</span>
          <span>{esc(ui["book_maps"])}</span>
        </a>
      </div>
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
  <script src="/js/site-header.js?v={js_v()}" defer></script>
  <script src="/js/reveal.js?v={js_v()}" defer></script>
  <script src="/js/home-carousel.js?v={js_v()}" defer></script>
  <script src="/js/lang-switcher.js?v={js_v()}" defer></script>
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
