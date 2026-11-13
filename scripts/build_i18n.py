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
        # strip embedded mid figure from body for rebuild
        body = re.sub(r'<figure class="svs-figure".*?</figure>\s*', "", body, count=1, flags=re.S)
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
    lines = []
    for loc in LOCALES:
        href = f"{SITE}/{loc}/{path_after_locale}".rstrip("/") + "/"
        if path_after_locale == "":
            href = f"{SITE}/{loc}/"
        lines.append(f'  <link rel="alternate" hreflang="{loc}" href="{href}" />')
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{SITE}/en/{path_after_locale.lstrip("/")}" />')
    return "\n".join(lines)


def lang_switcher(lang: str, path_after_locale: str, aria: str) -> str:
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lang_switcher import lang_dropdown

    return lang_dropdown(lang, path_after_locale, aria, LANG_NAMES, sitepro=False)


def site_chrome(lang: str, ui: dict, active: str, path_after: str, switcher: str, nav: str) -> str:
    """Brand + primary nav + language dropdown on the right."""
    return f'''  <header class="svs-shell svs-shell-header">
    <a class="svs-shell-brand" href="/{lang}/">
      <img src="/gallery/Picture 1.png" alt="{esc(ui["brand"])}" />
      <span>{esc(ui["brand"])}</span>
    </a>
    <div class="svs-shell-header-right">
      <nav class="svs-shell-nav" aria-label="Primary">
        {nav}
      </nav>
      {switcher}
    </div>
  </header>'''


def article_page(lang: str, slug: str) -> str:
    ui = UI[lang]
    if lang == "en":
        meta = dict(EN_META[slug])
    else:
        meta = dict(ART_I18N[slug][lang])
    # translations sometimes append brand to title — keep h1 clean
    meta["title"] = re.sub(r"\s*\|\s*Sea View Serenity\s*$", "", meta["title"]).strip()
    hero, mid = ARTICLE_MEDIA[slug]
    book = f"/{lang}/Book-now/"
    body = meta["body"].replace('href="BOOK"', f'href="{book}"').replace("href='BOOK'", f'href="{book}"')
    # insert mid figure after first h2 block end / first section
    mid_fig = f'''<figure class="svs-figure">
  <img src="/Articles/media/{mid}" alt="{meta.get("mid_alt","")}" loading="lazy" width="1200" height="675" />
  <figcaption>{meta.get("mid_caption","")}</figcaption>
</figure>
'''
    if "<h2>" in body:
        # after first closing </p> following first h2
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

    json_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": meta["title"],
        "description": meta["description"],
        "datePublished": "2026-11-07",
        "dateModified": "2026-11-07",
        "inLanguage": lang,
        "author": {"@type": "Organization", "name": "Sea View Serenity hosts"},
        "publisher": {
            "@type": "Organization",
            "name": "Sea View Serenity",
            "logo": {"@type": "ImageObject", "url": f"{SITE}/gallery/favicons/favicon.png"},
        },
        "mainEntityOfPage": canonical,
        "image": [f"{SITE}/Articles/media/{hero}"],
        "keywords": meta.get("keywords", ""),
    }

    nav = nav_html(lang, ui, "articles")
    switcher = lang_switcher(lang, path_after, ui["switcher_aria"])
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_footer import site_footer

    foot = site_footer(lang, ui)

    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl_attr}>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{esc(meta["description"])}" />
  <meta name="keywords" content="{esc(meta.get("keywords",""))}" />
  <link rel="canonical" href="{canonical}" />
{hreflang_links(path_after)}
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(meta["description"])}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:locale" content="{og_locale(lang)}" />
  <meta property="og:image" content="{SITE}/Articles/media/{hero}" />
  <link rel="icon" type="image/png" href="/gallery/favicons/favicon.png" />
  <link href="https://fonts.googleapis.com/css?family={fonts}&display=swap" rel="stylesheet" />
  <link href="/css/articles.css" rel="stylesheet" />
  <link href="/css/i18n.css" rel="stylesheet" />
  <link href="/css/footer.css" rel="stylesheet" />
  <script type="application/ld+json">
{json.dumps(json_ld, ensure_ascii=False, indent=2)}
  </script>
</head>
<body class="svs-articles">
  {site_chrome(lang, ui, "articles", path_after, switcher, nav)}
  <main>
    <div class="svs-shell svs-hero svs-hero--article">
      <p class="svs-kicker">{esc(meta.get("kicker") or ui["articles_kicker"])}</p>
      <h1>{esc(meta["title"])}</h1>
      <p class="svs-meta">{esc(ui["articles_meta_by"])} · {esc(ui["articles_meta_updated"])} 2026-11-07 · {esc(ui["articles_meta_read"])}</p>
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
  <script src="/js/lang-switcher.js" defer></script>
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
    return {"en": "en_GB", "el": "el_GR", "fr": "fr_FR", "de": "de_DE", "it": "it_IT", "he": "he_IL"}[lang]


