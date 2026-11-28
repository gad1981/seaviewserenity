import json, re
from pathlib import Path

D = Path(__file__).parent
KICKER = "Artikel · Syros & Urlaub am Meer"

META = {
    "where-to-stay-syros-areas-compared": dict(
        title="Wo übernachten auf Syros? Ermoupoli, Kini, Galissas im Vergleich",
        description="Wo wohnen auf Syros? Ermoupoli, Kini und Delfini, Galissas und die Südküste im Vergleich – für ruhige Strände, Nachtleben oder eine Villa-Woche.",
        keywords="Unterkunft Syros, wo übernachten Syros, Syros Urlaub Region, Kini oder Ermoupoli, Delfini Beach Unterkunft, Galissas Syros",
        hero_alt="Ano Syros und Ermoupoli oberhalb des Hafens",
        hero_caption="Ano Syros und Ermoupoli oberhalb des Hafens. Foto: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).",
    ),
    "seven-day-syros-itinerary-villa-base": dict(
        title="7 Tage auf Syros: Reiseplan für eine Villa an der Westküste",
        description="Eine Woche auf Syros ab einer Villa bei Delfini und Kini: Strände, Ermoupoli, Ano Syros, Essen, Ruhetage – und wann der Autoschlüssel am Haken bleibt.",
        keywords="Syros 7 Tage Reiseplan, Syros Wochenplan, Syros Urlaub Villa, Syros Rundreise Woche, Delfini Kini Reiseplan",
        hero_alt="Liegestühle auf der Terrasse der Sea View Serenity bei Sonnenuntergang",
        hero_caption="Terrassenabend in der Sea View Serenity: Erholung zwischen bewegten Inseltagen.",
    ),
    "getting-around-syros-car-rental-bus": dict(
        title="Unterwegs auf Syros: Mietwagen, Bus, Taxi – oder ohne Auto?",
        description="Mobil auf Syros ab der Westküste: Wann sich ein Mietwagen lohnt, was Busse und Taxis leisten und wie Fährhafen und Anreise zu Delfini und Kini passen.",
        keywords="Syros Mietwagen, Syros Bus, Syros Taxi, Fortbewegung Syros, Syros ohne Auto, Syros Fähre Anreise",
        hero_alt="Fährschiff im Hafen von Syros",
        hero_caption="Fähre im Hafen von Syros: Die Ankunft ist der leichte Teil – die Inselorganisation kommt danach. Foto: Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).",
    ),
    "kini-restaurants-sunset-dining": dict(
        title="Kini auf Syros: Tavernen und Abendessen bei Sonnenuntergang",
        description="Sonnenuntergangs-Dinner in Kini planen, mit Delfini als ruhigem Badeort: Tavernen an der Westküste, Tipps zur Uhrzeit und wann sich Ermoupoli lohnt.",
        keywords="Kini Restaurants, Kini Sonnenuntergang Abendessen, Syros Tavernen Westküste, Delfini Beach essen, Syros Essen gehen",
        hero_alt="Sonnenuntergang über dem Meer bei Kini auf Syros",
        hero_caption="Sonnenuntergang in Kini – das Abendtheater der Westküste. Foto: ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
    ),
    "syros-in-may-june-september": dict(
        title="Syros im Mai, Juni und September: ideal für die Villa",
        description="Warum Mai, Juni und September oft die schönste Zeit für Urlaub in einer Villa auf Syros sind: Meerestemperatur, Andrang, Fähren und Abende an der Westküste.",
        keywords="Syros Mai, Syros Juni, Syros September, beste Reisezeit Syros Villa, Nebensaison Kykladen",
        hero_alt="Schlafzimmer mit offenen Fensterläden zu Bougainvillea und Meer",
        hero_caption="Licht der Übergangszeit durch offene Fensterläden in der Sea View Serenity.",
    ),
    "things-to-do-on-syros": dict(
        title="Syros Sehenswürdigkeiten: Strände, Ermoupoli, Essen, Tagespläne",
        description="Praktischer Überblick zu Syros: Strände an der Westküste, Ermoupoli und Ano Syros, Essen und einfache Tagespläne ab einer Villa am Meer.",
        keywords="Syros Sehenswürdigkeiten, Syros Aktivitäten, Syros Strände, Ermoupoli Sehenswürdigkeiten, Syros Urlaub Tipps",
        hero_alt="Panoramablick auf Ermoupoli auf Syros",
        hero_caption="Ermoupoli: Die Liste der Inselerlebnisse beginnt mit einer richtigen Stadt. Foto: Zacharias Mitzelos / Wikimedia Commons (CC0).",
    ),
    "ano-syros-ermoupoli-walking-guide": dict(
        title="Ano Syros und Ermoupoli zu Fuß: zwei Städte, ein Rundgang",
        description="Rundgang durch Ermoupoli und Ano Syros: klassizistische Straßen, Hafen, Gassen, Aussichtspunkte – und wie Sie den Stadttag mit der Westküste verbinden.",
        keywords="Ano Syros Spaziergang, Ermoupoli Stadtrundgang, Syros Altstadt, Ermoupoli Sehenswürdigkeiten, Ano Syros Sehenswürdigkeiten",
        hero_alt="Blick von Ano Syros auf Ermoupoli",
        hero_caption="Ermoupoli von Ano Syros aus gesehen – beide Ebenen der Hauptstadt zu Fuß erleben. Foto: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0).",
    ),
}

FIG = re.compile(r'<figure class="svs-figure">\s*<img[^>]*alt="([^"]*)"[^>]*>\s*<figcaption>(.*?)</figcaption>', re.S)

out = {}
for slug, m in META.items():
    body = (D / f"{slug}.body.html").read_text(encoding="utf-8").strip()
    figs = FIG.findall(body)
    out[slug] = {
        "title": m["title"],
        "description": m["description"],
        "keywords": m["keywords"],
        "kicker": KICKER,
        "hero_alt": m["hero_alt"],
        "hero_caption": m["hero_caption"],
        "mid_alt": figs[0][0],
        "mid_caption": figs[0][1],
        "body": body,
    }

target = D.parent / "i18n_de_a.json"
target.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

# validation
src = json.load(open(D.parent / "en_source_packages.json", encoding="utf-8"))
chk = json.load(open(target, encoding="utf-8"))
wc = lambda h: len(re.sub(r"<[^>]+>", " ", h).split())
for slug in META:
    b, e = chk[slug]["body"], src[slug]["body"]
    same = lambda p: sorted(re.findall(p, b)) == sorted(re.findall(p, e))
    refs = re.findall(r'href="#ref\d+"', b) == re.findall(r'href="#ref\d+"', e)
    imgs = re.findall(r'src="([^"]+)"', b) == re.findall(r'src="([^"]+)"', e)
    tags = {t: (b.count("<" + t), e.count("<" + t)) for t in ("h2", "p>", "li>", "figure", "sup", "ul", "ol", "div")}
    bad = {t: v for t, v in tags.items() if v[0] != v[1]}
    print(f"{slug}: DE words={wc(b)} EN words={wc(e)} refs_ok={refs} imgs_ok={imgs} tagdiff={bad} title_len={len(chk[slug]['title'])} desc_len={len(chk[slug]['description'])}")
