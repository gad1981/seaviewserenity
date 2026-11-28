#!/usr/bin/env python3
"""Shared top nav — Articles white fixed bar is the site-wide norm."""
from __future__ import annotations

# Bump when shared CSS changes so all pages refresh together
CSS_V = "norm31"


def css_head_links(*, articles: bool = False, sitepro: bool = False) -> str:
    """Normalized stylesheet stack — Articles prototype for every page."""
    v = CSS_V
    links = []
    if sitepro:
        links.append(f'  <link href="/css/i18n.css?v={v}" rel="stylesheet" type="text/css" />')
        links.append(f'  <link href="/css/site-chrome.css?v={v}" rel="stylesheet" type="text/css" />')
        links.append(f'  <link href="/css/sitepro-i18n.css?v={v}" rel="stylesheet" type="text/css" />')
        links.append(f'  <link href="/css/footer.css?v={v}" rel="stylesheet" type="text/css" />')
    else:
        links.append(f'  <link href="/css/site-chrome.css?v={v}" rel="stylesheet" />')
        if articles:
            links.append(f'  <link href="/css/articles.css?v={v}" rel="stylesheet" />')
        links.append(f'  <link href="/css/i18n.css?v={v}" rel="stylesheet" />')
        links.append(f'  <link href="/css/footer.css?v={v}" rel="stylesheet" />')
    return "\n".join(links)


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


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


def site_chrome(lang: str, ui: dict, active: str, path_after: str) -> str:
    """Brand + primary nav + language dropdown (exact Articles header)."""
    from lang_switcher import lang_dropdown

    switcher = lang_dropdown(
        lang, path_after, ui["switcher_aria"], ui.get("_lang_names") or {}, sitepro=False
    )
    # Callers pass language_names via ui["_lang_names"] or we import LANG from caller
    return site_chrome_with_switcher(
        lang, ui, active, path_after, switcher, nav_html(lang, ui, active)
    )


def site_chrome_with_switcher(
    lang: str, ui: dict, active: str, path_after: str, switcher: str, nav: str
) -> str:
    menu_open = esc(ui.get("menu_open", "Menu"))
    menu_close = esc(ui.get("menu_close", "Close menu"))
    return f'''  <header class="svs-shell-header">
    <a class="svs-shell-brand" href="/{lang}/">
      <img src="/gallery/Picture 1.png" alt="{esc(ui["brand"])}" />
      <span>{esc(ui["brand"])}</span>
    </a>
    <button class="svs-nav-toggle" type="button" aria-expanded="false" aria-controls="svs-nav-panel" aria-label="{menu_open}" data-label-open="{menu_open}" data-label-close="{menu_close}">
      <span aria-hidden="true"></span><span aria-hidden="true"></span><span aria-hidden="true"></span>
    </button>
    <div class="svs-nav-panel" id="svs-nav-panel">
      <nav class="svs-shell-nav" aria-label="Primary">
        {nav}
      </nav>
      {switcher}
    </div>
  </header>'''


def build_chrome(lang: str, ui: dict, active: str, path_after: str, lang_names: dict) -> str:
    from lang_switcher import lang_dropdown

    switcher = lang_dropdown(lang, path_after, ui["switcher_aria"], lang_names, sitepro=False)
    return site_chrome_with_switcher(
        lang, ui, active, path_after, switcher, nav_html(lang, ui, active)
    )
