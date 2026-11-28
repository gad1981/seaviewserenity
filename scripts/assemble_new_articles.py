#!/usr/bin/env python3
"""Assemble draft article bodies + meta into EN HTML, ARTICLE_MEDIA, and i18n stubs."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT = Path(__file__).resolve().parent / "_draft_articles"
BUILD = Path(__file__).resolve().parent / "build_i18n.py"
ART_JSON = ROOT / "i18n" / "articles.json"
EN_ART = ROOT / "en" / "Articles"

KICKER = "Articles · Syros & seaside stays"
LANGS = ("el", "fr", "de", "it", "he")


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def sources_html(sources: list[dict]) -> str:
    items = []
    for s in sources:
        cite = esc(s["cite"])
        url = s["url"]
        sid = s["id"]
        items.append(
            f'      <li id="{sid}"><cite>{cite}</cite> — '
            f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a></li>'
        )
    return (
        '<section class="svs-sources" aria-label="References">\n'
        "    <h2>Sources and references</h2>\n"
        "    <ol>\n"
        + "\n".join(items)
        + "\n    </ol>\n  </section>"
    )


def shell_en(meta: dict, body: str, sources: str) -> str:
    """Minimal EN shell that extract_en_articles + article_page can rebuild from."""
    title = meta["title"]
    desc = meta["description"]
    kw = meta["keywords"]
    pub = meta["published"]
    mod = meta["modified"]
    hero = meta["hero_img"]
    hero_alt = meta.get("hero_alt", "")
    hero_cap = meta.get("hero_caption", "")
    slug_title = esc(title)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>{slug_title} | Sea View Serenity</title>
  <meta name="description" content="{esc(desc)}" />
  <meta name="keywords" content="{esc(kw)}" />
  <meta property="article:published_time" content="{pub}T00:00:00+02:00" />
  <meta property="article:modified_time" content="{mod}T00:00:00+02:00" />
</head>
<body class="svs-articles">
  <main>
    <div class="svs-shell svs-hero svs-hero--article">
      <p class="svs-kicker">{KICKER}</p>
      <h1>{slug_title}</h1>
    </div>
    <figure class="svs-figure svs-hero-figure svs-shell">
  <img src="/Articles/media/{hero}" alt="{esc(hero_alt)}" loading="lazy" width="1200" height="675" />
  <figcaption>{hero_cap}</figcaption>
</figure>
    <article class="svs-article-wrap">
      <div class="svs-article">
{body.strip()}
{sources}
      </div>
    </article>
  </main>
</body>
</html>
'''


def load_meta() -> dict:
    merged = {}
    for name in ("batch1.meta.json", "batch2.meta.json", "meta.json"):
        p = DRAFT / name
        if p.exists():
            merged.update(json.loads(p.read_text(encoding="utf-8")))
    return merged


def main() -> None:
    meta_all = load_meta()
    if not meta_all:
        raise SystemExit("No draft meta found in scripts/_draft_articles/")

    bodies = {p.stem.replace(".body", ""): p for p in DRAFT.glob("*.body.html")}
    # also accept slug.body.html → stem is slug.body
    bodies = {}
    for p in DRAFT.glob("*.body.html"):
        slug = p.name[: -len(".body.html")]
        bodies[slug] = p

    missing = [s for s in meta_all if s not in bodies]
    if missing:
        raise SystemExit(f"Missing body files for: {missing}")

    art_i18n = json.loads(ART_JSON.read_text(encoding="utf-8"))
    media_entries = []

    for slug, meta in meta_all.items():
        body = bodies[slug].read_text(encoding="utf-8")
        # Drop trailing sources if a draft included them
        body = re.split(r'<section class="svs-sources"', body, maxsplit=1)[0].rstrip()
        src = sources_html(meta["sources"])
        out_dir = EN_ART / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(shell_en(meta, body, src), encoding="utf-8")
        media_entries.append(
            f'    "{slug}": ("{meta["hero_img"]}", "{meta["mid_img"]}"),'
        )

        stub = {
            "title": meta["title"],
            "description": meta["description"],
            "keywords": meta["keywords"],
            "kicker": KICKER,
            "hero_alt": meta.get("hero_alt", ""),
            "hero_caption": meta.get("hero_caption", ""),
            "mid_alt": "",
            "mid_caption": "",
            "body": "<p>Translation pending.</p>",
        }
        art_i18n[slug] = {lang: dict(stub) for lang in LANGS}
        wc = len(re.sub(r"<[^>]+>", " ", body).split())
        print(f"wrote en/Articles/{slug}/ ({wc} words)")

    # Patch ARTICLE_MEDIA in build_i18n.py
    build = BUILD.read_text(encoding="utf-8")
    block = "ARTICLE_MEDIA = {\n"
    # Keep existing entries, add new ones before closing
    m = re.search(r"ARTICLE_MEDIA = \{([^}]*)\}", build, re.S)
    if not m:
        raise SystemExit("ARTICLE_MEDIA block not found")
    existing = m.group(1).rstrip()
    if not existing.endswith(","):
        existing = existing.rstrip() + ","
    new_lines = []
    for line in media_entries:
        key = line.split('"')[1]
        if f'"{key}"' not in existing:
            new_lines.append(line)
    patched = existing + ("\n" if new_lines else "") + "\n".join(new_lines) + "\n"
    build = build[: m.start()] + "ARTICLE_MEDIA = {" + patched + "}" + build[m.end() :]
    BUILD.write_text(build, encoding="utf-8")
    ART_JSON.write_text(json.dumps(art_i18n, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"updated ARTICLE_MEDIA (+{len(new_lines)}) and i18n stubs")


if __name__ == "__main__":
    main()
