#!/usr/bin/env python3
"""Fluent SEO meta (title/description/keywords/alts) for new articles — all locales."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "i18n" / "articles.json"

# Per-slug, per-lang SEO fields. Bodies left untouched here.
SEO: dict[str, dict[str, dict[str, str]]] = {
    "where-to-stay-syros-areas-compared": {
        "el": {
            "title": "Πού να μείνετε στη Σύρο: Ερμούπολη, Κίνι–Δελφίνι, Γαλησσάς και Νότος",
            "description": "Συγκρίνετε περιοχές διαμονής στη Σύρο — Ερμούπολη, δυτική ακτή Κινίου και Δελφινιού, Γαλησσάς και νότος — για ήσυχη παραλία, βραδινή ζωή ή εβδομάδα σε βίλα.",
            "keywords": "που να μεινετε Συρος, διαμονη Συρος περιοχες, Κινι ή Ερμουπολη, παραλια Δελφινι, Γαλησσας Συρος",
            "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα",
            "hero_alt": "Άνω Σύρος και Ερμούπολη πάνω από το λιμάνι",
            "hero_caption": "Άνω Σύρος και Ερμούπολη πάνω από το λιμάνι. Φωτογραφία: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).",
        },
        "fr": {
            "title": "Où dormir à Syros : Ermoupoli, Kini–Delfini, Galissas et le sud",
            "description": "Comparez les zones d’hébergement à Syros — Ermoupoli, côte ouest de Kini et Delfini, Galissas et le sud — pour plages calmes, soirées ou semaine en villa.",
            "keywords": "où dormir Syros, hébergement Syros quartiers, Kini ou Ermoupoli, plage Delfini, Galissas Syros",
            "kicker": "Articles · Syros et séjours en bord de mer",
            "hero_alt": "Ano Syros et Ermoupoli au-dessus du port",
            "hero_caption": "Ano Syros et Ermoupoli au-dessus du port. Photo : Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).",
        },
        "de": {
            "title": "Unterkunft auf Syros: Ermoupoli, Kini–Delfini, Galissas und der Süden",
            "description": "Vergleichen Sie Unterkunftsgebiete auf Syros — Ermoupoli, Westküste um Kini und Delfini, Galissas und Süden — für ruhige Strände, Abende oder eine Villa-Woche.",
            "keywords": "Unterkunft Syros, wo übernachten Syros, Kini oder Ermoupoli, Delfini Beach, Galissas Syros",
            "kicker": "Artikel · Syros & Urlaub am Meer",
            "hero_alt": "Ano Syros und Ermoupoli über dem Hafen",
            "hero_caption": "Ano Syros und Ermoupoli über dem Hafen. Foto: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).",
        },
        "it": {
            "title": "Dove dormire a Syros: Ermoupoli, Kini–Delfini, Galissas e il sud",
            "description": "Confrontate le zone di soggiorno a Syros — Ermoupoli, costa ovest di Kini e Delfini, Galissas e sud — per spiagge quiete, serate o una settimana in villa.",
            "keywords": "dove dormire Syros, alloggi Syros zone, Kini o Ermoupoli, spiaggia Delfini, Galissas Syros",
            "kicker": "Articoli · Syros e soggiorni al mare",
            "hero_alt": "Ano Syros ed Ermoupoli sopra il porto",
            "hero_caption": "Ano Syros ed Ermoupoli sopra il porto. Foto: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).",
        },
        "he": {
            "title": "איפה לישון בסירוס: ארמופולי, קיני–דלפיני, גליסאס והדרום",
            "description": "השוו אזורי לינה בסירוס — ארמופולי, החוף המערבי של קיני ודלפיני, גליסאס והדרום — לחוף שקט, ערב בעיר או שבוע בווילה.",
            "keywords": "איפה לישון סירוס, לינה סירוס אזורים, קיני או ארמופולי, חוף דלפיני, גליסאס סירוס",
            "kicker": "מאמרים · סירוס ולינה ליד הים",
            "hero_alt": "אנו סירוס וארמופולי מעל הנמל",
            "hero_caption": "אנו סירוס וארמופולי מעל הנמל. צילום: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).",
        },
    },
    "seven-day-syros-itinerary-villa-base": {
        "el": {
            "title": "Πρόγραμμα 7 ημερών στη Σύρο από βίλα στη δυτική ακτή",
            "description": "Πρακτική εβδομάδα στη Σύρο με βάση κοντά στο Δελφίνι–Κίνι: παραλίες, Ερμούπολη, Άνω Σύρος, φαγητό, μέρες ξεκούρασης και πότε αφήνετε το αυτοκίνητο.",
            "keywords": "προγραμμα 7 ημερων Συρος, itinerary Συρος, διακοπες βιλα Συρος, Δελφινι Κινι",
            "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα",
            "hero_alt": "Πολυθρόνες στη βεράντα του Sea View Serenity στο ηλιοβασίλεμα",
            "hero_caption": "Βράδυ στη βεράντα του Sea View Serenity: η παύση ανάμεσα στις μέρες του νησιού.",
        },
        "fr": {
            "title": "Itinéraire 7 jours à Syros depuis une villa sur la côte ouest",
            "description": "Une semaine concrète à Syros depuis une base près de Delfini–Kini : plages, Ermoupoli, Ano Syros, repas, jours calmes et quand laisser la voiture.",
            "keywords": "itinéraire 7 jours Syros, semaine Syros villa, programme Syros, Delfini Kini",
            "kicker": "Articles · Syros et séjours en bord de mer",
            "hero_alt": "Chaises longues sur la terrasse de Sea View Serenity au coucher du soleil",
            "hero_caption": "Soirée en terrasse à Sea View Serenity : la pause entre les journées d’île.",
        },
        "de": {
            "title": "7-Tage-Syros-Itinerar von einer Villa an der Westküste",
            "description": "Eine praktische Woche auf Syros mit Basis bei Delfini–Kini: Strände, Ermoupoli, Ano Syros, Essen, Ruhetage und wann das Auto stehen bleibt.",
            "keywords": "7 Tage Syros, Syros Itinerar, Villa Urlaub Syros, Delfini Kini",
            "kicker": "Artikel · Syros & Urlaub am Meer",
            "hero_alt": "Liegestühle auf der Terrasse von Sea View Serenity bei Sonnenuntergang",
            "hero_caption": "Terrassenabend im Sea View Serenity: die Pause zwischen Insel-Tagen.",
        },
        "it": {
            "title": "Itinerario di 7 giorni a Syros da una villa sulla costa ovest",
            "description": "Una settimana pratica a Syros con base vicino a Delfini–Kini: spiagge, Ermoupoli, Ano Syros, cibo, giorni di riposo e quando lasciare l’auto.",
            "keywords": "itinerario 7 giorni Syros, settimana Syros villa, programma Syros, Delfini Kini",
            "kicker": "Articoli · Syros e soggiorni al mare",
            "hero_alt": "Sedie sulla terrazza di Sea View Serenity al tramonto",
            "hero_caption": "Sera in terrazza a Sea View Serenity: la pausa tra i giorni sull’isola.",
        },
        "he": {
            "title": "מסלול 7 ימים בסירוס מבסיס וילה בחוף המערבי",
            "description": "שבוע מעשי בסירוס מבסיס ליד דלפיני–קיני: חופים, ארמופולי, אנו סירוס, אוכל, ימי מנוחה ומתי להשאיר את הרכב.",
            "keywords": "מסלול 7 ימים סירוס, איטינררי סירוס, חופשת וילה סירוס, דלפיני קיני",
            "kicker": "מאמרים · סירוס ולינה ליד הים",
            "hero_alt": "כיסאות במרפסת Sea View Serenity בשקיעה",
            "hero_caption": "ערב במרפסת Sea View Serenity: הפסקה בין ימי האי.",
        },
    },
    "getting-around-syros-car-rental-bus": {
        "el": {
            "title": "Μετακινήσεις στη Σύρο: ενοικίαση αυτοκινήτου, λεωφορεία, ταξί",
            "description": "Πώς κινείστε στη Σύρο από τη δυτική ακτή: πότε αξίζει αυτοκίνητο, τι καλύπτουν λεωφορεία και ταξί, και πώς δένει το λιμάνι με μια βίλα στο Δελφίνι–Κίνι.",
            "keywords": "ενοικιαση αυτοκινητου Συρος, μετακινησεις Συρος, λεωφορειο Συρος, ταξι Συρος",
            "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα",
            "hero_alt": "Πλοίο στο λιμάνι της Σύρου",
            "hero_caption": "Πλοίο στο λιμάνι της Σύρου — η άφιξη είναι το εύκολο μέρος. Φωτογραφία: Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).",
        },
        "fr": {
            "title": "Se déplacer à Syros : location de voiture, bus et taxis",
            "description": "Comment circuler à Syros depuis la côte ouest : quand louer une voiture, ce que couvrent bus et taxis, et la logistique du port pour une villa à Delfini–Kini.",
            "keywords": "location voiture Syros, se déplacer Syros, bus Syros, taxi Syros",
            "kicker": "Articles · Syros et séjours en bord de mer",
            "hero_alt": "Ferry dans le port de Syros",
            "hero_caption": "Ferry dans le port de Syros — l’arrivée est la partie facile. Photo : Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).",
        },
        "de": {
            "title": "Unterwegs auf Syros: Mietwagen, Bus und Taxi",
            "description": "Mobilität auf Syros von der Westküste aus: wann sich ein Mietwagen lohnt, was Bus und Taxi abdecken, und wie der Fährhafen zu einer Villa bei Delfini–Kini passt.",
            "keywords": "Mietwagen Syros, Verkehr Syros, Bus Syros, Taxi Syros",
            "kicker": "Artikel · Syros & Urlaub am Meer",
            "hero_alt": "Fähre im Hafen von Syros",
            "hero_caption": "Fähre im Hafen von Syros — die Ankunft ist der einfache Teil. Foto: Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).",
        },
        "it": {
            "title": "Muoversi a Syros: noleggio auto, autobus e taxi",
            "description": "Come spostarsi a Syros dalla costa ovest: quando conviene l’auto, cosa coprono bus e taxi, e la logistica del porto per una villa a Delfini–Kini.",
            "keywords": "noleggio auto Syros, muoversi Syros, autobus Syros, taxi Syros",
            "kicker": "Articoli · Syros e soggiorni al mare",
            "hero_alt": "Traghetto nel porto di Syros",
            "hero_caption": "Traghetto nel porto di Syros — arrivare è la parte facile. Foto: Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).",
        },
        "he": {
            "title": "תחבורה בסירוס: השכרת רכב, אוטובוסים ומוניות",
            "description": "איך מתניידים בסירוס מהחוף המערבי: מתי שווה רכב, מה מכסים אוטובוס ומונית, ואיך הנמל מתחבר לווילה ליד דלפיני–קיני.",
            "keywords": "השכרת רכב סירוס, תחבורה סירוס, אוטובוס סירוס, מונית סירוס",
            "kicker": "מאמרים · סירוס ולינה ליד הים",
            "hero_alt": "מעבורת בנמל סירוס",
            "hero_caption": "מעבורת בנמל סירוס — ההגעה היא החלק הקל. צילום: Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).",
        },
    },
    "kini-restaurants-sunset-dining": {
        "el": {
            "title": "Εστιατόρια στο Κίνι και δείπνο στο ηλιοβασίλεμα στη δυτική Σύρο",
            "description": "Πώς να σχεδιάσετε δείπνα στο ηλιοβασίλεμα στο Κίνι, με το Δελφίνι ως ήσυχη βάση για μπάνιο: ταβέρνες, timing και πότε αξίζει Ερμούπολη.",
            "keywords": "εστιατορια Κινι, δειπνο ηλιοβασιλεμα Συρος, ταβερνες δυτικη Συρος, Δελφινι",
            "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα",
            "hero_alt": "Ηλιοβασίλεμα πάνω από τη θάλασσα στο Κίνι",
            "hero_caption": "Ηλιοβασίλεμα στο Κίνι — το δείπνο της δυτικής ακτής. Φωτογραφία: ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
        },
        "fr": {
            "title": "Restaurants à Kini et dîners au coucher du soleil sur la côte ouest",
            "description": "Comment organiser les dîners au coucher du soleil à Kini, avec Delfini comme base baignade calme : tavernes, timing, et quand filer à Ermoupoli.",
            "keywords": "restaurants Kini, dîner coucher soleil Syros, tavernes côte ouest, Delfini",
            "kicker": "Articles · Syros et séjours en bord de mer",
            "hero_alt": "Coucher de soleil sur la mer à Kini",
            "hero_caption": "Coucher de soleil à Kini — le théâtre du dîner sur la côte ouest. Photo : ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
        },
        "de": {
            "title": "Restaurants in Kini und Sonnenuntergangs-Dinner an der Westküste",
            "description": "Sonnenuntergangs-Dinner in Kini planen, mit Delfini als ruhiger Schwimmbasis: Tavernen, Timing und wann Ermoupoli die bessere Wahl ist.",
            "keywords": "Restaurants Kini, Sonnenuntergang Dinner Syros, Tavernen Westküste, Delfini",
            "kicker": "Artikel · Syros & Urlaub am Meer",
            "hero_alt": "Sonnenuntergang über dem Meer in Kini",
            "hero_caption": "Sonnenuntergang in Kini — Dinner-Theater der Westküste. Foto: ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
        },
        "it": {
            "title": "Ristoranti a Kini e cene al tramonto sulla costa ovest di Syros",
            "description": "Come pianificare cene al tramonto a Kini, con Delfini come base quieta per il bagno: taverne, orari e quando conviene Ermoupoli.",
            "keywords": "ristoranti Kini, cena tramonto Syros, taverne costa ovest, Delfini",
            "kicker": "Articoli · Syros e soggiorni al mare",
            "hero_alt": "Tramonto sul mare a Kini",
            "hero_caption": "Tramonto a Kini — il teatro della cena sulla costa ovest. Foto: ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
        },
        "he": {
            "title": "מסעדות בקיני וארוחת ערב בשקיעה בחוף המערבי",
            "description": "איך לתכנן ארוחות ערב בשקיעה בקיני, עם דלפיני כבסיס שחייה שקט: טברנות, תזמון ומתי ארמופולי עדיפה.",
            "keywords": "מסעדות קיני, ארוחת ערב שקיעה סירוס, טברנות חוף מערבי, דלפיני",
            "kicker": "מאמרים · סירוס ולינה ליד הים",
            "hero_alt": "שקיעה מעל הים בקיני",
            "hero_caption": "שקיעה בקיני — תיאטרון ארוחת הערב של החוף המערבי. צילום: ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
        },
    },
    "syros-in-may-june-september": {
        "el": {
            "title": "Σύρος Μάιο, Ιούνιο και Σεπτέμβριο: γιατί η ενδιάμεση σεζόν ταιριάζει στη βίλα",
            "description": "Γιατί Μάιος, Ιούνιος και Σεπτέμβριος συχνά είναι το γλυκό σημείο για διακοπές σε βίλα στη Σύρο: θάλασσα, κόσμος, ακτοπλοΐα και δυτικά βράδια χωρίς πίεση Αυγούστου.",
            "keywords": "Συρος Μαιο, Συρος Ιουνιο, Συρος Σεπτεμβριο, καλυτερη εποχη Συρος, shoulder season Κυκλαδες",
            "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα",
            "hero_alt": "Υπνοδωμάτιο με ανοιχτά παντζούρια προς μπουκαμβίλια και θάλασσα",
            "hero_caption": "Φως ενδιάμεσης σεζόν από ανοιχτά παντζούρια στο Sea View Serenity.",
        },
        "fr": {
            "title": "Syros en mai, juin et septembre : pourquoi l’intersaison convient à la villa",
            "description": "Pourquoi mai, juin et septembre sont souvent le sweet spot pour une villa à Syros : mer, fréquentation, ferries et soirées ouest sans la pression d’août.",
            "keywords": "Syros en mai, Syros en juin, Syros en septembre, meilleure période Syros, intersaison Cyclades",
            "kicker": "Articles · Syros et séjours en bord de mer",
            "hero_alt": "Chambre avec volets ouverts sur bougainvillier et mer",
            "hero_caption": "Lumière d’intersaison à travers les volets ouverts à Sea View Serenity.",
        },
        "de": {
            "title": "Syros im Mai, Juni und September: Warum die Nebensaison zur Villa passt",
            "description": "Warum Mai, Juni und September oft das Beste für eine Villa auf Syros sind: Meer, Andrang, Fähren und Westküstenabende ohne August-Druck.",
            "keywords": "Syros im Mai, Syros im Juni, Syros im September, beste Reisezeit Syros, Nebensaison Kykladen",
            "kicker": "Artikel · Syros & Urlaub am Meer",
            "hero_alt": "Schlafzimmer mit offenen Fensterläden zu Bougainvillea und Meer",
            "hero_caption": "Nebensaison-Licht durch offene Fensterläden im Sea View Serenity.",
        },
        "it": {
            "title": "Syros a maggio, giugno e settembre: perché la mezza stagione è ideale in villa",
            "description": "Perché maggio, giugno e settembre sono spesso il momento giusto per una villa a Syros: mare, folla, traghetti e sere a ovest senza la pressione di agosto.",
            "keywords": "Syros a maggio, Syros a giugno, Syros a settembre, periodo migliore Syros, mezza stagione Cicladi",
            "kicker": "Articoli · Syros e soggiorni al mare",
            "hero_alt": "Camera con persiane aperte su buganvillea e mare",
            "hero_caption": "Luce di mezza stagione dalle persiane aperte a Sea View Serenity.",
        },
        "he": {
            "title": "סירוס במאי, יוני וספטמבר: למה עונת הביניים מתאימה לווילה",
            "description": "למה מאי, יוני וספטמבר הם לעתים קרובות הנקודה המתוקה לחופשת וילה בסירוס: ים, קהל, מעבורות וערבים במערב בלי לחץ אוגוסט.",
            "keywords": "סירוס במאי, סירוס ביוני, סירוס בספטמבר, הזמן הטוב לסירוס, עונת ביניים קיקלדים",
            "kicker": "מאמרים · סירוס ולינה ליד הים",
            "hero_alt": "חדר שינה עם תריסים פתוחים לבוגנוויליה ולים",
            "hero_caption": "אור של עונת ביניים דרך תריסים פתוחים ב-Sea View Serenity.",
        },
    },
}

# Continue remaining slugs in compact form via second dict merge below
MORE = json.loads(r'''
{
  "things-to-do-on-syros": {
    "el": {"title": "Τι να κάνετε στη Σύρο: παραλίες, Ερμούπολη, φαγητό και απλά πλάνα", "description": "Πρακτικός οδηγός για δραστηριότητες στη Σύρο — δυτικές παραλίες, Ερμούπολη και Άνω Σύρος, φαγητό και απλά ημερήσια πλάνα από παραθαλάσσια βίλα.", "keywords": "τι να κανετε Συρος, αξιοθεατα Συρος, παραλιες Συρος, Ερμουπολη", "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα", "hero_alt": "Πανοραμική θέα της Ερμούπολης στη Σύρο", "hero_caption": "Ερμούπολη: η λίστα αρχίζει από μια πραγματική πόλη. Φωτογραφία: Zacharias Mitzelos / Wikimedia Commons (CC0)."},
    "fr": {"title": "Que faire à Syros : plages, Ermoupoli, cuisine et journées simples", "description": "Guide pratique des activités à Syros — plages de l’ouest, Ermoupoli et Ano Syros, nourriture et journées simples depuis une villa en bord de mer.", "keywords": "que faire à Syros, activités Syros, plages Syros, Ermoupoli", "kicker": "Articles · Syros et séjours en bord de mer", "hero_alt": "Vue panoramique d’Ermoupoli à Syros", "hero_caption": "Ermoupoli : la to-do list commence par une vraie ville. Photo : Zacharias Mitzelos / Wikimedia Commons (CC0)."},
    "de": {"title": "Aktivitäten auf Syros: Strände, Ermoupoli, Essen und einfache Tagespläne", "description": "Praktischer Überblick über Dinge, die man auf Syros tun kann — Westküstenstrände, Ermoupoli und Ano Syros, Essen und einfache Tage von einer Strandvilla aus.", "keywords": "Aktivitäten Syros, Sehenswürdigkeiten Syros, Strände Syros, Ermoupoli", "kicker": "Artikel · Syros & Urlaub am Meer", "hero_alt": "Panoramablick auf Ermoupoli auf Syros", "hero_caption": "Ermoupoli: Die To-do-Liste beginnt mit einer echten Stadt. Foto: Zacharias Mitzelos / Wikimedia Commons (CC0)."},
    "it": {"title": "Cosa fare a Syros: spiagge, Ermoupoli, cibo e giornate semplici", "description": "Guida pratica alle cose da fare a Syros — spiagge ovest, Ermoupoli e Ano Syros, cibo e giornate semplici da una villa sul mare.", "keywords": "cosa fare a Syros, attività Syros, spiagge Syros, Ermoupoli", "kicker": "Articoli · Syros e soggiorni al mare", "hero_alt": "Vista panoramica di Ermoupoli a Syros", "hero_caption": "Ermoupoli: la lista inizia con una vera città. Foto: Zacharias Mitzelos / Wikimedia Commons (CC0)."},
    "he": {"title": "מה לעשות בסירוס: חופים, ארמופולי, אוכל ותוכניות פשוטות", "description": "מדריך מעשי לפעילויות בסירוס — חופי המערב, ארמופולי ואנו סירוס, אוכל וימי טיול פשוטים מבסיס וילה ליד הים.", "keywords": "מה לעשות בסירוס, אטרקציות סירוס, חופים סירוס, ארמופולי", "kicker": "מאמרים · סירוס ולינה ליד הים", "hero_alt": "נוף פנורמי של ארמופולי בסירוס", "hero_caption": "ארמופולי: הרשימה מתחילה בעיר אמיתית. צילום: Zacharias Mitzelos / Wikimedia Commons (CC0)."}
  },
  "ano-syros-ermoupoli-walking-guide": {
    "el": {"title": "Περπάτημα σε Άνω Σύρο και Ερμούπολη: δύο πόλεις, ένα νησί-πρωτεύουσα", "description": "Οδηγός πεζοπορίας στην Ερμούπολη και την Άνω Σύρο: νεοκλασικοί δρόμοι, λιμάνι, σοκάκια, θέες και πώς να συνδυάσετε μέρα στην πόλη με βίλα στη δύση.", "keywords": "Ανω Συρος περπατημα, Ερμουπολη οδηγος, παλια πολη Συρος", "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα", "hero_alt": "Θέα της Ερμούπολης από την Άνω Σύρο", "hero_caption": "Ερμούπολη από την Άνω Σύρο — περπατήστε και τις δύο στρώσεις της πρωτεύουσας. Φωτογραφία: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0)."},
    "fr": {"title": "Balade à Ano Syros et Ermoupoli : deux villes, une île-capitale", "description": "Guide de marche à Ermoupoli et Ano Syros : rues néoclassiques, port, ruelles, points de vue, et comment coupler une journée en ville avec une villa à l’ouest.", "keywords": "Ano Syros balade, guide Ermoupoli, vieille ville Syros", "kicker": "Articles · Syros et séjours en bord de mer", "hero_alt": "Vue d’Ermoupoli depuis Ano Syros", "hero_caption": "Ermoupoli depuis Ano Syros — marchez les deux couches de la capitale. Photo : NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0)."},
    "de": {"title": "Spaziergang durch Ano Syros und Ermoupoli: zwei Städte, eine Inselhauptstadt", "description": "Wanderführer für Ermoupoli und Ano Syros: klassizistische Straßen, Hafen, Gassen, Aussichten — und wie ein Stadttag zur Westküsten-Villa passt.", "keywords": "Ano Syros Spaziergang, Ermoupoli Guide, Altstadt Syros", "kicker": "Artikel · Syros & Urlaub am Meer", "hero_alt": "Blick auf Ermoupoli von Ano Syros", "hero_caption": "Ermoupoli von Ano Syros — gehen Sie beide Schichten der Hauptstadt. Foto: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0)."},
    "it": {"title": "Camminata ad Ano Syros ed Ermoupoli: due città, un’isola capitale", "description": "Guida a piedi di Ermoupoli e Ano Syros: strade neoclassiche, porto, vicoli, viste, e come abbinare un giorno in città a una villa sulla costa ovest.", "keywords": "Ano Syros camminata, guida Ermoupoli, centro storico Syros", "kicker": "Articoli · Syros e soggiorni al mare", "hero_alt": "Vista di Ermoupoli da Ano Syros", "hero_caption": "Ermoupoli da Ano Syros — camminate entrambi i livelli della capitale. Foto: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0)."},
    "he": {"title": "הליכה באנו סירוס ובארמופולי: שתי ערים, אי-בירה אחד", "description": "מדריך הליכה בארמופולי ובאנו סירוס: רחובות ניאו-קלאסיים, נמל, סמטאות, תצפיות, ואיך לחבר יום בעיר לווילה במערב.", "keywords": "אנו סירוס הליכה, מדריך ארמופולי, עיר עתיקה סירוס", "kicker": "מאמרים · סירוס ולינה ליד הים", "hero_alt": "נוף לארמופולי מאנו סירוס", "hero_caption": "ארמופולי מאנו סירוס — לכו בשני השכבות של הבירה. צילום: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0)."}
  },
  "day-trips-from-syros-tinos-mykonos": {
    "el": {"title": "Ημερήσιες εκδρομές από Σύρο σε Τήνο και Μύκονο (και γιατί η Σύρος είναι καλύτερη βάση)", "description": "Πώς να χρησιμοποιήσετε τη Σύρο ως ήρεμη βάση στις Κυκλάδες για ημερήσια πλοία προς Τήνο ή Μύκονο — timing και γιατί μετράει η επιστροφή σε ήσυχη δυτική βίλα.", "keywords": "εκδρομες απο Συρο, Συρος Τηνος πλοιο, Συρος Μυκονος ημερησια", "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα", "hero_alt": "Ηλιοβασίλεμα πάνω στη Σύρο από το λιμάνι της Τήνου", "hero_caption": "Η Σύρος στον ορίζοντα από την Τήνο — αρκετά κοντά για μια μέρα. Φωτογραφία: Jules Verne Times Two / Wikimedia Commons (CC BY-SA 4.0)."},
    "fr": {"title": "Excursions d’une journée depuis Syros vers Tinos et Mykonos", "description": "Utiliser Syros comme base calme des Cyclades pour des allers-retours en ferry vers Tinos ou Mykonos — timing, et pourquoi rentrer dans une villa ouest compte.", "keywords": "excursion Syros Tinos, ferry Syros Mykonos, day trip Cyclades", "kicker": "Articles · Syros et séjours en bord de mer", "hero_alt": "Coucher de soleil sur Syros vu depuis le port de Tinos", "hero_caption": "Syros à l’horizon depuis Tinos — assez proche pour une journée. Photo : Jules Verne Times Two / Wikimedia Commons (CC BY-SA 4.0)."},
    "de": {"title": "Tagesausflüge von Syros nach Tinos und Mykonos", "description": "Syros als ruhige Kykladen-Basis für Fähr-Tagestrips nach Tinos oder Mykonos nutzen — Timing und warum die Rückkehr in eine Westküsten-Villa zählt.", "keywords": "Tagesausflug Syros Tinos, Fähre Syros Mykonos, Island hopping Basis", "kicker": "Artikel · Syros & Urlaub am Meer", "hero_alt": "Sonnenuntergang über Syros vom Hafen von Tinos", "hero_caption": "Syros am Horizont von Tinos — nah genug für einen Tag. Foto: Jules Verne Times Two / Wikimedia Commons (CC BY-SA 4.0)."},
    "it": {"title": "Gite di un giorno da Syros a Tinos e Mykonos", "description": "Usare Syros come base tranquilla delle Cicladi per traghetti giornalieri verso Tinos o Mykonos — orari e perché tornare in una villa a ovest conta.", "keywords": "gita Syros Tinos, traghetto Syros Mykonos, day trip Cicladi", "kicker": "Articoli · Syros e soggiorni al mare", "hero_alt": "Tramonto su Syros visto dal porto di Tinos", "hero_caption": "Syros all’orizzonte da Tinos — abbastanza vicina per un giorno. Foto: Jules Verne Times Two / Wikimedia Commons (CC BY-SA 4.0)."},
    "he": {"title": "טיולי יום מסירוס לטינוס ולמיקונוס (ולמה סירוס היא בסיס טוב יותר)", "description": "איך להשתמש בסירוס כבסיס רגוע בקיקלדים לטיולי מעבורת לטינוס או מיקונוס — תזמון ולמה חשוב לחזור לווילה שקטה במערב.", "keywords": "טיול יום סירוס טינוס, מעבורת סירוס מיקונוס, בסיס קיקלדים", "kicker": "מאמרים · סירוס ולינה ליד הים", "hero_alt": "שקיעה מעל סירוס מנמל טינוס", "hero_caption": "סירוס באופק מטינוס — קרובה מספיק ליום אחד. צילום: Jules Verne Times Two / Wikimedia Commons (CC BY-SA 4.0)."}
  },
  "pet-friendly-syros-villa-stay": {
    "el": {"title": "Διαμονή στη Σύρο με κατοικίδιο: τι να ρωτήσετε πριν φέρετε τον σκύλο", "description": "Πρακτικός οδηγός για ταξίδι στη Σύρο με σκύλο: κανόνες βίλας, παραλίες, ζέστη, μεταφορές και πώς να σχεδιάσετε ήσυχη δυτική διαμονή.", "keywords": "κατοικιδιο Συρος, σκυλος Συρος βιλα, pet friendly Συρος", "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα", "hero_alt": "Βεράντα στο Sea View Serenity με θέα στη θάλασσα", "hero_caption": "Ήσυχη βεράντα βοηθά κατοικίδια και ανθρώπους μετά τις μέρες στο νησί."},
    "fr": {"title": "Villa à Syros avec animal : que demander avant d’amener le chien", "description": "Conseils pratiques pour voyager à Syros avec un chien : règles de villa, plages, chaleur, transport, et séjour calme sur la côte ouest.", "keywords": "chien Syros, villa pet friendly Syros, animal de compagnie Cyclades", "kicker": "Articles · Syros et séjours en bord de mer", "hero_alt": "Terrasse de Sea View Serenity face à la mer", "hero_caption": "Une terrasse calme aide chiens et humains après les journées d’île."},
    "de": {"title": "Haustierfreundliche Villa auf Syros: Was Sie vor der Anreise klären sollten", "description": "Praktische Tipps für Syros mit Hund: Villa-Regeln, Strände, Hitze, Anreise und wie ein ruhiger Westküsten-Aufenthalt gelingt.", "keywords": "Hund Syros, pet friendly Villa Syros, Haustier Kykladen", "kicker": "Artikel · Syros & Urlaub am Meer", "hero_alt": "Terrasse im Sea View Serenity mit Meerblick", "hero_caption": "Eine ruhige Terrasse hilft Hund und Mensch nach Inseltagen."},
    "it": {"title": "Villa a Syros con cane: cosa chiedere prima di arrivare", "description": "Guida pratica per Syros con cane: regole della villa, spiagge, caldo, trasporti e come pianificare un soggiorno quieto sulla costa ovest.", "keywords": "cane Syros, villa pet friendly Syros, animali Cicladi", "kicker": "Articoli · Syros e soggiorni al mare", "hero_alt": "Terrazza di Sea View Serenity sul mare", "hero_caption": "Una terrazza quieta aiuta cani e persone dopo le giornate sull’isola."},
    "he": {"title": "וילה ידידותית לחיות מחמד בסירוס: מה לשאול לפני שמביאים את הכלב", "description": "הדרכה מעשית לביקור בסירוס עם כלב: כללי וילה, חופים, חום, תחבורה ואיך לתכנן שהייה רגועה במערב.", "keywords": "כלב סירוס, וילה ידידותית לחיות מחמד, pet friendly סירוס", "kicker": "מאמרים · סירוס ולינה ליד הים", "hero_alt": "מרפסת Sea View Serenity מול הים", "hero_caption": "מרפסת שקטה עוזרת לכלבים ולאנשים אחרי ימי האי."}
  },
  "packing-meltemi-wind-guide-syros": {
    "el": {"title": "Τι να πάρετε στη Σύρο και το μελτέμι: άνεμος, στρώσεις και παραλίες plan B", "description": "Οδηγός αποσκευών για Σύρο σε περίοδο μελτεμιού: ρούχα για άνεμο, κιτ παραλίας και πώς αλλάζετε ακτή όταν η δύση ταράζεται.", "keywords": "μελτεμι Συρος, τι να πακεταρω Συρος, ανεμος Κυκλαδες", "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα", "hero_alt": "Ουρανός ηλιοβασιλέματος πάνω από το Κίνι", "hero_caption": "Όμορφο δυτικό φως μπορεί να έρθει με αέρα — πακετάρετε και για τα δύο. Φωτογραφία: ERWEH / Wikimedia Commons (CC BY-SA 2.5)."},
    "fr": {"title": "Que mettre dans la valise pour Syros et le meltem : vent, couches et plages plan B", "description": "Que emporter à Syros en saison de meltem : vêtements anti-vent, kit plage, et comment changer de côte quand l’ouest devient agité.", "keywords": "meltem Syros, valise Syros, vent Cyclades, plage plan B", "kicker": "Articles · Syros et séjours en bord de mer", "hero_alt": "Ciel de coucher de soleil au-dessus de Kini", "hero_caption": "La belle lumière ouest peut arriver avec du vent — prévoyez les deux. Photo : ERWEH / Wikimedia Commons (CC BY-SA 2.5)."},
    "de": {"title": "Packliste Syros und Meltemi: Wind, Schichten und Plan-B-Strände", "description": "Was Sie für Syros in der Meltemi-Zeit einpacken: windfeste Kleidung, Strandkit und wie Sie die Küste wechseln, wenn der Westen unruhig wird.", "keywords": "Meltemi Syros, Packliste Syros, Wind Kykladen, Strand Plan B", "kicker": "Artikel · Syros & Urlaub am Meer", "hero_alt": "Sonnenuntergangshimmel über Kini", "hero_caption": "Schönes Westlicht kann mit Wind kommen — packen Sie für beides. Foto: ERWEH / Wikimedia Commons (CC BY-SA 2.5)."},
    "it": {"title": "Cosa mettere in valigia per Syros e il meltemi: vento, strati e spiagge plan B", "description": "Cosa portare a Syros in stagione di meltemi: abiti antivento, kit spiaggia e come cambiare costa quando l’ovest si agita.", "keywords": "meltemi Syros, valigia Syros, vento Cicladi, spiaggia plan B", "kicker": "Articoli · Syros e soggiorni al mare", "hero_alt": "Cielo al tramonto sopra Kini", "hero_caption": "La bella luce ovest può arrivare col vento — preparate entrambi. Foto: ERWEH / Wikimedia Commons (CC BY-SA 2.5)."},
    "he": {"title": "מה לארוז לסירוס ולמלטמי: רוח, שכבות וחופי תוכנית ב'", "description": "מדריך אריזה לסירוס בעונת המלטמי: בגדים לרוח, ערכת חוף ואיך מחליפים חוף כשהמערב מתנחש.", "keywords": "מלטמי סירוס, מה לארוז סירוס, רוח קיקלדים", "kicker": "מאמרים · סירוס ולינה ליד הים", "hero_alt": "שמי שקיעה מעל קיני", "hero_caption": "אור מערבי יפה יכול להגיע עם רוח — ארזו לשניהם. צילום: ERWEH / Wikimedia Commons (CC BY-SA 2.5)."}
  },
  "grocery-self-catering-delfini-kini": {
    "el": {"title": "Αυτοεξυπηρέτηση κοντά σε Δελφίνι και Κίνι: ψώνια, φούρνοι και μαγείρεμα στη βίλα", "description": "Πώς να μαγειρεύετε από βίλα στη δυτική Σύρο κοντά στο Δελφίνι και το Κίνι: πού ψωνίζετε, τι μαγειρεύετε και πώς μπαίνει η Ερμούπολη στο πρόγραμμα.", "keywords": "ψωνια Συρος, αυτοεξυπηρετηση Συρος, φουρνος Κινι, μαγειρεμα βιλα", "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα", "hero_alt": "Κουζίνα στο Sea View Serenity", "hero_caption": "Πλήρης κουζίνα βίλας μετατρέπει τα ψώνια της Σύρου σε εύκολα γεύματα στη βεράντα."},
    "fr": {"title": "En autonomie près de Delfini et Kini : courses, boulangeries et cuisine en villa", "description": "Comment cuisiner depuis une villa sur la côte ouest près de Delfini et Kini : où faire les courses, que cuisiner, et le rôle d’Ermoupoli.", "keywords": "courses Syros, self catering Syros, boulangerie Kini, cuisine villa", "kicker": "Articles · Syros et séjours en bord de mer", "hero_alt": "Cuisine de Sea View Serenity", "hero_caption": "Une cuisine de villa complète transforme les courses en repas faciles en terrasse."},
    "de": {"title": "Selbstversorgung bei Delfini und Kini: Einkaufen, Bäckereien und Villa-Küche", "description": "Kochen von einer Westküsten-Villa bei Delfini und Kini: wo einkaufen, was kochen, und wie Ermoupoli in den Wochenplan passt.", "keywords": "Einkaufen Syros, Selbstversorgung Syros, Bäckerei Kini, Villa Küche", "kicker": "Artikel · Syros & Urlaub am Meer", "hero_alt": "Küche im Sea View Serenity", "hero_caption": "Eine voll ausgestattete Villa-Küche macht aus dem Einkauf leichte Terrassenmahlzeiten."},
    "it": {"title": "Self-catering vicino a Delfini e Kini: spesa, panifici e cucina in villa", "description": "Come cucinare da una villa sulla costa ovest vicino a Delfini e Kini: dove fare la spesa, cosa cucinare e il ruolo di Ermoupoli.", "keywords": "spesa Syros, self catering Syros, panificio Kini, cucina villa", "kicker": "Articoli · Syros e soggiorni al mare", "hero_alt": "Cucina di Sea View Serenity", "hero_caption": "Una cucina completa trasforma la spesa in pasti facili in terrazza."},
    "he": {"title": "לינה עם מטבח ליד דלפיני וקיני: קניות, מאפיות ובישול בווילה", "description": "איך לבשל מווילה בחוף המערבי ליד דלפיני וקיני: איפה לקנות, מה לבשל ואיך ארמופולי נכנסת לתוכנית.", "keywords": "קניות סירוס, self catering סירוס, מאפייה קיני, בישול בווילה", "kicker": "מאמרים · סירוס ולינה ליד הים", "hero_alt": "המטבח ב-Sea View Serenity", "hero_caption": "מטבח וילה מלא הופך את הקניות לארוחות קלות במרפסת."}
  },
  "winter-year-round-syros": {
    "el": {"title": "Σύρος όλο τον χρόνο: γιατί το νησί-πρωτεύουσα δουλεύει και εκτός καλοκαιριού", "description": "Γιατί η Σύρος μένει ενδιαφέρουσα εκτός αιχμής: ζωή στην Ερμούπολη, πραγματικότητες χειμώνα και ενδιάμεσης σεζόν, και πώς προσαρμόζεται ένα δυτικό σπίτι όταν λιγοστεύουν οι μέρες παραλίας.", "keywords": "Συρος χειμωνας, Συρος ολο τον χρονο, Ερμουπολη εκτος σεζον", "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα", "hero_alt": "Σαλόνι με πέτρινο τζάκι στο Sea View Serenity", "hero_caption": "Εποχή τζακιού: η Σύρος ως πρωτεύουσα όλο τον χρόνο, όχι μόνο στάση παραλίας."},
    "fr": {"title": "Syros toute l’année : pourquoi l’île-capitale fonctionne hors été", "description": "Pourquoi Syros reste intéressante hors saison : vie à Ermoupoli, réalités d’hiver et d’intersaison, et comment une maison ouest s’adapte quand les jours de plage raccourcissent.", "keywords": "Syros en hiver, Syros toute l’année, Ermoupoli hors saison", "kicker": "Articles · Syros et séjours en bord de mer", "hero_alt": "Salon avec cheminée en pierre à Sea View Serenity", "hero_caption": "Saison cheminée : Syros comme capitale toute l’année, pas seulement une halte plage."},
    "de": {"title": "Syros das ganze Jahr: Warum die Inselhauptstadt auch außerhalb des Sommers funktioniert", "description": "Warum Syros außerhalb der Hochsaison interessant bleibt: Leben in Ermoupoli, Winter- und Nebensaison, und wie ein Westküstenhaus sich anpasst, wenn Badetage weniger werden.", "keywords": "Syros im Winter, Syros ganzjährig, Ermoupoli Nebensaison", "kicker": "Artikel · Syros & Urlaub am Meer", "hero_alt": "Wohnzimmer mit Steinkamin im Sea View Serenity", "hero_caption": "Kaminsaison: Syros als ganzjährige Hauptinsel, nicht nur Strandstopp."},
    "it": {"title": "Syros tutto l’anno: perché l’isola-capitale funziona anche fuori estate", "description": "Perché Syros resta interessante fuori stagione: vita a Ermoupoli, realtà di inverno e mezza stagione, e come una casa a ovest si adatta quando i giorni di spiaggia diminuiscono.", "keywords": "Syros in inverno, Syros tutto l’anno, Ermoupoli fuori stagione", "kicker": "Articoli · Syros e soggiorni al mare", "hero_alt": "Soggiorno con camino in pietra a Sea View Serenity", "hero_caption": "Stagione del camino: Syros come capitale tutto l’anno, non solo sosta spiaggia."},
    "he": {"title": "סירוס כל השנה: למה אי-הבירה עובד גם מחוץ לקיץ", "description": "למה סירוס נשארת מעניינת מחוץ לשיא: חיים בארמופולי, מציאות חורף ועונת ביניים, ואיך בית במערב מסתגל כשימי החוף מתקצרים.", "keywords": "סירוס בחורף, סירוס כל השנה, ארמופולי מחוץ לעונה", "kicker": "מאמרים · סירוס ולינה ליד הים", "hero_alt": "סלון עם אח אבן ב-Sea View Serenity", "hero_caption": "עונת האח: סירוס כבירה כל השנה, לא רק עצירת חוף."}
  },
  "multi-gen-group-villa-syros": {
    "el": {"title": "Οικογενειακές και ομαδικές διακοπές σε βίλα στη Σύρο: χώρος, ρυθμός και logistics", "description": "Πώς να οργανώσετε διαμονή πολλών γενεών ή παρέας σε βίλα στη Σύρο: ύπνος, ρυθμός παραλίας, μαγείρεμα για πολλούς και γιατί δουλεύει ένα δυτικό σπίτι κοντά στο Δελφίνι.", "keywords": "ομαδικη βιλα Συρος, πολυγενεακες διακοπες Ελλαδα, μεγαλη παρεα Συρος", "kicker": "Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα", "hero_alt": "Τραπεζαρία και καθιστικό με πέτρινη καμάρα", "hero_caption": "Ένα τραπέζι, πολλές γενιές: η διάταξη που κάνει τις ομαδικές εβδομάδες να δουλεύουν."},
    "fr": {"title": "Séjours en villa multi-générationnels et en groupe à Syros", "description": "Comment organiser une villa à Syros pour plusieurs générations ou un groupe d’amis : couchages, rythme plage, cuisine pour une tablée, et pourquoi une maison ouest près de Delfini fonctionne.", "keywords": "villa groupe Syros, vacances multi générations Grèce, grande tablée Syros", "kicker": "Articles · Syros et séjours en bord de mer", "hero_alt": "Salle à manger et séjour avec arche en pierre", "hero_caption": "Une table, plusieurs générations : l’agencement qui fait réussir les semaines en groupe."},
    "de": {"title": "Mehrgenerationen- und Gruppenvilla auf Syros: Platz, Tempo und Logistik", "description": "Wie Sie einen Mehrgenerationen- oder Freundesgruppen-Aufenthalt in einer Villa auf Syros planen: Schlafen, Strandtempo, Kochen für viele — und warum ein Westküstenhaus bei Delfini funktioniert.", "keywords": "Gruppenvilla Syros, Mehrgenerationen Urlaub Griechenland, große Gruppe Syros", "kicker": "Artikel · Syros & Urlaub am Meer", "hero_alt": "Ess- und Wohnbereich mit Steinbogen", "hero_caption": "Ein Tisch, mehrere Generationen: das Layout, das Gruppenwochen trägt."},
    "it": {"title": "Soggiorni in villa multi-generazionali e di gruppo a Syros", "description": "Come organizzare una villa a Syros per più generazioni o un gruppo di amici: posti letto, ritmo spiaggia, cucinare per tanti e perché funziona una casa a ovest vicino a Delfini.", "keywords": "villa gruppo Syros, vacanze multi generazionali Grecia, gruppo grande Syros", "kicker": "Articoli · Syros e soggiorni al mare", "hero_alt": "Zona pranzo e soggiorno con arco in pietra", "hero_caption": "Un tavolo, più generazioni: la disposizione che fa funzionare le settimane di gruppo."},
    "he": {"title": "חופשות וילה רב-דוריות וקבוצתיות בסירוס: מקום, קצב ולוגיסטיקה", "description": "איך לתכנן שהיית וילה בסירוס למשפחה רב-דורית או קבוצת חברים: שינה, קצב חוף, בישול להרבה אנשים ולמה בית במערב ליד דלפיני עובד.", "keywords": "וילה קבוצתית סירוס, חופשה רב דורית יוון, קבוצה גדולה סירוס", "kicker": "מאמרים · סירוס ולינה ליד הים", "hero_alt": "פינת אוכל וסלון עם קשת אבן", "hero_caption": "שולחן אחד, כמה דורות: הפריסה שמחזיקה שבועות קבוצתיים."}
  }
}
''')

for slug, langs in MORE.items():
    SEO.setdefault(slug, {}).update(langs)


def main() -> None:
    art = json.loads(ART.read_text(encoding="utf-8"))
    n = 0
    for slug, langs in SEO.items():
        art.setdefault(slug, {})
        for lang, fields in langs.items():
            cur = dict(art[slug].get(lang) or {})
            cur.update(fields)
            # keep existing body if already translated; else leave pending stub
            if "body" not in cur or not cur["body"] or "Translation pending" in cur["body"]:
                cur["body"] = cur.get("body") or "<p>Translation pending.</p>"
            cur.setdefault("mid_alt", "")
            cur.setdefault("mid_caption", "")
            art[slug][lang] = cur
            n += 1
    ART.write_text(json.dumps(art, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"updated SEO fields for {n} lang/slug pairs")


if __name__ == "__main__":
    main()