def nav_html(lang: str, ui: dict, active: str) -> str:
    items = [
        ("home", f"/{lang}/", ui["nav_home"]),
        ("villa", f"/{lang}/The-Villa/", ui["nav_villa"]),
        ("articles", f"/{lang}/Articles/", ui["nav_articles"]),
        ("book", f"/{lang}/Book-now/", ui["nav_book"]),
    ]
    out = []
    for key, href, label in items:
        cur = ' aria-current="page"' if key == active else ""
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return "\n      ".join(out)


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
      <div class="svs-card-media"><img src="/Articles/media/{hero}" alt="" loading="lazy" width="640" height="400" /></div>
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
    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl_attr}>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(ui["articles_index_title"])}</title>
  <meta name="description" content="{esc(ui["articles_index_description"])}" />
  <link rel="canonical" href="{canonical}" />
{hreflang_links("Articles/")}
  <meta property="og:title" content="{esc(ui["articles_index_title"])}" />
  <meta property="og:description" content="{esc(ui["articles_index_description"])}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:locale" content="{og_locale(lang)}" />
  <meta property="og:image" content="{SITE}/Articles/media/villa-terrace-sunset.jpg" />
  <link rel="icon" type="image/png" href="/gallery/favicons/favicon.png" />
  <link href="https://fonts.googleapis.com/css?family={fonts}&display=swap" rel="stylesheet" />
  <link href="/css/articles.css" rel="stylesheet" />
  <link href="/css/i18n.css" rel="stylesheet" />
  <link href="/css/footer.css" rel="stylesheet" />
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
  <img src="/Articles/media/villa-terrace-sunset.jpg" alt="{esc(ui["brand"])}" loading="lazy" width="1200" height="675" />
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
  <script src="/js/lang-switcher.js" defer></script>
</body>
</html>
'''


def marketing_page(lang: str, page: str) -> str:
    """Clean i18n marketing pages (Home / Villa / Book) using articles shell."""
    ui = UI[lang]
    rtl_attr = ' dir="rtl"' if lang == "he" else ""
    fonts = "Heebo:400,600,700|Open+Sans:400,600,700" if lang == "he" else "Roboto:400,500,700|Open+Sans:400,600,700"

    if page == "home":
        active, path_after = "home", ""
        canonical = f"{SITE}/{lang}/"
        title, desc = ui["home_title"], ui["home_description"]
        h1 = ui["home_h1"]
        body = f'''
    <div class="svs-shell svs-hero">
      <p class="svs-kicker">{esc(ui["brand"])}</p>
      <h1>{esc(h1)}</h1>
      <p class="svs-lede">{esc(desc)}</p>
      <p style="margin-top:1rem"><a class="svs-cta" href="/{lang}/Book-now/">{esc(ui["home_book_cta"])}</a></p>
    </div>
    <figure class="svs-figure svs-hero-figure svs-shell">
      <img src="/Articles/media/villa-terrace-sunset.jpg" alt="{esc(ui["brand"])}" loading="lazy" width="1200" height="675" />
    </figure>
    <article class="svs-article-wrap"><div class="svs-article">
      <h2>{esc(ui["home_welcome_h2"])}</h2>
      <p>{esc(ui["home_welcome_p"])}</p>
      <figure class="svs-figure">
        <img src="/Articles/media/villa-bedroom-sea-view.jpg" alt="" loading="lazy" width="1200" height="675" />
      </figure>
      <h2>{esc(ui["home_view_h2"])}</h2>
      <p>{esc(ui["home_view_p"])}</p>
      <h2>{esc(ui["home_amenities_h2"])}</h2>
      <p>{esc(ui["home_amenities_p"])}</p>
      <div class="svs-callout">
        <strong>{esc(ui["brand"])}</strong>
        {esc(ui["articles_ready_text"])}
        <a class="svs-cta" href="/{lang}/Book-now/">{esc(ui["home_book_cta"])}</a>
        <a class="svs-cta" href="/{lang}/The-Villa/" style="margin-inline-start:0.5rem;background:#13161a">{esc(ui["nav_villa"])}</a>
      </div>
    </div></article>'''
    elif page == "villa":
        active, path_after = "villa", "The-Villa/"
        canonical = f"{SITE}/{lang}/The-Villa/"
        title, desc = ui["villa_title"], ui["villa_description"]
        body = f'''
    <div class="svs-shell svs-hero">
      <p class="svs-kicker">{esc(ui["brand"])}</p>
      <h1>{esc(ui["villa_h1"])}</h1>
      <p class="svs-lede">{esc(ui["villa_intro"])}</p>
      <p style="margin-top:1rem"><a class="svs-cta" href="/{lang}/Book-now/">{esc(ui["villa_cta"])}</a></p>
    </div>
    <figure class="svs-figure svs-hero-figure svs-shell">
      <img src="/Articles/media/villa-dining-living.jpg" alt="" loading="lazy" width="1200" height="675" />
    </figure>
    <article class="svs-article-wrap"><div class="svs-article">
      <p>{esc(ui["villa_description"])}</p>
      <figure class="svs-figure">
        <img src="/Articles/media/villa-kitchen.jpg" alt="" loading="lazy" width="1200" height="675" />
      </figure>
      <figure class="svs-figure">
        <img src="/Articles/media/villa-bedroom-balcony.jpg" alt="" loading="lazy" width="1200" height="675" />
      </figure>
      <div class="svs-callout">
        <strong>{esc(ui["villa_cta"])}</strong>
        {esc(ui["articles_ready_text"])}
        <a class="svs-cta" href="/{lang}/Book-now/">{esc(ui["villa_cta"])}</a>
      </div>
    </div></article>'''
    else:  # book
        active, path_after = "book", "Book-now/"
        canonical = f"{SITE}/{lang}/Book-now/"
        title, desc = ui["book_title"], ui["book_description"]
        body = f'''
    <div class="svs-shell svs-hero">
      <p class="svs-kicker">{esc(ui["brand"])}</p>
      <h1>{esc(ui["book_h1"])}</h1>
      <p class="svs-lede">{esc(ui["book_intro"])}</p>
    </div>
    <section class="svs-shell svs-book-hero" aria-label="{esc(ui["book_platforms_title"])}">
      <div class="svs-book-hero-media">
        <img src="/Articles/media/villa-terrace-sunset.jpg" alt="{esc(ui["brand"])}" loading="eager" width="1200" height="675" />
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
    <section class="svs-shell svs-book-direct">
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
    <section class="svs-shell svs-book-map" aria-label="{esc(ui["book_map_title"])}">
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
    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl_attr}>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title) if "Sea View Serenity" in title else esc(title) + " | Sea View Serenity"}</title>
  <meta name="description" content="{esc(desc)}" />
  <link rel="canonical" href="{canonical}" />
{hreflang_links(path_after)}
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:locale" content="{og_locale(lang)}" />
  <meta property="og:image" content="{SITE}/Articles/media/villa-terrace-sunset.jpg" />
  <link rel="icon" type="image/png" href="/gallery/favicons/favicon.png" />
  <link href="https://fonts.googleapis.com/css?family={fonts}&display=swap" rel="stylesheet" />
  <link href="/css/articles.css" rel="stylesheet" />
  <link href="/css/i18n.css" rel="stylesheet" />
