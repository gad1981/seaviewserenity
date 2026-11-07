from .common import callout

TABLE = (
    '<h2>{h0}</h2>'
    '<table style="width:100%;border-collapse:collapse;font-size:0.95rem">'
    '<thead><tr>'
    '<th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">{h1}</th>'
    '<th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">{h2}</th>'
    '</tr></thead><tbody>'
    '{rows}'
    '</tbody></table>'
)


def _table(h0, h1, h2, rows):
    return TABLE.format(h0=h0, h1=h1, h2=h2, rows=rows)


def entries():
    rows_el = (
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Ηλιοβασιλέματα σε καλντέρα και απόκρημνες απότομες πλαγιές</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Σαντορίνη</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Beach clubs και πυκνή νυχτερινή ζωή</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Μύκονος</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Πολιτισμός πόλης + ήσυχες νύχτες στη θάλασσα</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Σύρος</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem">Οικογενειακό σπίτι με κουζίνα κοντά σε κόλπο</td><td style="padding:0.45rem 0.4rem">Δυτική Σύρος (π.χ. Δελφίνι / Κίνι)</td></tr>'
    )

    shared_refs = (
        '<p>Visit Greece περιγράφει τις Κυκλάδες ως την πιο γνωστή νησιωτική ομάδα του Αιγαίου, ενώ τη Σύρο την τοποθετεί ως κομψή πρωτεύουσα όπου Ανατολή και Δύση συναντώνται σε κοσμοπολίτικη ατμόσφαιρα.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup> Αυτή η ιδιότητα πρωτεύουσας έχει πρακτική αξία: ακτοπλοϊκές συνδέσεις, ζωντανή πόλη και υπηρεσίες πέρα από το απόλυτο peak.</p>'
    )

    el = {
        "title": "Σύρος vs Σαντορίνη και Μύκονος: Πώς να επιλέξετε πιο ήσυχες Κυκλάδες | Sea View Serenity",
        "description": "Συγκρίνετε τη Σύρο με Σαντορίνη και Μύκονο για πιο ήσυχες διακοπές στις Κυκλάδες — πολιτισμός, παραλίες και παραθαλάσσια διαμονή με αίσθηση νησιού.",
        "keywords": "Σύρος vs Μύκονος, Σύρος vs Σαντορίνη, ήσυχες Κυκλάδες, διακοπές Σύρος, διακοπές Κυκλάδες, διαμονή στη θάλασσα Ελλάδα",
        "kicker": "Άρθρα · Σύρος και παραθαλάσσιες διαμονές",
        "hero_alt": "Θέα της Ερμούπολης στη Σύρο",
        "hero_caption": "Η Ερμούπολη, πρωτεύουσα της Σύρου — νεοκλασικό λιμάνι-πόλη.",
        "mid_alt": "Ήσυχη παραθαλάσσια βεράντα στο ηλιοβασίλεμα στη Σύρο",
        "mid_caption": "Πιο ήσυχα βράδια δίπλα στη θάλασσα — λόγος που πολλοί επιλέγουν Σύρο αντί για νησιά με έμφαση στη νύχτα.",
        "body": (
            '<p>Πολλοί ξεκινούν με «Σαντορίνη» ή «Μύκονος» και αργότερα ρωτούν αν θέλουν πιο <strong>ήσυχες διακοπές στις Κυκλάδες</strong>. Η Σύρος ταιριάζει συχνά καλύτερα όταν το ιστορικό αναζήτησής σας λέει «ήσυχο ελληνικό νησί», «πολιτισμός και παραλίες» ή «διαμονή στη θάλασσα χωρίς πάρτι».</p>'
            + shared_refs
            + '<h2>Σύρος vs Σαντορίνη</h2>'
            '<p>Η Σαντορίνη είναι εμβληματική για θέα καλντέρας και εικόνες μήνα του μέλιτος. Η Σύρος είναι ισχυρότερη αν θέλετε:</p>'
            '<ul>'
            '<li>Νεοκλασικούς δρόμους και καθημερινή ζωή καφέ στην Ερμούπολη<sup><a href="#ref2">[2]</a></sup></li>'
            '<li>Μεσαιωνικό καθολικό τετραγωνισμό στην Άνω Σύρο δίπλα στην ορθόδοξη Ερμούπολη<sup><a href="#ref2">[2]</a></sup></li>'
            '<li>Ημέρες παραλίας χαμηλού προφίλ στη δυτική ακτή (Κίνι, Δελφίνι) ή νότια για μεγαλύτερους αμμώδεις όρμους<sup><a href="#ref3">[3]</a></sup></li>'
            '</ul>'
            '<p>Αν τα keywords είναι «ρομαντική θέα Ελλάδα», η Σαντορίνη μπορεί να κερδίζει. Αν είναι «αυθεντική πόλη στις Κυκλάδες + παραμονή στη θάλασσα», η Σύρος είναι συνήθως πιο σαφής επιλογή.</p>'
            '<h2>Σύρος vs Μύκονος</h2>'
            '<p>Η Μύκονος κυριαρχεί στη νυχτερινή ζωή και στα beach brands με υψηλή ορατότητα. Η Σύρος κυριαρχεί στην ισορροπία: πολιτισμός, γαστρονομία και παράκτια χωριά χωρίς VIP τραπέζι για να θεωρήσετε την εκδρομή επιτυχημένη. Το επίσημο κείμενο προορισμού τονίζει φεστιβάλ, κουζίνα και ζωντάνια πέρα από σύντομο καλοκαιρινό spike.<sup><a href="#ref2">[2]</a></sup></p>'
            '<h2>Τι σημαίνουν τα δεδομένα ενοικίασης 2025–2026 για τους ταξιδιώτες</h2>'
            '<p>Η απόδοση βραχυχρόνιων μισθώσεων στις Κυκλάδες επιβράδυνε σε μέρη του 2025, με αναφορές Hosthub για χαμηλότερη πληρότητα και τιμές σε σχέση με προηγούμενα peaks — ένας λόγος να ανακαλύπτουν αξία σε λιγότερο εκτεθειμένα νησιά.<sup><a href="#ref4">[4]</a></sup> Για το καλοκαίρι 2026, αναλύσεις ξανά δείχνουν ισχυρότερο εθνικό ρυθμό και ανάκαμψη για εμβληματικές Κυκλάδες, ενώ οι επισκέπτες επιβραβεύουν ποιότητα έναντι minimal καταλυμάτων.<sup><a href="#ref5">[5]</a></sup><sup><a href="#ref6">[6]</a></sup></p>'
            '<p>Πρακτικά: <strong>κλείστε την εμπειρία νησιού που θέλετε πραγματικά</strong>. Αν θέλετε ήσυχα βράδια, κόλπο με τα πόδια και πλήρες σπίτι για οικογένεια, οι ενοικιάσεις στη Σύρο ανταγωνίζονται στη ζήσιμη διαμονή — όχι στον πιο δυνατά φανταχτερό όρο αναζήτησης.</p>'
            + callout(
                "Προτιμάτε πιο ήσυχη βάση στις Κυκλάδες;",
                "Το Sea View Serenity βρίσκεται κοντά στη Δελφίνι στη Σύρο — κοντά στα ηλιοβασιλέματα του Κινιού και εντός εύλογης απόστασης από το νεοκλασικό κέντρο της Ερμούπολης.",
                "Κράτηση τώρα",
            )
            + _table("Γρήγορος πίνακας σύγκρισης", "Αν θέλετε…", "Σκεφτείτε", rows_el)
        ),
    }

    rows_fr = (
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Couchers de soleil sur la caldeira & falaises iconiques</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Santorin</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Beach clubs & vie nocturne dense</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Mykonos</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Culture urbaine + nuits plus calmes au bord de l\'eau</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Syros</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem">Maison familiale avec cuisine près d\'une crique</td><td style="padding:0.45rem 0.4rem">Côte ouest de Syros (ex. Delfini / Kini)</td></tr>'
    )
    fr_body_core = (
        '<p>Beaucoup commencent par « Santorin » ou « Mykonos », puis se demandent s’ils veulent des <strong>vacances plus calmes aux Cyclades</strong>. Syros correspond souvent mieux si vous cherchez « île grecque tranquille », « culture et plages » ou « logement en bord de mer sans fête ».</p>'
        '<p>Visit Greece décrit les Cyclades comme l’archipel le plus connu de l’Égée, et place Syros comme capitale élégante où Orient et Occident se rencontrent.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup> Statut de capitale utile : ferries, ville active, services hors pics de fête.</p>'
        '<h2>Syros vs Santorin</h2>'
        '<p>Santorin : caldeira et cartes postales. Syros convient si vous voulez rues néoclassiques et cafés à Ermoupoli<sup><a href="#ref2">[2]</a></sup>, quartier catholique médiéval à Ano Syros<sup><a href="#ref2">[2]</a></sup>, plages plus discrètes à l’ouest (Kini, Delfini) ou au sud pour le sable<sup><a href="#ref3">[3]</a></sup>. Keywords « point de vue romantique » : Santorin ; « ville cycladique authentique + mer » : Syros.</p>'
        '<h2>Syros vs Mykonos</h2>'
        '<p>Mykonos mène la nuit et les marques de plage. Syros équilibre culture, gastronomie et villages côtiers sans table VIP pour valider le séjour.<sup><a href="#ref2">[2]</a></sup></p>'
        '<h2>Ce que les données location 2025–2026 impliquent</h2>'
        '<p>Les locations courts séjours ont ralenti en parties des Cyclades en 2025 (reporting Hosthub : occupation et tarifs sous les pics précédents).<sup><a href="#ref4">[4]</a></sup> Vers l’été 2026, analyses nationales et retour des grandes îles, avec prime à la qualité.<sup><a href="#ref5">[5]</a></sup><sup><a href="#ref6">[6]</a></sup></p>'
        '<p>Conseil : <strong>réservez l’expérience d’île que vous voulez vraiment</strong>. Soirées calmes, crique accessible, maison pour la famille : Syros rivalise sur la « vivable », pas sur le bruit des recherches.</p>'
        + callout(
            "Une base plus calme aux Cyclades ?",
            "Sea View Serenity est près de Delfini à Syros — coucher de soleil à Kini et centre néoclassique d’Ermoupoli à portée.",
            "Réserver",
        )
        + _table("Checklist de comparaison rapide", "Si vous voulez…", "Penchez-vous vers", rows_fr)
    )

    fr = {
        "title": "Syros vs Santorin et Mykonos : choisir des Cyclades plus calmes | Sea View Serenity",
        "description": "Comparez Syros à Santorin et Mykonos pour des vacances cycladiques plus tranquilles — culture, plages et logement en bord de mer authentique.",
        "keywords": "Syros vs Mykonos, Syros vs Santorin, Cyclades calmes, vacances Syros, vacances Cyclades, séjour bord de mer Grèce",
        "kicker": "Articles · Syros et séjours en bord de mer",
        "hero_alt": "Vue d'Ermoupoli sur l'île de Syros, Grèce",
        "hero_caption": "Ermoupoli, capitale de Syros — ville portuaire néoclassique.",
        "mid_alt": "Terrasse tranquille au coucher du soleil sur Syros",
        "mid_caption": "Des soirées plus calmes en bord de mer — une raison fréquente de choisir Syros plutôt que l'île « fête ».",
        "body": fr_body_core,
    }

    rows_de = (
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Kaldera-Sonnenuntergänge &amp; Postkartenklippen</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Santorini</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Beachclubs &amp; dichtes Nachtleben</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Mykonos</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Stadtkultur + ruhigere Abende am Meer</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Syros</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem">Familienhaus mit Küche nahe einer Bucht</td><td style="padding:0.45rem 0.4rem">Westküste Syros (z. B. Delfini / Kini)</td></tr>'
    )
    de = {
        "title": "Syros vs Santorini und Mykonos: Ruhigere Kykladenurlaube wählen | Sea View Serenity",
        "description": "Vergleichen Sie Syros mit Santorini und Mykonos für ruhigere Kykladen-Ferien — Kultur, Strände und Unterkunft am Meer mit Inselgefühl.",
        "keywords": "Syros vs Mykonos, Syros vs Santorini, ruhige Kykladen, Syros Urlaub, Kykladen Urlaub, Unterkunft am Meer Griechenland",
        "kicker": "Artikel · Syros & Aufenthalte am Meer",
        "hero_alt": "Blick auf Ermoupoli auf Syros, Griechenland",
        "hero_caption": "Ermoupoli, Hauptstadt von Syros — neoklassische Hafenstadt.",
        "mid_alt": "Ruhige Terrasse bei Sonnenuntergang auf Syros",
        "mid_caption": "Ruhigere Abende am Meer — warum viele Syros statt Partynacht-Inseln wählen.",
        "body": (
            '<p>Viele starten mit « Santorini » oder « Mykonos » und fragen später, ob sie einen <strong>ruhigeren Kykladenurlaub</strong> wollen. Syros passt oft besser bei « ruhige griechische Insel », « Kultur und Strände » oder « Unterkunft am Meer ohne Party ».</p>'
            '<p>Visit Greece beschreibt die Kykladen als die bekannteste Inselgruppe der Ägäis und Syros als elegante Hauptstadt, wo Ost und West kosmopolitisch zusammentreffen.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup> Hauptstadt-Vorteil: Fähren, lebendige Stadt, Services auch außerhalb Party-Peak.</p>'
            '<h2>Syros vs Santorini</h2>'
            '<p>Santorini: Kaldera-Ikonen. Syros stärker bei neoklassischen Straßen und Café-Alltag in Ermoupoli<sup><a href="#ref2">[2]</a></sup>, mittelalterlichem katholischen Viertel in Ano Syros<sup><a href="#ref2">[2]</a></sup>, ruhigeren Weststränden (Kini, Delfini) oder sandigen Süd-buchten<sup><a href="#ref3">[3]</a></sup>.</p>'
            '<h2>Syros vs Mykonos</h2>'
            '<p>Mykonos führt bei Nachtleben und Beach-Brands. Syros bei Balance: Kultur, Kulinarik, Küstendörfer — ohne VIP-Tisch als Erfolgskriterium.<sup><a href="#ref2">[2]</a></sup></p>'
            '<h2>Was Mietdaten 2025–2026 bedeuten</h2>'
            '<p>Kurzzeitmieten in den Kykladen kühlten 2025 teils ab (Hosthub-Reporting: geringere Auslastung und Raten gegenüber früheren Spitzen).<sup><a href="#ref4">[4]</a></sup> Für Sommer 2026: national stärkeres Tempo, Erholung bei Flagship-Inseln, Gäste honorieren Qualität.<sup><a href="#ref5">[5]</a></sup><sup><a href="#ref6">[6]</a></sup></p>'
            '<p><strong>Buchen Sie das Inselerlebnis, das Sie wirklich wollen.</strong> Ruhige Abende, Bucht zu Fuß, volles Haus für die Familie: Syros konkurriert über Wohnqualität — nicht über den lautesten Suchbegriff.</p>'
            + callout(
                "Lieber eine ruhigere Kykladen-Basis?",
                "Sea View Serenity liegt nahe Delfini auf Syros — Kini-Sonnenuntergänge und Ermoupolis’ neoklassisches Zentrum in Reichweite.",
                "Jetzt buchen",
            )
            + _table("Kurze Vergleichsliste", "Wenn Sie … wollen", "Tendenz", rows_de)
        ),
    }

    rows_it = (
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Tramonti sulla caldera e scogliere iconiche</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Santorini</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Beach club e vita notturna densa</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Mykonos</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Cultura cittadina + notti più tranquille al mare</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Syros</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem">Casa familiare con cucina vicino a una caletta</td><td style="padding:0.45rem 0.4rem">Costa ovest di Syros (es. Delfini / Kini)</td></tr>'
    )
    it = {
        "title": "Syros vs Santorini e Mykonos: scegliere Cicladi più tranquille | Sea View Serenity",
        "description": "Confrontate Syros con Santorini e Mykonos per vacanze più calme nelle Cicladi — cultura, spiagge e alloggio sul mare autentico.",
        "keywords": "Syros vs Mykonos, Syros vs Santorini, Cicladi tranquille, vacanze Syros, vacanze Cicladi, soggiorno mare Grecia",
        "kicker": "Articoli · Syros e soggiorni sul mare",
        "hero_alt": "Vista di Ermoupoli sull'isola di Syros, Grecia",
        "hero_caption": "Ermoupoli, capitale di Syros — città portuale neoclassica.",
        "mid_alt": "Terrazza sul mare al tramonto, tranquilla, a Syros",
        "mid_caption": "Sere più calme sul mare: motivo frequente per scegliere Syros invece delle isole «party ».",
        "body": (
            '<p>Molti partono da « Santorini » o « Mykonos » e poi chiedono se vogliono <strong>vacanze più tranquille nelle Cicladi</strong>. Syros spesso calza meglio con « isola greca tranquilla », « cultura e spiagge » o « alloggio sul mare senza feste ».</p>'
            '<p>Visit Greece descrive le Cicladi come l’arcipelago più noto dell’Egeo e Syros come capitale elegante dove Oriente e Occidente si incontrano.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup> Capitale significa traghetti, città attiva, servizi oltre i weekend di festa.</p>'
            '<h2>Syros vs Santorini</h2>'
            '<p>Santorini vince sulle calde. Syros se volete strade neoclassiche e caffè quotidiani a Ermoupoli<sup><a href="#ref2">[2]</a></sup>, quartiere cattolico medievale ad Ano Syros<sup><a href="#ref2">[2]</a></sup>, spiagge low-key a ovest (Kini, Delfini) o sabbia a sud<sup><a href="#ref3">[3]</a></sup>.</p>'
            '<h2>Syros vs Mykonos</h2>'
            '<p>Mykonos guida nightlife e beach brand. Syros equilibrio: cultura, gastronomia, villaggi costieri senza tavolo VIP.<sup><a href="#ref2">[2]</a></sup></p>'
            '<h2>Cosa implicano i dati affitti 2025–2026</h2>'
            '<p>Gli affitti brevi nelle Cicladi sono rallentati in parti del 2025 (report Hosthub: occupazione e tariffe sotto picchi precedenti).<sup><a href="#ref4">[4]</a></sup> Verso l’estate 2026: ritmo nazionale più forte, ripresa sulle isole iconiche, premi alla qualità.<sup><a href="#ref5">[5]</a></sup><sup><a href="#ref6">[6]</a></sup></p>'
            '<p><strong>Prenotate l’esperienza insulare che volete davvero.</strong> Sere tranquille, caletta a piedi, casa piena per la famiglia: Syros compete sulla vivibilità.</p>'
            + callout(
                "Preferite una base più calma nelle Cicladi?",
                "Sea View Serenity è vicino a Delfini a Syros — tramonti a Kini e centro neoclassico di Ermoupoli raggiungibile.",
                "Prenota ora",
            )
            + _table("Checklist di confronto rapido", "Se volete…", "Orientatevi verso", rows_it)
        ),
    }

    rows_he = (
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">שקיעות בקלדרה וצוקים איקוניים</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">סנטוריני</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">מועדוני חוף וחיי לילה צפופים</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">מיקונוס</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">תרבות עיר + ערבים שקטים יותר ליד הים</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">סירוס</td></tr>'
        '<tr><td style="padding:0.45rem 0.4rem">בית משפחתי עם מטבח ליד מפרץ</td><td style="padding:0.45rem 0.4rem">חוף מערבי בסירוס (למשל דלפיני / קיני)</td></tr>'
    )
    he = {
        "title": "סירוס מול סנטוריני ומיקונוס: לבחור חופשה שקטה יותר בקיקלדים | Sea View Serenity",
        "description": "השוו בין סירוס לסנטוריני ומיקונוס לחופשה שקטה יותר בקיקלדים — תרבות, חופים ולינה ליד הים עם תחושת אי אמיתית.",
        "keywords": "סירוס מול מיקונוס, סירוס מול סנטוריני, קיקלדים שקטים, חופשה בסירוס, חופשה בקיקלדים, לינה ליד הים ביוון",
        "kicker": "מאמרים · סירוס ולינה ליד הים",
        "hero_alt": "מבט על ארמופולי באי סירוס, יוון",
        "hero_caption": "ארמופולי, בירת סירוס — עיר נמל נאוקלאסית.",
        "mid_alt": "מרפסת שקטה ליד הים בשקיעה בסירוס",
        "mid_caption": "ערבים שקטים יותר ליד הים — סיבה נפוצה לבחור בסירוס ולא באיי מסיבות.",
        "body": (
            '<p>רבים מתחילים ב«סנטוריני» או «מיקונוס» ורק אחר כך שואלים אם הם רוצים <strong>חופשה שקטה יותר בקיקלדים</strong>. סירוס מתאימה לעתים קרובות יותר לחיפושים כמו «אי יווני שקט», «תרבות וחופים» או «לינה ליד הים בלי מסיבות».</p>'
            '<p>Visit Greece מתאר את הקיקלדים כקבוצת האיים המפורסמת באגאי, ואת סירוס כבירה אלגנטית שבה מזרח ומערב נפגשים באווירה קוסמופוליטית.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup> מעמד בירה מעשי: מעבורות, עיר פעילה ושירותים מעבר לסופי שבוע של מסיבות.</p>'
            '<h2>סירוס מול סנטוריני</h2>'
            '<p>סנטוריני איקונית לנוף קלדרה ותמונות ירח דבש. סירוס חזקה יותר אם רוצים רחובות נאוקלאסיים וחיי קפה יומיומיים בארמופולי<sup><a href="#ref2">[2]</a></sup>, רובע קתולי מימי הביניים בענו סירוס<sup><a href="#ref2">[2]</a></sup>, וימי חוף שקטים יותר במערב (קיני, דלפיני) או חול בדרום<sup><a href="#ref3">[3]</a></sup>.</p>'
            '<h2>סירוס מול מיקונוס</h2>'
            '<p>מיקונוס מובילה בלילה ובמותגי חוף. סירוס באיזון: תרבות, גסטרונומיה וכפרי חוף בלי שולחן VIP כדי להצליח.<sup><a href="#ref2">[2]</a></sup></p>'
            '<h2>מה נתוני השכירות 2025–2026 אומרים למטיילים</h2>'
            '<p>ביצועי שכירות לזמן קצר בקיקלדים התקררו בחלקים ב-2025, עם דיווח Hosthub על תפוסה ומחירים נמוכים יותר מהשיאים הקודמים.<sup><a href="#ref4">[4]</a></sup> לקראת קיץ 2026: קצב חזק יותר ברמה הלאומית וסיפור התאוששות לאיים הדגל, והאורחים מתגמלים איכות.<sup><a href="#ref5">[5]</a></sup><sup><a href="#ref6">[6]</a></sup></p>'
            '<p><strong>הזמינו את חוויית האי שאתם באמת רוצים.</strong> ערבים שקטים, מפרץ בהליכה, בית מלא למשפחה — השכירות בסירוס מתחרות בחיוּת, לא בכותרת החיפוש הרועשת ביותר.</p>'
            + callout(
                "מעדיפים בסיס שקט יותר בקיקלדים?",
                "Sea View Serenity ליד דלפיני בסירוס — קרוב לשקיעות בקיני ובמרחק סביר ממרכז ארמופולי הנאוקלאסי.",
                "הזמנה עכשיו",
            )
            + _table("רשימת השוואה מהירה", "אם אתם רוצים…", "הטו לכיוון", rows_he)
        ),
    }

    return {"el": el, "fr": fr, "de": de, "it": it, "he": he}
