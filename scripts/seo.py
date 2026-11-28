#!/usr/bin/env python3
"""Shared multilingual SEO head tags, geo data, and JSON-LD helpers."""
from __future__ import annotations

import json
from typing import Any

SITE = "https://seaviewserenity.gr"
BRAND = "Sea View Serenity"

# Villa pin — Delfini Beach, Ano Syros
GEO_LAT = 37.4584631
GEO_LNG = 24.9024781
GEO_REGION = "GR-L"
GEO_PLACENAME = "Delfini Beach, Ano Syros, Syros, Cyclades, Greece"
GEO_ADDRESS = {
    "@type": "PostalAddress",
    "streetAddress": "Delfini Beach",
    "addressLocality": "Ano Syros",
    "postalCode": "81400",
    "addressRegion": "Cyclades",
    "addressCountry": "GR",
}
GEO_MAPS = "https://maps.app.goo.gl/z3p1PRkGuHZF1TBDA"
PHONE = "+306937027555"
OG_LOCALE = {
    "en": "en_GB",
    "el": "el_GR",
    "fr": "fr_FR",
    "de": "de_DE",
    "it": "it_IT",
    "he": "he_IL",
}

LOCALES = ["en", "el", "fr", "de", "it", "he"]

DEFAULT_OG_IMAGE = f"{SITE}/gallery_gen/d9a25b075f62f8d817a4f599e5f5010c_fit.png"
DEFAULT_OG_IMAGE_W = 1448
DEFAULT_OG_IMAGE_H = 1086
LOGO_URL = f"{SITE}/gallery/Picture%201.png"
FAVICON_PNG = "/gallery/favicons/favicon-32x32.png"
APPLE_TOUCH = "/gallery/favicons/apple-touch-icon.png"
MANIFEST = "/site.webmanifest"


def esc(s: str) -> str:
    return (
        (s or "")
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def og_locale(lang: str) -> str:
    return OG_LOCALE.get(lang, "en_GB")


def hreflang_links(path_after_locale: str) -> str:
    lines = []
    for loc in LOCALES:
        if path_after_locale == "":
            href = f"{SITE}/{loc}/"
        else:
            href = f"{SITE}/{loc}/{path_after_locale}".rstrip("/") + "/"
        lines.append(f'  <link rel="alternate" hreflang="{loc}" href="{href}" />')
    xd = f"{SITE}/en/" if path_after_locale == "" else f"{SITE}/en/{path_after_locale.lstrip('/')}"
    if not xd.endswith("/"):
        xd += "/"
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{xd}" />')
    return "\n".join(lines)


def icon_links() -> str:
    return f'''  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="/gallery/favicons/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/gallery/favicons/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="{APPLE_TOUCH}" />
  <link rel="manifest" href="{MANIFEST}" />
  <meta name="theme-color" content="#7caae5" />
  <meta name="msapplication-TileColor" content="#7caae5" />
  <meta name="msapplication-TileImage" content="/gallery/favicons/mstile-150x150.png" />'''


def geo_meta() -> str:
    return f'''  <meta name="geo.region" content="{GEO_REGION}" />
  <meta name="geo.placename" content="{esc(GEO_PLACENAME)}" />
  <meta name="geo.position" content="{GEO_LAT};{GEO_LNG}" />
  <meta name="ICBM" content="{GEO_LAT}, {GEO_LNG}" />'''


def seo_head(
    *,
    lang: str,
    title: str,
    description: str,
    canonical: str,
    path_after: str,
    og_type: str = "website",
    og_image: str = DEFAULT_OG_IMAGE,
    og_image_alt: str = "",
    og_image_w: int = DEFAULT_OG_IMAGE_W,
    og_image_h: int = DEFAULT_OG_IMAGE_H,
    keywords: str = "",
    robots: str = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1",
    article_published: str = "",
    article_modified: str = "",
    json_ld: list[dict[str, Any]] | dict[str, Any] | None = None,
) -> str:
    """Full <head> SEO block (title through structured data), no charset/viewport/fonts/css."""
    desc = description.strip()
    if len(desc) > 160:
        # Soft trim on word boundary for SERP/snippet hygiene
        cut = desc[:157].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
        desc_meta = cut
    else:
        desc_meta = desc

    og_title = title
    tw_title = title
    image_alt = og_image_alt or title
    locale = og_locale(lang)

    alt_locales = []
    for loc in LOCALES:
        if loc == lang:
            continue
        alt_locales.append(
            f'  <meta property="og:locale:alternate" content="{og_locale(loc)}" />'
        )

    kw_line = f'\n  <meta name="keywords" content="{esc(keywords)}" />' if keywords else ""
    article_lines = ""
    if og_type == "article":
        if article_published:
            article_lines += f'\n  <meta property="article:published_time" content="{article_published}" />'
        if article_modified:
            article_lines += f'\n  <meta property="article:modified_time" content="{article_modified}" />'
        article_lines += '\n  <meta property="article:section" content="Travel" />'
        article_lines += f'\n  <meta property="article:author" content="{esc(BRAND)}" />'

    ld_blocks = ""
    if json_ld:
        items = json_ld if isinstance(json_ld, list) else [json_ld]
        for item in items:
            ld_blocks += (
                "\n  <script type=\"application/ld+json\">\n"
                + json.dumps(item, ensure_ascii=False, indent=2)
                + "\n  </script>"
            )

    return f'''  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc_meta)}" />{kw_line}
  <meta name="robots" content="{robots}" />
  <meta name="googlebot" content="{robots}" />
  <meta name="author" content="{esc(BRAND)}" />
  <meta name="publisher" content="{esc(BRAND)}" />
  <link rel="canonical" href="{canonical}" />
{hreflang_links(path_after)}
{icon_links()}
{geo_meta()}
  <meta property="og:site_name" content="{esc(BRAND)}" />
  <meta property="og:title" content="{esc(og_title)}" />
  <meta property="og:description" content="{esc(desc_meta)}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:locale" content="{locale}" />
{chr(10).join(alt_locales)}
  <meta property="og:image" content="{og_image}" />
  <meta property="og:image:secure_url" content="{og_image}" />
  <meta property="og:image:type" content="{_image_mime(og_image)}" />
  <meta property="og:image:width" content="{og_image_w}" />
  <meta property="og:image:height" content="{og_image_h}" />
  <meta property="og:image:alt" content="{esc(image_alt)}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(tw_title)}" />
  <meta name="twitter:description" content="{esc(desc_meta)}" />
  <meta name="twitter:image" content="{og_image}" />
  <meta name="twitter:image:alt" content="{esc(image_alt)}" />{article_lines}{ld_blocks}'''


def _image_mime(url: str) -> str:
    u = (url or "").lower()
    if u.endswith(".png"):
        return "image/png"
    if u.endswith(".webp"):
        return "image/webp"
    if u.endswith(".gif"):
        return "image/gif"
    return "image/jpeg"


def organization_ld() -> dict[str, Any]:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{SITE}/#organization",
        "name": BRAND,
        "url": f"{SITE}/",
        "logo": {
            "@type": "ImageObject",
            "url": LOGO_URL,
            "width": 82,
            "height": 82,
        },
        "image": DEFAULT_OG_IMAGE,
        "telephone": PHONE,
        "address": GEO_ADDRESS,
        "sameAs": [
            "https://www.instagram.com/seaviewserenityatsyros/",
        ],
    }