</head>
<body class="svs-articles">
  {site_chrome(lang, ui, active, path_after, switcher, nav_html(lang, ui, active))}
  <main>
{body}
  </main>
  <footer class="svs-shell svs-shell-footer">
    <p>{ui["footer_copy"].replace("seaviewserenity.gr", '<a href="/' + lang + '/">seaviewserenity.gr</a>')}</p>
    <p>{ui["footer_designed"].replace("georgegad.com", '<a href="https://georgegad.com" target="_blank" rel="noopener">georgegad.com</a>')}</p>
  </footer>
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
    return f'''<!DOCTYPE html>
<html lang="{lang}"{rtl_attr}>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}" />
  <link rel="canonical" href="{canonical}" />
{hreflang_links(path_after)}
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:locale" content="{og_locale(lang)}" />
  <link rel="icon" type="image/png" href="/gallery/favicons/favicon.png" />
  <link href="https://fonts.googleapis.com/css?family={fonts}&display=swap" rel="stylesheet" />
  <link href="/css/articles.css" rel="stylesheet" />
  <link href="/css/i18n.css" rel="stylesheet" />
  <link href="/css/footer.css" rel="stylesheet" />
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
  <script src="/js/lang-switcher.js" defer></script>
</body>
</html>
'''


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_sitemap() -> None:
    urls = []
    for lang in LOCALES:
        for path in ["", "The-Villa/", "Book-now/", "Articles/", "Terms/", "Cookies/"]:
            loc = f"{SITE}/{lang}/{path}" if path else f"{SITE}/{lang}/"
            urls.append(f"  <url><loc>{loc}</loc><changefreq>weekly</changefreq></url>")
        for slug in ARTICLE_MEDIA:
            urls.append(
                f"  <url><loc>{SITE}/{lang}/Articles/{slug}/</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>"
            )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
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
        ],
    }
    (ROOT / "vercel.json").write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    extract_en_articles()
    # Home / Villa / Book: restore original Site.pro layouts (hero, gallery, absolute CSS)
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from restore_sitepro import write_pages as write_sitepro_pages

    write_sitepro_pages()

    for lang in LOCALES:
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
  <meta http-equiv="refresh" content="0; url=/en/" />
  <link rel="canonical" href="https://seaviewserenity.gr/en/" />
  <title>Sea View Serenity</title>
  <script>location.replace('/en/' + location.search + location.hash);</script>
</head>
<body>
  <p><a href="/en/">Sea View Serenity — continue in English</a></p>
</body>
</html>
""",
    )

    build_sitemap()
    build_vercel()
    print("sitemap + vercel updated")


if __name__ == "__main__":
    main()
