#!/usr/bin/env python3
"""Restore original Site.pro Home / Villa / Book pages under locale prefixes."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ["en", "el", "fr", "de", "it", "he"]
SITE = "https://seaviewserenity.gr"
UI = json.loads((ROOT / "i18n" / "ui.json").read_text(encoding="utf-8"))
LANG_NAMES = UI["language_names"]
TPL = {
    "home": (ROOT / "i18n" / "sitepro" / "home.en.html").read_text(encoding="utf-8"),
    "villa": (ROOT / "i18n" / "sitepro" / "villa.en.html").read_text(encoding="utf-8"),
    "book": (ROOT / "i18n" / "sitepro" / "book.en.html").read_text(encoding="utf-8"),
}

# Exact Site.pro English body copy (must match templates byte-for-byte)
HOME_WELCOME = (
    "Welcome to Sea View Serenity, your exclusive coastal escape just a leisurely "
    "10-min walk from Delfini beach at Syros island. Ideal for families or groups "
    "seeking a serene getaway, our charming house offers cozy accommodations and "
    "ample space to unwind. Enjoy candlelit dinners with breathtaking sea views "
    "from your bedrooms. With umbrellas and a beach bar nearby, endless days of "
    "sun-soaked bliss await. Whether lounging on the shore, hiking trails, or "
    "savoring local seafood, our home is your perfect coastal base."
)
HOME_VIEW = (
    "Our seaside house offers breathtaking views that perfectly capture the essence "
    "of coastal beauty. From the spacious windows, you can gaze out over the expansive "
    "aegean sea, watching the waves gently lap against the shore. The picturesque "
    "scenery is complemented by stunning sunsets that paint the sky in vibrant hues, "
    "providing a serene backdrop for relaxation. Whether you're enjoying a morning "
    "coffee or unwinding in the evening, the view from our house promises to be a "
    "constant source of tranquility and inspiration."
)
HOME_AMENITIES = (
    "Our seaside house offers a range of top-notch amenities to ensure a comfortable "
    "and enjoyable stay. Guests can take advantage of the two dedicated parking slots "
    "under a protective ceiling, making arrivals and departures seamless. The property "
    "includes complimentary Wi-Fi coverage throughout, allowing you to stay connected. "
    "The fully equipped kitchen is perfect for preparing meals, featuring a large fridge "
    "with freezer, electric stove, kettle, toaster, microwave, and French coffee maker. "
    "Inside, the second bathroom features a sculptured marble-framed mirror, adding a "
    "touch of elegance, and includes a washing machine for added convenience. The house "
    "also boasts cozy bedrooms with plush bedding, an indoor fire pit for evening "
    "gatherings, and easy access to a nearby beach bar and amenities."
)

VILLA_LABELS = {
    "en": {
        "Bedrooms x 3": "Bedrooms x 3",
        "Bathrooms x 2": "Bathrooms x 2",
        "Dinner Area": "Dinner Area",
        "Living Room": "Living Room",
    },
    "el": {
        "Bedrooms x 3": "Υπνοδωμάτια x 3",
        "Bathrooms x 2": "Μπάνια x 2",
        "Dinner Area": "Τραπεζαρία",
        "Living Room": "Σαλόνι",
    },
    "fr": {
        "Bedrooms x 3": "Chambres x 3",
        "Bathrooms x 2": "Salles de bain x 2",
        "Dinner Area": "Salle à manger",
        "Living Room": "Salon",
    },
    "de": {
        "Bedrooms x 3": "Schlafzimmer x 3",
        "Bathrooms x 2": "Bäder x 2",
        "Dinner Area": "Essbereich",
        "Living Room": "Wohnzimmer",
    },
    "it": {
        "Bedrooms x 3": "Camere x 3",
        "Bathrooms x 2": "Bagni x 2",
        "Dinner Area": "Zona pranzo",
        "Living Room": "Soggiorno",
    },
    "he": {
        "Bedrooms x 3": "חדרי שינה x 3",
        "Bathrooms x 2": "חדרי רחצה x 2",
        "Dinner Area": "פינת אוכל",
        "Living Room": "סלון",
    },
}

BOOK_STRINGS = {
    "Contact Us": {
        "en": "Contact Us",
        "el": "Επικοινωνία",
        "fr": "Nous contacter",
        "de": "Kontakt",
        "it": "Contattaci",
        "he": "צור קשר",
    },
    "Book your Stay": {
        "en": "Book your Stay",
        "el": "Κλείστε τη διαμονή σας",
        "fr": "Réservez votre séjour",
        "de": "Buchen Sie Ihren Aufenthalt",
        "it": "Prenota il soggiorno",
        "he": "הזמינו את השהייה",
    },
    "Find us on the map": None,  # ui book_map_title
    "You can also book your stay through one of the booking platforms. Click to check availability.": None,  # ui
    "If you seek a tranquil place near the sea, Sea View Serenity is the ideal destination for you.": {
        "en": "If you seek a tranquil place near the sea, Sea View Serenity is the ideal destination for you.",
        "el": "Αν αναζητάτε ένα ήρεμο μέρος δίπλα στη θάλασσα, το Sea View Serenity είναι ο ιδανικός προορισμός.",
        "fr": "Si vous cherchez un lieu tranquille près de la mer, Sea View Serenity est la destination idéale.",
        "de": "Wenn Sie einen ruhigen Ort am Meer suchen, ist Sea View Serenity das ideale Ziel.",
        "it": "Se cercate un luogo tranquillo vicino al mare, Sea View Serenity è la destinazione ideale.",
        "he": "אם אתם מחפשים מקום שקט ליד הים, Sea View Serenity הוא היעד האידיאלי.",
    },
    "Direct Phone or Whatsapp:": {
        "en": "Direct Phone or Whatsapp:",
        "el": "Τηλέφωνο ή WhatsApp:",
        "fr": "Téléphone ou WhatsApp :",
        "de": "Telefon oder WhatsApp:",
        "it": "Telefono o WhatsApp:",
        "he": "טלפון או WhatsApp:",
    },
    "DM on Instagram:": {
        "en": "DM on Instagram:",
        "el": "Μήνυμα στο Instagram:",
        "fr": "DM sur Instagram :",
        "de": "DM auf Instagram:",
        "it": "DM su Instagram:",
        "he": "הודעה ב-Instagram:",
    },
    "Address:": {
        "en": "Address:",
        "el": "Διεύθυνση:",
        "fr": "Adresse :",
        "de": "Adresse:",
        "it": "Indirizzo:",
        "he": "כתובת:",
    },
}

MAP_CLICK = {
    "en": "Click</a> and check on Google maps",
    "el": "Κλικ</a> και δείτε στο Google maps",
    "fr": "Cliquez</a> pour ouvrir Google Maps",
    "de": "Klicken</a> und in Google Maps prüfen",
    "it": "Clic</a> e controllate su Google Maps",
    "he": "לחצו</a> ובדקו ב-Google Maps",
}


def lang_dd(lang: str, path_after: str, aria: str) -> str:
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from lang_switcher import lang_dropdown

    return lang_dropdown(lang, path_after, aria, LANG_NAMES, sitepro=True)


def hreflang(path_after: str) -> str:
    lines = []
    for loc in LOCALES:
        href = f"{SITE}/{loc}/{path_after}" if path_after else f"{SITE}/{loc}/"
        lines.append(f'  <link rel="alternate" hreflang="{loc}" href="{href}" />')
    xd = f"{SITE}/en/{path_after}" if path_after else f"{SITE}/en/"
    lines.append(f'  <link rel="alternate" hreflang="x-default" href="{xd}" />')
    return "\n".join(lines)


def abs_assets(html: str) -> str:
    for attr in ("href", "src"):
        html = re.sub(rf'{attr}="(css/)', rf'{attr}="/\1', html)
        html = re.sub(rf'{attr}="(js/)', rf'{attr}="/\1', html)
        html = re.sub(rf'{attr}="(gallery/)', rf'{attr}="/\1', html)
        html = re.sub(rf'{attr}="(gallery_gen/)', rf'{attr}="/\1', html)
    return html


def fix_nav(html: str, lang: str, ui: dict, active: str, path_after: str = "") -> str:
    home_cls = ' class="wb_this_page_menu_item active"' if active == "home" else ""
    villa_cls = ' class="wb_this_page_menu_item active"' if active == "villa" else ""
    art_cls = ' class="wb_this_page_menu_item active"' if active == "articles" else ""
    book_cls = ' class="wb_this_page_menu_item active"' if active == "book" else ""
    menu = (
        f'<ul class="hmenu" dir="ltr">'
        f'<li{home_cls}><a href="/{lang}/">{ui["nav_home"]}</a></li>'
        f'<li{villa_cls}><a href="/{lang}/The-Villa/">{ui["nav_villa"]}</a></li>'
        f'<li{art_cls}><a href="/{lang}/Articles/">{ui["nav_articles"]}</a></li>'
        f'<li{book_cls}><a href="/{lang}/Book-now/">{ui["nav_book"]}</a></li>'
        f"</ul>"
    )
    html = re.sub(r'<ul class="hmenu"[^>]*>.*?</ul>', menu, html, count=1, flags=re.S)
    html = re.sub(r'href="https://seaviewserenity\.gr/?"', f'href="/{lang}/"', html)
    html = re.sub(r'href="https://seaviewserenity\.gr/book-now"', f'href="/{lang}/Book-now/"', html)
    html = html.replace('href="The-Villa/"', f'href="/{lang}/The-Villa/"')
    html = html.replace('href="Book-now/"', f'href="/{lang}/Book-now/"')
    html = html.replace('href="Articles/"', f'href="/{lang}/Articles/"')
    html = html.replace("><span>Book Now</span>", f"><span>{ui['home_book_cta']}</span>")
    # Language dropdown OUTSIDE wb-menu so it never sits inside the 32px burger box
    dd = lang_dd(lang, path_after, ui["switcher_aria"])
    html = re.sub(
        r'(class="wb_element wb-menu[^"]*"[^>]*>[\s\S]*?<div class="clearfix"></div></div>)',
        rf"\1{dd}",
        html,
        count=1,
    )
    # Remove unused Site.pro Languages plugin slot (Book page)
    html = re.sub(
        r'<div id="[^"]+" class="wb_element wb-prevent-layout-click" data-plugin="Languages"></div>',
        "",
        html,
        count=1,
    )
    return html


def translate_home(html: str, lang: str, ui: dict) -> str:
    html = re.sub(r"<title>[^<]*</title>", f"<title>{ui['home_title']}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{ui["home_description"]}"',
        html,
        count=1,
    )
    if lang == "en":
        return html
    html = html.replace(">Welcome</", f">{ui['home_welcome_h2']}</")
    html = html.replace(">The View</", f">{ui['home_view_h2']}</")
    html = html.replace(">Amenities</", f">{ui['home_amenities_h2']}</")
    html = html.replace(HOME_WELCOME, ui["home_welcome_p"])
    html = html.replace(HOME_VIEW, ui["home_view_p"])
    html = html.replace(HOME_AMENITIES, ui["home_amenities_p"])
    return html


def translate_villa(html: str, lang: str, ui: dict) -> str:
    html = re.sub(r"<title>[^<]*</title>", f"<title>{ui['villa_title']}</title>", html, count=1)
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{ui["villa_description"]}"',
        html,
        count=1,
    )
    if lang == "en":
        return html
    for en, tr in VILLA_LABELS[lang].items():
        html = html.replace(en, tr)
    return html


def translate_book(html: str, lang: str, ui: dict) -> str:
    html = re.sub(
        r"<title>[^<]*</title>",
        f"<title>{ui['book_title']} | Sea View Serenity</title>",
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{ui["book_description"]}"',
        html,
        count=1,
    )
    if lang != "en":
        for en, val in BOOK_STRINGS.items():
            if val is None:
                if en == "Find us on the map":
                    tr = ui["book_map_title"]
                else:
                    tr = ui["book_platforms_lede"]
            else:
                tr = val[lang]
            html = html.replace(en, tr)
        html = html.replace(
            "Click</a> and check on Google maps",
            MAP_CLICK[lang],
        )

    # Interactive map: keep Site.pro picture box, swap static image for embed
    embed = (
        f'<iframe class="svs-sitepro-map" title="{ui["book_map_title"]} — Sea View Serenity" '
        f'src="https://www.google.com/maps?q=37.4584631,24.9024781&amp;z=15&amp;hl={lang}&amp;output=embed" '
        f'loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'
    )
    html = re.sub(
        r'<img loading="lazy" alt="" src="/gallery_gen/3e7a1034080468cbb3c86a1b7102ed98_1027x1041_429x0_1904x1041_crop\.png">',
        embed,
        html,
        count=1,
    )
    # Also match before abs_assets (relative path) — handled after abs so use absolute
    html = re.sub(
        r'<img loading="lazy" alt="" src="gallery_gen/3e7a1034080468cbb3c86a1b7102ed98_1027x1041_429x0_1904x1041_crop\.png">',
        embed,
        html,
        count=1,
    )
    return html


def inject_head_body(html: str, lang: str, path_after: str, ui: dict, canonical: str) -> str:
    # Keep LTR Site.pro layout for all locales (including Hebrew) so absolute positions hold
    html = re.sub(r"<html[^>]*>", f'<html lang="{lang}">', html, count=1)
    html = re.sub(
        r'<link rel="canonical" href="[^"]*"\s*/?>',
        f'<link rel="canonical" href="{canonical}" />',
        html,
        count=1,
    )
    inject = (
        f"{hreflang(path_after)}\n"
        f'  <link href="/css/i18n.css" rel="stylesheet" type="text/css" />\n'
        f'  <link href="/css/sitepro-i18n.css" rel="stylesheet" type="text/css" />\n'
        f'  <link href="/css/footer.css" rel="stylesheet" type="text/css" />\n'
    )
    html = html.replace(
        f'<link rel="canonical" href="{canonical}" />',
        f'<link rel="canonical" href="{canonical}" />\n{inject}',
        1,
    )
    html = re.sub(
        r'<meta property="og:url" content="[^"]*"\s*/?>',
        f'<meta property="og:url" content="{canonical}" />',
        html,
        count=1,
    )
    # Full site footer as sibling after #wb_root (Site.pro absolute layout)
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from site_footer import site_footer

    foot = site_footer(lang, ui)
    if re.search(r'</div>\s*<script src="/js/jquery', html):
        html = re.sub(
            r'(</div>\s*)(<script src="/js/jquery)',
            rf"\1{foot}\n\2",
            html,
            count=1,
        )
    elif "</body>" in html:
        html = html.replace("</body>", foot + "\n</body>", 1)

    if "</body>" in html and "lang-switcher.js" not in html:
        html = html.replace(
            "</body>",
            '  <script src="/js/lang-switcher.js" defer></script>\n</body>',
            1,
        )
    return html


def build_page(page: str, lang: str) -> str:
    ui = UI[lang]
    html = TPL[page]
    html = abs_assets(html)
    if page == "home":
        active, path_after, canonical = "home", "", f"{SITE}/{lang}/"
        html = fix_nav(html, lang, ui, active, path_after)
        html = translate_home(html, lang, ui)
    elif page == "villa":
        active, path_after, canonical = "villa", "The-Villa/", f"{SITE}/{lang}/The-Villa/"
        html = fix_nav(html, lang, ui, active, path_after)
        html = translate_villa(html, lang, ui)
    else:
        active, path_after, canonical = "book", "Book-now/", f"{SITE}/{lang}/Book-now/"
        html = fix_nav(html, lang, ui, active, path_after)
        html = translate_book(html, lang, ui)
    html = inject_head_body(html, lang, path_after, ui, canonical)
    html = re.sub(r'<base href="[^"]*"\s*/?>', '<base href="/" />', html)
    return html


def write_pages() -> None:
    for lang in LOCALES:
        mapping = {
            "home": ROOT / lang / "index.html",
            "villa": ROOT / lang / "The-Villa" / "index.html",
            "book": ROOT / lang / "Book-now" / "index.html",
        }
        for page, path in mapping.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build_page(page, lang), encoding="utf-8")
            print("restored", lang, page)


if __name__ == "__main__":
    write_pages()
