#!/usr/bin/env python3
"""Shared site footer for Site.pro pages and Articles shell."""
from __future__ import annotations

import json
from pathlib import Path

WHATSAPP = "https://api.whatsapp.com/send?phone=306937027555"
INSTAGRAM = "https://www.instagram.com/seaviewserenityatsyros/"
FACEBOOK = "https://www.facebook.com/seaviewserenity/"
MAPS = "https://maps.app.goo.gl/z3p1PRkGuHZF1TBDA"
BOOKING = "https://www.booking.com/hotel/gr/sea-view-serenity.el.html"
AIRBNB = "https://www.airbnb.com/rooms/1116489236524222235"
VRBO = "https://www.vrbo.com/en-gb/p11962377"
ADDRESS = "Delfini Beach, Ano Syros 81400, Syros, Greece"
PHONE_DISPLAY = "+30 693 702 7555"

LEGAL = json.loads((Path(__file__).resolve().parents[1] / "i18n" / "legal.json").read_text(encoding="utf-8"))


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def cookie_banner(lang: str) -> str:
    L = LEGAL[lang]
    return f'''<div id="svs-cookie-banner" class="svs-cookie-banner" hidden role="dialog" aria-live="polite" aria-label="{esc(L["cookies_nav"])}">
  <div class="svs-cookie-banner__inner">
    <p class="svs-cookie-banner__text">{esc(L["cookie_banner_text"])}</p>
    <div class="svs-cookie-banner__actions">
      <a class="svs-cookie-banner__link" href="/{lang}/Cookies/">{esc(L["cookie_banner_policy"])}</a>
      <button type="button" class="svs-cookie-banner__btn" data-svs-cookie-accept>{esc(L["cookie_banner_accept"])}</button>
    </div>
  </div>
</div>
<script src="/js/cookie-banner.js" defer></script>'''


def site_footer(lang: str, ui: dict) -> str:
    home = f"/{lang}/"
    villa = f"/{lang}/The-Villa/"
    articles = f"/{lang}/Articles/"
    book = f"/{lang}/Book-now/"
    terms = f"/{lang}/Terms/"
    cookies = f"/{lang}/Cookies/"
    brand = esc(ui["brand"])
    L = LEGAL[lang]
    return f'''<footer class="svs-site-footer" role="contentinfo">
  <div class="svs-site-footer__inner">
    <div class="svs-site-footer__brand">
      <a class="svs-site-footer__logo" href="{home}">
        <img src="/gallery/Picture 1.png" alt="{brand}" width="48" height="48" loading="lazy" />
        <span>{brand}</span>
      </a>
      <p class="svs-site-footer__tagline">{esc(ui["footer_tagline"])}</p>
    </div>
    <div class="svs-site-footer__grid">
      <nav class="svs-site-footer__col" aria-label="{esc(ui["footer_explore"])}">
        <h2 class="svs-site-footer__heading">{esc(ui["footer_explore"])}</h2>
        <ul>
          <li><a href="{home}">{esc(ui["nav_home"])}</a></li>
          <li><a href="{villa}">{esc(ui["nav_villa"])}</a></li>
          <li><a href="{articles}">{esc(ui["nav_articles"])}</a></li>
          <li><a href="{book}">{esc(ui["nav_book"])}</a></li>
        </ul>
      </nav>
      <nav class="svs-site-footer__col" aria-label="{esc(ui["footer_book"])}">
        <h2 class="svs-site-footer__heading">{esc(ui["footer_book"])}</h2>
        <ul>
          <li><a href="{book}">{esc(ui["nav_book"])}</a></li>
          <li><a href="{BOOKING}" target="_blank" rel="noopener">Booking.com</a></li>
          <li><a href="{AIRBNB}" target="_blank" rel="noopener">Airbnb</a></li>
          <li><a href="{VRBO}" target="_blank" rel="noopener">Vrbo</a></li>
        </ul>
      </nav>
      <div class="svs-site-footer__col">
        <h2 class="svs-site-footer__heading">{esc(ui["footer_contact"])}</h2>
        <ul>
          <li><a href="{WHATSAPP}" target="_blank" rel="noopener">{esc(ui["footer_phone_label"])}: {PHONE_DISPLAY}</a></li>
          <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">@seaviewserenityatsyros</a></li>
          <li><a href="{MAPS}" target="_blank" rel="noopener">{esc(ui["footer_maps"])}</a></li>
          <li><span class="svs-site-footer__muted">{esc(ui["footer_address_label"])}: {esc(ADDRESS)}</span></li>
        </ul>
      </div>
      <nav class="svs-site-footer__col" aria-label="{esc(L["legal_heading"])}">
        <h2 class="svs-site-footer__heading">{esc(L["legal_heading"])}</h2>
        <ul>
          <li><a href="{terms}">{esc(L["terms_nav"])}</a></li>
          <li><a href="{cookies}">{esc(L["cookies_nav"])}</a></li>
          <li><a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></li>
          <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li>
        </ul>
      </nav>
    </div>
    <div class="svs-site-footer__bottom">
      <div>
        <p>{esc(ui["footer_copy"]).replace("seaviewserenity.gr", f'<a href="{home}">seaviewserenity.gr</a>')}</p>
        <nav class="svs-site-footer__legal" aria-label="{esc(L["legal_heading"])}">
          <a href="{terms}">{esc(L["terms_nav"])}</a>
          <a href="{cookies}">{esc(L["cookies_nav"])}</a>
        </nav>
      </div>
      <p>{esc(ui["footer_designed"]).replace("georgegad.com", '<a href="https://georgegad.com" target="_blank" rel="noopener">georgegad.com</a>')}</p>
    </div>
  </div>
</footer>
{cookie_banner(lang)}'''