def lodging_ld(lang: str, description: str) -> dict[str, Any]:
    return {
        "@context": "https://schema.org",
        "@type": ["LodgingBusiness", "VacationRental"],
        "@id": f"{SITE}/#lodging",
        "name": BRAND,
        "description": description,
        "url": f"{SITE}/{lang}/",
        "image": [DEFAULT_OG_IMAGE, f"{SITE}/Articles/media/villa-terrace-sunset.jpg"],
        "telephone": PHONE,
        "address": GEO_ADDRESS,
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": GEO_LAT,
            "longitude": GEO_LNG,
        },
        "hasMap": GEO_MAPS,
        "priceRange": "€€",
        "petsAllowed": False,
        "checkinTime": "15:00",
        "checkoutTime": "12:00",
        "numberOfRooms": 3,
        "occupancy": {"@type": "QuantitativeValue", "maxValue": 6},
        "amenityFeature": [
            {"@type": "LocationFeatureSpecification", "name": "Kitchen", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "WiFi", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Dedicated workspace", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "FreeParking", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Washer", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Sea view", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Fireplace", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Outdoor fire pit", "value": True},
        ],
        "containedInPlace": {
            "@type": "Place",
            "name": "Delfini Beach, Syros",
            "address": GEO_ADDRESS,
        },
        "inLanguage": lang,
        "parentOrganization": {"@id": f"{SITE}/#organization"},
    }


def website_ld(lang: str) -> dict[str, Any]:
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "url": f"{SITE}/",
        "name": BRAND,
        "inLanguage": LOCALES,
        "publisher": {"@id": f"{SITE}/#organization"},
        "potentialAction": {
            "@type": "ReadAction",
            "target": [f"{SITE}/{loc}/" for loc in LOCALES],
        },
    }


def breadcrumb_ld(items: list[tuple[str, str]]) -> dict[str, Any]:
    """items: list of (name, absolute_url)"""
    elements = []
    for i, (name, url) in enumerate(items, start=1):
        elements.append(
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": url,
            }
        )
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }


def webpage_ld(
    *,
    lang: str,
    name: str,
    description: str,
    url: str,
    page_type: str = "WebPage",
) -> dict[str, Any]:
    return {
        "@context": "https://schema.org",
        "@type": page_type,
        "@id": f"{url}#webpage",
        "url": url,
        "name": name,
        "description": description,
        "inLanguage": lang,
        "isPartOf": {"@id": f"{SITE}/#website"},
        "about": {"@id": f"{SITE}/#lodging"},
        "publisher": {"@id": f"{SITE}/#organization"},
    }
