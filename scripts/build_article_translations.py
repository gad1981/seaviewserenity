#!/usr/bin/env python3
"""Build article i18n JSON — run: python3 scripts/build_article_translations.py"""
import json
import sys

KICKER = {
    "el": "Άρθρα · Σύρος & παραθαλάσσιες διαμονές",
    "fr": "Articles · Syros et séjours au bord de la mer",
    "de": "Artikel · Syros & Übernachtungen am Meer",
    "it": "Articoli · Syros e soggiorni sul mare",
    "he": "מאמרים · סירוס וחופשות על הים",
}

def how_to_get_to():
    return {
        "el": {
            "title": "Πώς να πάτε στη Σύρο από την Αθήνα: πλοίο, πτήση και συμβουλές κράτησης | Sea View Serenity",
            "description": "Συγκρίνετε πλοίο και πτήση Αθήνα–Σύρος, χρόνους διαδρομής και πότε να κλείσετε εισιτήρια ώστε το check-in στη παραθαλάσσια βίλα να είναι χωρίς άγχος.",
            "keywords": "πώς να πάω στη Σύρο, πλοίο Αθήνα Σύρος, πτήση Σύρος, Πειραιάς Σύρος, αεροδρόμιο Σύρου, ταξίδι Κυκλάδες",
            "kicker": KICKER["el"],
            "hero_alt": "Η Ερμούπολη από πλοίο που φτάνει στη Σύρο",
            "hero_caption": "Η Ερμούπολη από το πλοίο — η συνηθισμένη άφιξη στη Σύρο.",
            "mid_alt": "Το λιμάνι της Σύρου στην Ερμούπολη",
            "mid_caption": "Το λιμάνι της Σύρου στην Ερμούπολη.",
            "body": """<p>Αναζητήσεις όπως <strong>«πώς να πάω στη Σύρο»</strong> και <strong>«πλοίο Αθήνα Σύρος»</strong> συνήθως προέρχονται από ταξιδιώτες που ήδη θέλουν το νησί — χρειάζονται απλώς ένα σαφές σχέδιο άφιξης πριν κλείσουν παραθαλάσσιο σπίτι. Η Σύρος προσφέρεται αεροπορικώς και ακτοπλοϊκώς· οι περισσότεροι επισκέπτες φτάνουν ακόμη με πλοίο στην Ερμούπολη.</p>
<h2>Επιλογή 1: Πλοίο από την Αθήνα (Πειραιάς)</h2>
<p>Η κύρια γραμμή είναι <strong>Πειραιάς → Ερμούπολη</strong>. Τα δρομολόγια ισχύουν όλο το χρόνο, με έως και περίπου έξι καθημερινές αναχωρήσεις στην κορυφή της σεζόν, και διάρκεια από περίπου <strong>2 ώρες</strong> στις ταχύτερες υπηρεσίες έως <strong>4 ώρες</strong> στα συμβατικά πλοία.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-harbour.jpg" alt="Το λιμάνι της Σύρου στην Ερμούπολη" loading="lazy" width="1200" height="675" />
  <figcaption>Το λιμάνι της Σύρου στην Ερμούπολη.</figcaption>
</figure>
<p>Οι τοπικές πληροφορίες αναφέρουν καθημερινή ακτοπλοϊκή σύνδεση από τον Πειραιά, με συμβατικά δρομολόγια περίπου τετραώρου και ταχύπλοα κοντά στις δυόμισι ώρες, καθώς και επιπλέον συνδέσεις με τις Κυκλάδες που καθιστούν τη Σύρο πρακτικό κόμβο.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>Ιδανικό για:</strong> αποσκευές, οικογένειες και μεταφορά ενοικιαζόμενου αυτοκινήτου για αλλαγή παραλιών</li>
  <li><strong>Κλείστε νωρίς αν:</strong> ταξιδεύετε Ιούλιο–Αύγουστο ή χρειάζεστε θέση στο γκαράζ αυτοκινήτων<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Συμβουλή άφιξης:</strong> κατεβαίνετε στην πόλη-λιμάνι της Ερμούπολης — καταστήματα, λεωφορεία και μεταφορές είναι κοντά<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>Επιλογή 2: Πτήση από την Αθήνα</h2>
<p>Υπάρχει σύντομο εσωτερικό δρομολόγιο από το Διεθνές Αεροδρόμιο Αθηνών προς το αεροδρόμιο της Σύρου σε περίπου <strong>25 λεπτά</strong>, με σύνδεση και από τη Θεσσαλονίκη για μακρύτερα εσωτερικά δρομολόγια.<sup><a href="#ref3">[3]</a></sup> Η συχνότητα μπορεί να είναι μικρότερη από το πλοίο, οπότε ελέγξτε το πρόγραμμα — μην το θεωρείτε δεδομένο, ειδικά εκτός κορυφαίων εβδομάδων.</p>
<h2>Αεροδρόμιο ή λιμάνι: τι να διαλέξετε;</h2>
<ol>
  <li><strong>Προτιμήστε το πλοίο</strong> για καθημερινές επιλογές, μεταφορά αυτοκινήτου και όμορφη άφιξη στην πρωτεύουσα.</li>
  <li><strong>Προτιμήστε την πτήση</strong> όταν ο συνολικός χρόνος πόρτα-πόρτα μετράει περισσότερο από το κόστος και υπάρχουν θέσεις στις ημερομηνίες σας.<sup><a href="#ref3">[3]</a></sup></li>
  <li><strong>Κρατήστε περιθώριο</strong> από το αεροδρόμιο Αθηνών μέχρι τον Πειραιά αν πετάτε στο ATH και ταξιδεύετε την ίδια μέρα με πλοίο.<sup><a href="#ref1">[1]</a></sup></li>
</ol>
<div class="svs-callout">
  <strong>Άφιξη και χαλάρωση στη θάλασσα</strong>
  Μόλις φτάσετε στην Ερμούπολη, η επόμενη απόφαση είναι η βάση σας. Το Sea View Serenity είναι παραθαλάσσιο σπίτι στη δυτική ακτή κοντά στην παραλία Δελφίνι — ιδανικό μετά από ημέρα πλοίου, όταν θέλετε ήσυχο νερό και πλήρως εξοπλισμένη κουζίνα.
  <a class="svs-cta" href="BOOK">Κλείστε τη διαμονή σας στη Σύρο</a>
</div>
<h2>Σειρά κρατήσεων που προστατεύει τις διακοπές σας</h2>
<p>Κλειδώστε πρώτα τη <strong>διαμονή</strong> για κορυφαίες εβδομάδες, μετά πλοίο/πτήση και στη συνέχεια ενοικίαση αυτοκινήτου αν χρειάζεται. Το Νοτίο Αιγαίο παραμένει η πιο δημοφιλής περιοχή διανυκτερεύσεων στη χώρα, οπότε τα δημοφιλή παραθαλάσσια σπίτια και τα γκαράζ πλοίων «σφίγγονται» το μεσοκαίρι.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
        "fr": {
            "title": "Comment aller à Syros depuis Athènes : ferry, vol et conseils de réservation | Sea View Serenity",
            "description": "Comparez ferry et vol Athènes–Syros, durées de trajet et meilleur moment pour réserver afin que l’arrivée dans votre villa en bord de mer se passe sans stress.",
            "keywords": "comment aller à Syros, ferry Athènes Syros, vol Syros, Pirée Syros, aéroport de Syros, voyage Cyclades",
            "kicker": KICKER["fr"],
            "hero_alt": "Ermoupoli vue depuis un ferry approchant Syros",
            "hero_caption": "Ermoupoli depuis le ferry — l’arrivée habituelle à Syros.",
            "mid_alt": "Port de Syros à Ermoupoli, Grèce",
            "mid_caption": "Le port de Syros à Ermoupoli.",
            "body": """<p>Les recherches du type <strong>« comment aller à Syros »</strong> ou <strong>« ferry Athènes Syros »</strong> viennent souvent de voyageurs qui ont déjà choisi l’île : il leur manque surtout un plan d’arrivée clair avant de réserver une maison au bord de la mer. Syros est accessible par la mer et par les airs ; la plupart des visiteurs arrivent encore en ferry à Ermoupoli.</p>
<h2>Option 1 : Ferry depuis Athènes (Le Pirée)</h2>
<p>La liaison principale est <strong>Pirée → Ermoupoli</strong>. Des traversées existent toute l’année, avec jusqu’à environ six départs quotidiens en haute saison, pour une durée d’environ <strong>2 heures</strong> sur les lignes les plus rapides jusqu’à <strong>4 heures</strong> sur les navires conventionnels.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-harbour.jpg" alt="Port de Syros à Ermoupoli" loading="lazy" width="1200" height="675" />
  <figcaption>Le port de Syros à Ermoupoli.</figcaption>
</figure>
<p>Les guides locaux indiquent un service quotidien depuis le Pirée : environ quatre heures en ferry conventionnel, près de deux heures et demie en rapide, plus des liaisons vers d’autres îles des Cyclades qui font de Syros un hub pratique.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>Idéal pour :</strong> les bagages, les familles et emmener une voiture de location pour changer de plage</li>
  <li><strong>Réservez tôt si :</strong> vous voyagez en juillet–août ou avez besoin d’une place garage<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>À l’arrivée :</strong> vous débarquez dans la ville-port d’Ermoupoli — commerces, bus et transferts sont proches<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>Option 2 : Vol depuis Athènes</h2>
<p>Un court vol intérieur relie l’aéroport international d’Athènes à l’aéroport de Syros en environ <strong>25 minutes</strong>, avec une liaison possible depuis Thessalonique pour les itinéraires domestiques plus longs.<sup><a href="#ref3">[3]</a></sup> La fréquence peut être plus faible qu’au ferry : vérifiez le planning — surtout hors des semaines de pointe.</p>
<h2>Aéroport ou port : que choisir ?</h2>
<ol>
  <li><strong>Le ferry</strong> pour des départs quotidiens, le transport de voiture et une arrivée scénique dans la capitale.</li>
  <li><strong>Le vol</strong> quand le temps porte-à-porte compte plus que le prix et qu’il reste des places à vos dates.<sup><a href="#ref3">[3]</a></sup></li>
  <li><strong>Gardez une marge</strong> entre l’aéroport d’Athènes et le Pirée si vous atterrissez à ATH et prenez le ferry le jour même.<sup><a href="#ref1">[1]</a></sup></li>
</ol>
<div class="svs-callout">
  <strong>Arriver, puis s’installer face à la mer</strong>
  Une fois à Ermoupoli, choisissez votre base. Sea View Serenity est une maison en bord de mer sur la côte ouest, près de la plage de Delfini — parfaite après une journée de ferry, quand vous voulez une eau calme et une cuisine complète.
  <a class="svs-cta" href="BOOK">Réserver votre séjour à Syros</a>
</div>
<h2>Ordre de réservation qui protège vos vacances</h2>
<p>Verrouillez d’abord le <strong>logement</strong> pour les semaines chargées, puis ferry/vol, puis la location de voiture si besoin. La région de la mer Égée méridionale reste la zone la plus demandée pour les nuitées ; maisons prisées et places garage se remplissent vite en plein été.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
        "de": {
            "title": "So kommen Sie von Athen nach Syros: Fähre, Flug und Buchungstipps | Sea View Serenity",
            "description": "Vergleichen Sie Fähre und Flug Athen–Syros, Fahrzeiten und den besten Buchungszeitpunkt — damit der Check-in in Ihrer Villa am Meer stressfrei bleibt.",
            "keywords": "wie nach Syros, Fähre Athen Syros, Flug Syros, Piräus Syros, Flughafen Syros, Kykladen Reise",
            "kicker": KICKER["de"],
            "hero_alt": "Ermoupoli von einer ankommenden Fähre aus, Syros",
            "hero_caption": "Ermoupoli von der Fähre — die übliche Ankunft auf Syros.",
            "mid_alt": "Hafen von Syros in Ermoupoli, Griechenland",
            "mid_caption": "Der Hafen von Syros in Ermoupoli.",
            "body": """<p>Suchanfragen wie <strong>„wie komme ich nach Syros“</strong> oder <strong>„Fähre Athen Syros“</strong> stammen meist von Reisenden, die das Inselziel schon gewählt haben — sie brauchen einen klaren Ankunftsplan, bevor sie ein Haus am Meer buchen. Syros ist per Luft und See erreichbar; die meisten Gäste kommen weiterhin mit der Fähre nach Ermoupoli.</p>
<h2>Option 1: Fähre ab Athen (Piräus)</h2>
<p>Die Hauptverbindung ist <strong>Piräus → Ermoupoli</strong>. Ganzjährig gibt es Fahrten, in der Hochsaison bis zu etwa sechs tägliche Abfahrten, mit Reisezeiten von rund <strong>2 Stunden</strong> auf den schnellsten Linien bis etwa <strong>4 Stunden</strong> auf konventionellen Schiffen.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-harbour.jpg" alt="Hafen von Syros in Ermoupoli" loading="lazy" width="1200" height="675" />
  <figcaption>Der Hafen von Syros in Ermoupoli.</figcaption>
</figure>
<p>Lokale Informationen nennen tägliche Fährverbindungen ab Piräus: konventionell etwa vier Stunden, Hochgeschwindigkeit näher an zweieinhalb Stunden, plus weitere Kykladen-Verbindungen — Syros eignet sich gut als Knotenpunkt.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>Am besten für:</strong> Gepäck, Familien und ein Mietauto zum Strandhopping</li>
  <li><strong>Früh buchen, wenn:</strong> Sie im Juli–August reisen oder einen Autostellplatz an Bord brauchen<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Tipp bei der Ankunft:</strong> Sie landen in der Hafenstadt Ermoupoli — Geschäfte, Busse und Transfers sind nah<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>Option 2: Flug ab Athen</h2>
<p>Ein kurzer Inlandsflug verbindet den Internationalen Flughafen Athen mit dem Flughafen Syros in etwa <strong>25 Minuten</strong>; auch Thessaloniki wird für längere Inlandsrouten angeboten.<sup><a href="#ref3">[3]</a></sup> Die Frequenz kann geringer sein als bei der Fähre — prüfen Sie den Fahrplan, besonders außerhalb der Spitzenwochen.</p>
<h2>Flughafen oder Hafen: was passt besser?</h2>
<ol>
  <li><strong>Fähre wählen</strong> für tägliche Optionen, Autotransport und eine stimmungsvolle Ankunft in der Inselhauptstadt.</li>
  <li><strong>Flug wählen</strong>, wenn die Tür-zu-Tür-Zeit wichtiger ist als der Preis und Plätze zu Ihren Terminen verfügbar sind.<sup><a href="#ref3">[3]</a></sup></li>
  <li><strong>Puffer einplanen</strong> vom Flughafen Athen zum Piräus, wenn Sie in ATH landen und am selben Tag weiterfahren.<sup><a href="#ref1">[1]</a></sup></li>
</ol>
<div class="svs-callout">
  <strong>Ankommen und am Meer ankommen</strong>
  In Ermoupoli geht es als Nächstes um Ihre Basis. Sea View Serenity ist ein Haus an der Westküste nahe dem Strand Delfini — ideal nach einem Fährtag, wenn Sie ruhiges Wasser und eine voll ausgestattete Küche möchten.
  <a class="svs-cta" href="BOOK">Syros-Aufenthalt buchen</a>
</div>
<h2>Buchungsreihenfolge, die den Urlaub absichert</h2>
<p><strong>Unterkunft zuerst</strong> für Spitzenwochen festlegen, dann Fähre/Flug, dann ggf. Mietwagen. Die Südägäis bleibt die stark nachgefragte Übernachtungsregion — beliebte Häuser am Meer und Autodecks sind im Hochsommer schnell voll.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
        "it": {
            "title": "Come arrivare a Syros da Atene: traghetto, volo e consigli di prenotazione | Sea View Serenity",
            "description": "Confronta traghetto e volo Atene–Syros, tempi di viaggio e quando prenotare così il check-in nella villa sul mare resta senza stress.",
            "keywords": "come andare a Syros, traghetto Atene Syros, volo Syros, Pireo Syros, aeroporto Syros, viaggio Cicladi",
            "kicker": KICKER["it"],
            "hero_alt": "Ermoupoli vista da un traghetto in arrivo a Syros",
            "hero_caption": "Ermoupoli dal traghetto — l’arrivo più comune a Syros.",
            "mid_alt": "Porto di Syros a Ermoupoli, Grecia",
            "mid_caption": "Il porto di Syros a Ermoupoli.",
            "body": """<p>Chi cerca <strong>«come andare a Syros»</strong> o <strong>«traghetto Atene Syros»</strong> ha spesso già scelto l’isola: serve un piano d’arrivo chiaro prima di prenotare una casa sul mare. Syros si raggiunge per mare e per aria; la maggior parte degli ospiti arriva ancora in traghetto a Ermoupoli.</p>
<h2>Opzione 1: Traghetto da Atene (Pireo)</h2>
<p>La tratta principale è <strong>Pireo → Ermoupoli</strong>. Ci sono corse tutto l’anno, fino a circa sei partenze giornaliere in alta stagione, con tempi da circa <strong>2 ore</strong> sui collegamenti più veloci fino a <strong>4 ore</strong> sulle navi convenzionali.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-harbour.jpg" alt="Porto di Syros a Ermoupoli" loading="lazy" width="1200" height="675" />
  <figcaption>Il porto di Syros a Ermoupoli.</figcaption>
</figure>
<p>Le guide locali indicano collegamenti quotidiani dal Pireo: circa quattro ore in nave convenzionale, vicino a due ore e mezza in aliscafo, oltre a altre rotte delle Cicladi che rendono Syros un hub pratico.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>Ideale per:</strong> bagagli, famiglie e portare un’auto a noleggio per cambiare spiaggia</li>
  <li><strong>Prenotate presto se:</strong> viaggiate a luglio–agosto o vi serve posto auto a bordo<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>All’arrivo:</strong> sbarcate nella città-porto di Ermoupoli — negozi, bus e transfer sono vicini<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>Opzione 2: Volo da Atene</h2>
<p>Un breve volo domestico collega l’aeroporto internazionale di Atene all’aeroporto di Syros in circa <strong>25 minuti</strong>, con collegamento anche da Salonicco per itinerari interni più lunghi.<sup><a href="#ref3">[3]</a></sup> La frequenza può essere minore del traghetto: controllate l’orario, soprattutto fuori dalle settimane di punta.</p>
<h2>Aeroporto o porto: cosa scegliere?</h2>
<ol>
  <li><strong>Traghetto</strong> per opzioni quotidiane, trasporto auto e un arrivo scenico nella capitale.</li>
  <li><strong>Volo</strong> quando il tempo porta a porta conta più del prezzo e ci sono posti alle vostre date.<sup><a href="#ref3">[3]</a></sup></li>
  <li><strong>Margine di tempo</strong> dall’aeroporto di Atene al Pireo se atterrate ad ATH e partite lo stesso giorno.<sup><a href="#ref1">[1]</a></sup></li>
</ol>
<div class="svs-callout">
  <strong>Sbarcare e sistemarsi al mare</strong>
  Arrivati a Ermoupoli, scegliete la base. Sea View Serenity è una casa sul mare sulla costa occidentale, vicino alla spiaggia di Delfini — perfetta dopo una giornata in traghetto, con acqua tranquilla e cucina completa.
  <a class="svs-cta" href="BOOK">Prenota il soggiorno a Syros</a>
</div>
<h2>Ordine di prenotazione che tutela le vacanze</h2>
<p>Bloccare prima <strong>l’alloggio</strong> nelle settimane di punta, poi traghetto/volo, poi l’auto se serve. Il Mar Egeo meridionale resta la regione con più pernottamenti — case sul mare e posti auto a bordo si riempiono a metà estate.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
        "he": {
            "title": "איך מגיעים לסירוס מאתונה: מעבורת, טיסה וטיפים להזמנה | Sea View Serenity",
            "description": "השוו מעבורת וטיסה אתונה–סירוס, זמני נסיעה ומתי להזמין כרטיסים כדי שצ'ק-אין בווילה על הים יהיה ללא לחץ.",
            "keywords": "איך מגיעים לסירוס, מעבורת אתונה סירוס, טיסה לסירוס, פיראוס סירוס, נמל תעופה סירוס, חופשה בקיקלדים",
            "kicker": KICKER["he"],
            "hero_alt": "ארמופולי כפי שנראית ממעבורת נכנסת לסירוס",
            "hero_caption": "ארמופולי מהמעבורת — ההגעה המקובלת לסירוס.",
            "mid_alt": "נמל סירוס בארמופולי, יוון",
            "mid_caption": "נמל סירוס בארמופולי.",
            "body": """<p>חיפושים כמו <strong>«איך מגיעים לסירוס»</strong> ו<strong>«מעבורת אתונה סירוס»</strong> מגיעים לרוב ממטיילים שכבר בחרו באי — הם צריכים תוכנית הגעה ברורה לפני שמזמינים בית על הים. מגיעים לסירוס בים ובאוויר; רוב האורחים עדיין נוחתים במעבורת בארמופולי.</p>
<h2>אפשרות 1: מעבורת מאתונה (פיראוס)</h2>
<p>הקו המרכזי הוא <strong>פיראוס → ארמופולי</strong>. יש הפלגות כל השנה, עד כשש יציאות יומיות בעונה השיאית, ובזמני נסיעה של כ<strong>שעתיים</strong> בשירותים המהירים ועד כ<strong>ארבע שעות</strong> באוניות רגילות.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-harbour.jpg" alt="נמל סירוס בארמופולי" loading="lazy" width="1200" height="675" />
  <figcaption>נמל סירוס בארמופולי.</figcaption>
</figure>
<p>מקורות מקומיים מציינים שירות יומי מפיראוס: כארבע שעות במעבורת רגילה, כשעתיים וחצי במהירה, ועוד קווים לקיקלדים שממצבים את סירוס כמרכז תחבורה נוח.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>מתאים ל:</strong> מזוודות, משפחות והבאת רכב שכור למעבר בין חופים</li>
  <li><strong>הזמינו מוקדם אם:</strong> נוסעים ביולי–אוגוסט או צריכים מקום לרכב בסיפון<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>טיפ בהגעה:</strong> יורדים בעיר הנמל ארמופולי — חנויות, אוטובוסים והסעות קרובים<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>אפשרות 2: טיסה מאתונה</h2>
<p>יש טיסה פנימית קצרה משדה התעופה הבינלאומי של אתונה לנמל התעופה של סירוס, בערך <strong>25 דקות</strong>, וגם קישור מתסלוניקי למסלולים פנימיים ארוכים יותר.<sup><a href="#ref3">[3]</a></sup> התדירות עלולה להיות נמוכה יותר מהמעבורת — בדקו לוח זמנים, במיוחד מחוץ לשבועות השיא.</p>
<h2>שדה תעופה או נמל: מה לבחור?</h2>
<ol>
  <li><strong>מעבורת</strong> לאפשרויות יומיות, העברת רכב והגעה יפה לבירה.</li>
  <li><strong>טיסה</strong> כשזמן דלת לדלת חשוב יותר מהמחיר ויש מקומות בתאריכים שלכם.<sup><a href="#ref3">[3]</a></sup></li>
  <li><strong>השאירו מרווח</strong> משדה התעופה של אתונה לפיראוס אם נוחתים ב-ATH ושטים באותו יום.<sup><a href="#ref1">[1]</a></sup></li>
</ol>
<div class="svs-callout">
  <strong>נוחתים ומתמקמים ליד הים</strong>
  אחרי ארמופולי מגיעה ההחלטה על הבסיס. Sea View Serenity הוא בית על חוף המערבי ליד חוף דלפיני — מצוין אחרי יום מעבורת, כשחשובים מים שקטים ומטבח מלא.
  <a class="svs-cta" href="BOOK">הזמינו את השהייה בסירוס</a>
</div>
<h2>סדר הזמנה ששומר על החופשה</h2>
<p>קבעו קודם את <strong>הלינה</strong> בשבועות עמוסים, אחר כך מעבורת/טיסה, ואז השכרת רכב במידת הצורך. הים האגאי הדרומי עדיין האזור העמוס ביותר בלינות — בתים פופולריים על הים ומקומות לרכב במעבורת מתמלאים באמצע הקיץ.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
    }

def family_vacation():
    return {
        "el": {
            "title": "Οικογενειακές διακοπές στη Σύρο: παραλίες, χώρος και συμβουλές για σπίτι στην ακτή | Sea View Serenity",
            "description": "Οργανώστε οικογενειακές διακοπές στη Σύρο με ήσυχες παραλίες, πρακτικό checklist βίλας και βάση στη δυτική ακτή κοντά στο Δελφίνι και το Κίνι.",
            "keywords": "οικογενειακές διακοπές Σύρος, διακοπές με παιδιά Ελλάδα, Σύρος με παιδιά, βίλα οικογένεια Σύρος, παραθαλάσσιο σπίτι οικογένεια",
            "kicker": KICKER["el"],
            "hero_alt": "Παραλία Γαλησσάς στη Σύρο",
            "hero_caption": "Παραλία Γαλησσάς — μεγάλος αμμώδης κόλπος δημοφιλής σε οικογένειες.",
            "mid_alt": "Υπνοδωμάτιο με μπαλκόνι και θέα στο Αιγαίο",
            "mid_caption": "Ξεχωριστά υπνοδωμάτια και πρωινό με θαλάσσιο αέρα βοηθούν πολυμελείς οικογένειες να ξεκουράζονται.",
            "body": """<p>Οικογένειες που αναζητούν <strong>«Σύρος με παιδιά»</strong> ή <strong>«οικογενειακές διακοπές στην Ελλάδα»</strong> συνήθως θέλουν τρία πράγματα: ασφαλέστερο κολύμπι, αρκετούς χώρους για χαλάρωση και κουζίνα που να μην κάνει κάθε γεύμα logistics project.</p>
<h2>Ποιες παραλίες της Σύρου ταιριάζουν σε οικογένειες;</h2>
<p>Στο νότιο τμήμα οι παραλίες είναι συνήθως πιο προστατευμένες από τα μελτέμια, με ρηχά νερά στον Αγαθόπη και εύκολη πρόσβαση στη Γαλησσά. Στα δυτικά, το Κίνι προσφέρει προστατευμένο αμμώδη κόλπο· κοντά, Δελφίνι και Βαρβαρoύσα είναι μικρότερα και ήσυχα.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-bedroom-balcony.jpg" alt="Υπνοδωμάτιο με μπαλκόνι και θέα στο Αιγαίο" loading="lazy" width="1200" height="675" />
  <figcaption>Ξεχωριστά υπνοδωμάτια και πρωινό με θαλάσσιο αέρα βοηθούν πολυμελείς οικογένειες να ξεκουράζονται.</figcaption>
</figure>
<p>Η μίξη βοηθά: ήσυχος κόλπος το πρωί, μεγαλύτερος οργανωμένος κόλπος όταν τα παιδιά θέλουν ομπρέλες, χώρο και μεγάλη μέρα στην παραλία.</p>
<h2>Γιατί ένα παραθαλάσσιο σπίτι είναι καλύτερο από στενό δωμάτιο ξενοδοχείου</h2>
<p>Οι βραχυχρόνιες μισθώσεις είναι πλέον οικιακού τύπου προϊόν για εμπειρίες που ζητούν οικογένειες και πολυγενεαλικές ομάδες.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>Κουζίνα + ψυγείο:</strong> πρωινό και σνακ για τα παιδιά στο δικό σας ρυθμό</li>
  <li><strong>Πλυντήριο:</strong> πετσέτες παραλίας και ρούχα με άμμο χωρίς πανικό</li>
  <li><strong>Πάρκινγκ:</strong> αλλαγή παραλίας χωρίς ταξί κάθε πρωί</li>
  <li><strong>Ξεχωριστοί χώροι ύπνου:</strong> νωρίς στο κρεβάτι χωρίς να τελειώνει η βραδιά για όλους</li>
</ul>
<h2>Ρυθμός ημέρας έτοιμος για οικογένεια στη Σύρο</h2>
<ol>
  <li>Πρωινό κολύμπι σε προστατευμένο κόλπο (περιοχή Δελφίνι / Κίνι).<sup><a href="#ref1">[1]</a></sup></li>
  <li>Μεσημέρι πίσω στο σπίτι για γεύμα και σκιά.</li>
  <li>Απόγευμα παγωτό ή σύντομος περίπατος στην Ερμούπολη — η πρωτεύουσα μένει ζωντανή και πεζοδρομήσιμη.<sup><a href="#ref3">[3]</a></sup></li>
  <li>Νωρίς δείπνο δίπλα στο νερό για ήρεμο κλείσιμο ημέρας.</li>
</ol>
<div class="svs-callout">
  <strong>Οικογενειακή βάση κοντά στο Δελφίνι</strong>
  Το Sea View Serenity είναι οργανωμένο για οικογένειες και ομάδες: θέα στη θάλασσα, πλήρης κουζίνα, πάρκινγκ, πλυντήριο και σύντομος δρόμος για την παραλία Δελφίνι.
  <a class="svs-cta" href="BOOK">Δείτε διαθεσιμότητα</a>
</div>
<h2>Συμβουλή κράτησης για εβδομάδες σχολικών διακοπών</h2>
<p>Η καλοκαιρινή ζήτηση συγκεντρώνεται ακόμη στον Ιούλιο και Αύγουστο — κλείστε νωρίς· Μάιος–Ιούνιος ή Σεπτέμβριος είναι καλές εναλλακτικές αν το σχολικό ημερολόγιο το επιτρέπει.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
        "fr": {
            "title": "Vacances en famille à Syros : plages, espace et conseils pour une maison en bord de mer | Sea View Serenity",
            "description": "Organisez des vacances familiales à Syros : plages calmes, checklist villa pratique et base sur la côte ouest près de Delfini et Kini.",
            "keywords": "vacances famille Syros, vacances enfants Grèce, Syros avec enfants, villa famille Syros, maison bord de mer famille",
            "kicker": KICKER["fr"],
            "hero_alt": "Plage de Galissas à Syros, Grèce",
            "hero_caption": "Galissas — grande baie de sable prisée des familles.",
            "mid_alt": "Chambre avec balcon et vue sur la mer Égée",
            "mid_caption": "Chambres séparées et matinées face à la mer aident les familles nombreuses à vraiment se reposer.",
            "body": """<p>Les familles qui tapent <strong>« Syros avec enfants »</strong> ou <strong>« vacances famille Grèce bord de mer »</strong> veulent en général trois choses : baignade plus sûre, assez d’espace pour décompresser et une cuisine qui évite de transformer chaque repas en logistique.</p>
<h2>Quelles plages de Syros conviennent aux familles ?</h2>
<p>Au sud, les plages sont souvent plus abritées du meltemi, avec eaux peu profondes à Agathopes et un grand accès facile à Galissas. À l’ouest, Kini offre une crique sablonneuse protégée ; Delfini et Varvarousa, plus petites et plus calmes, sont tout près.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-bedroom-balcony.jpg" alt="Chambre avec balcon et vue sur la mer Égée" loading="lazy" width="1200" height="675" />
  <figcaption>Chambres séparées et matinées face à la mer aident les familles nombreuses à vraiment se reposer.</figcaption>
</figure>
<p>Mélangez : crique paisible le matin, grande baie organisée quand les enfants veulent parasols, espace et longues journées plage.</p>
<h2>Pourquoi une maison en bord de mer vaut mieux qu’une chambre d’hôtel serrée</h2>
<p>Les locations courte durée offrent le confort résidentiel que recherchent voyages multi-générations et familles nombreuses en haute saison.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>Cuisine + frigo :</strong> petit-déjeuner et goûters à votre rythme</li>
  <li><strong>Lave-linge :</strong> serviettes de plage et vêtements sableux sans stress</li>
  <li><strong>Parking :</strong> changer de plage sans calculer un taxi chaque matin</li>
  <li><strong>Couchages séparés :</strong> coucher tôt les enfants sans couper la soirée des adultes</li>
</ul>
<h2>Rythme d’une journée famille à Syros</h2>
<ol>
  <li>Baignade matinale dans une crique abritée (secteur Delfini / Kini).<sup><a href="#ref1">[1]</a></sup></li>
  <li>Retour à la maison à midi pour déjeuner et ombre.</li>
  <li>Glace ou courte balade à Ermoupoli l’après-midi — la capitale reste vivante et piétonne.<sup><a href="#ref3">[3]</a></sup></li>
  <li>Dîner tôt au bord de l’eau pour finir la journée en douceur.</li>
</ol>
<div class="svs-callout">
  <strong>Base familiale près de Delfini</strong>
  Sea View Serenity est pensé pour familles et groupes : vue mer, cuisine équipée, parking, buanderie et accès court à la plage de Delfini.
  <a class="svs-cta" href="BOOK">Vérifier les dates</a>
</div>
<h2>Réserver pendant les vacances scolaires</h2>
<p>La demande estivale se concentre encore en juillet–août : réservez tôt ; mai–juin ou septembre sont d’excellentes alternatives si le calendrier scolaire le permet.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
        "de": {
            "title": "Familienurlaub auf Syros: Strände, Platz und Tipps fürs Haus am Meer | Sea View Serenity",
            "description": "Planen Sie einen Familienurlaub auf Syros mit ruhigen Stränden, praktischer Villa-Checkliste und Westküsten-Basis nahe Delfini und Kini.",
            "keywords": "Familienurlaub Syros, Urlaub mit Kindern Griechenland, Syros mit Kindern, Familienvilla Syros, Ferienhaus Familie Meer",
            "kicker": KICKER["de"],
            "hero_alt": "Strand Galissas auf Syros, Griechenland",
            "hero_caption": "Galissas — große Sandbucht, beliebt bei Familien.",
            "mid_alt": "Schlafzimmer mit Balkon und Ägäis-Blick",
            "mid_caption": "Getrennte Schlafzimmer und Morgenluft am Meer helfen größeren Familien wirklich auszuruhen.",
            "body": """<p>Wer <strong>„Syros mit Kindern“</strong> oder <strong>„Familienurlaub Griechenland Meer“</strong> sucht, braucht meist drei Dinge: sichereres Schwimmen, genug Raum zum Abschalten und eine Küche, die nicht jedes Essen zum Logistikprojekt macht.</p>
<h2>Welche Strände auf Syros passen für Familien?</h2>
<p>Im Süden sind Strände oft besser vor dem Meltemi geschützt, mit flachem Wasser in Agathopes und leichtem Zugang in Galissas. Im Westen bietet Kini eine geschützte Sandbucht; Delfini und Varvarousa sind kleiner und ruhiger.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-bedroom-balcony.jpg" alt="Schlafzimmer mit Balkon und Ägäis-Blick" loading="lazy" width="1200" height="675" />
  <figcaption>Getrennte Schlafzimmer und Morgenluft am Meer helfen größeren Familien wirklich auszuruhen.</figcaption>
</figure>
<p>Morgens ruhige Bucht, später größere organisierte Bucht, wenn Kinder Schirme, Platz und lange Strandtage wollen.</p>
<h2>Warum ein Haus am Meer besser ist als ein enges Hotelzimmer</h2>
<p>Kurzzeitmieten sind das Wohngefühl, das Mehrgenerationen- und Kinderreisen in der Hochsaison brauchen.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>Küche + Kühlschrank:</strong> Frühstück und Snacks nach eigenem Takt</li>
  <li><strong>Waschmaschine:</strong> Handtücher und Sandwäsche ohne Drama</li>
  <li><strong>Parkplatz:</strong> Strandhopping ohne jeden Morgen Taxi-Rechnung</li>
  <li><strong>Getrennte Schlafbereiche:</strong> frühes Zubettgehen der Kinder, ohne den Abend für alle zu beenden</li>
</ul>
<h2>Ein familienfreundlicher Tagesrhythmus auf Syros</h2>
<ol>
  <li>Morgenschwimmen in geschützter Bucht (Delfini / Kini).<sup><a href="#ref1">[1]</a></sup></li>
  <li>Mittags zurück ins Haus zu Essen und Schatten.</li>
  <li>Nachmittags Eis oder kurzer Spaziergang in Ermoupoli.<sup><a href="#ref3">[3]</a></sup></li>
  <li>Frühes Abendessen am Wasser — ruhiger Tagesausklang.</li>
</ol>
<div class="svs-callout">
  <strong>Familienbasis nahe Delfini</strong>
  Sea View Serenity ist für Familien und Gruppen eingerichtet: Meerblick, volle Küche, Parkplatz, Wäsche und kurzer Weg zum Strand Delfini.
  <a class="svs-cta" href="BOOK">Termine prüfen</a>
</div>
<h2>Buchungstipp für Schulferien</h2>
<p>Die Sommernachfrage ballt sich weiter in Juli und August — früh buchen; Mai–Juni oder September sind oft angenehmer, wenn der Schulplan mitspielt.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
        "it": {
            "title": "Vacanza in famiglia a Syros: spiagge, spazio e consigli per una casa sul mare | Sea View Serenity",
            "description": "Organizza una vacanza familiare a Syros con spiagge tranquille, checklist pratica per la villa e base sulla costa occidentale vicino a Delfini e Kini.",
            "keywords": "vacanza famiglia Syros, vacanza bambini Grecia, Syros con bambini, villa famiglia Syros, casa sul mare famiglia",
            "kicker": KICKER["it"],
            "hero_alt": "Spiaggia di Galissas a Syros, Grecia",
            "hero_caption": "Galissas — ampia baia sabbiosa molto scelta dalle famiglie.",
            "mid_alt": "Camera da letto con balcone e vista sull'Egeo",
            "mid_caption": "Camere separate e mattinate di brezza marina aiutano le famiglie numerose a riposare davvero.",
            "body": """<p>Chi cerca <strong>«Syros con bambini»</strong> o <strong>«vacanza famiglia Grecia mare»</strong> vuole di solito tre cose: nuotate più tranquille, spazio per rilassarsi e una cucina che non trasformi ogni pasto in un progetto logistico.</p>
<h2>Quali spiagge di Syros vanno bene per le famiglie?</h2>
<p>A sud le spiagge sono spesso più riparate dal meltemi, con acque basse ad Agathopes e accesso facile a Galissas. A ovest, Kini offre una cala sabbiosa protetta; Delfini e Varvarousa, più piccole e silenziose, sono vicine.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-bedroom-balcony.jpg" alt="Camera da letto con balcone e vista sull'Egeo" loading="lazy" width="1200" height="675" />
  <figcaption>Camere separate e mattinate di brezza marina aiutano le famiglie numerose a riposare davvero.</figcaption>
</figure>
<p>Alterna cala tranquilla al mattino e baia organizzata quando i bambini vogliono ombrelloni, spazio e giornate lunghe in spiaggia.</p>
<h2>Perché una casa sul mare batte una camera d’hotel stretta</h2>
<p>Le locazioni brevi offrono il comfort abitativo che cercano viaggi multigenerazionali e famiglie numerose in alta stagione.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>Cucina + frigo:</strong> colazione e snack per i bambini ai vostri orari</li>
  <li><strong>Lavatrice:</strong> teli mare e vestiti sabbiosi senza panico</li>
  <li><strong>Parcheggio:</strong> cambio spiaggia senza taxi ogni mattina</li>
  <li><strong>Zone notte separate:</strong> nanna presto senza chiudere la serata per tutti</li>
</ul>
<h2>Ritmo di una giornata family a Syros</h2>
<ol>
  <li>Nuotata mattutina in cala riparata (zona Delfini / Kini).<sup><a href="#ref1">[1]</a></sup></li>
  <li>Rientro a casa a mezzogiorno per pranzo e ombra.</li>
  <li>Gelato o breve passeggiata a Ermoupoli nel pomeriggio.<sup><a href="#ref3">[3]</a></sup></li>
  <li>Cena presto sull’acqua per chiudere la giornata con calma.</li>
</ol>
<div class="svs-callout">
  <strong>Base familiare vicino a Delfini</strong>
  Sea View Serenity è pensato per famiglie e gruppi: vista mare, cucina completa, parcheggio, lavanderia e breve distanza dalla spiaggia di Delfini.
  <a class="svs-cta" href="BOOK">Controlla le date</a>
</div>
<h2>Prenotare nelle settimane di scuola chiusa</h2>
<p>La domanda estiva resta concentrata a luglio–agosto: prenotate presto; maggio–giugno o settembre sono ottime alternative se il calendario scolastico lo consente.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
        "he": {
            "title": "חופשה משפחתית בסירוס: חופים, מרחב וטיפים לבית על הים | Sea View Serenity",
            "description": "תכננו חופשה משפחתית בסירוס עם חופים רגועים, רשימת בדיקה מעשית לווילה ובסיס בחוף המערבי ליד דלפיני וקיני.",
            "keywords": "חופשה משפחתית סירוס, חופשה עם ילדים יוון, סירוס עם ילדים, וילה משפחה סירוס, בית על הים משפחה",
            "kicker": KICKER["he"],
            "hero_alt": "חוף גליסאס בסירוס, יוון",
            "hero_caption": "גליסאס — מפרץ חולי גדול שאהוב על משפחות.",
            "mid_alt": "חדר שינה עם מרפסת ונוף לים האגאי",
            "mid_caption": "חדרי שינה נפרדים ובקרים עם אוויר ים עוזרים למשפחות גדולות באמת לנוח.",
            "body": """<p>משפחות שמחפשות <strong>«סירוס עם ילדים»</strong> או <strong>«חופשה משפחתית יוון על הים»</strong> צריכות בדרך כלל שלושה דברים: שחייה בטוחה יותר, מספיק מקום להירגע ומטבח שלא הופך כל ארוחה לפרויקט לוגיסטי.</p>
<h2>אילו חופים בסירוס מתאימים למשפחות?</h2>
<p>בדרום החופים מוגנים לרוב יותר ממלטמי, עם מים רדודים באגתופס וגישה נוחה לגליסאס. במערב, קיני מציע מפרץ חולי מוגן; דלפיני וורבורוסה קטנים ושקטים יותר בקרבת מקום.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-bedroom-balcony.jpg" alt="חדר שינה עם מרפסת ונוף לים האגאי" loading="lazy" width="1200" height="675" />
  <figcaption>חדרי שינה נפרדים ובקרים עם אוויר ים עוזרים למשפחות גדולות באמת לנוח.</figcaption>
</figure>
<p>שלבו: מפרץ רגוע בבוקר, מפרץ מאורגן גדול יותר כשהילדים רוצים מטריות, מרחב ויום חוף ארוך.</p>
<h2>למה בית על הים עדיף על חדר מלון צפוף</h2>
<p>שכירויות לטווח קצר נותנות את הנוחות הביתית שמחפשות משפחות רב-דוריות ועמוסות ילדים בעונה השיאית.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
  <li><strong>מטבח + מקרר:</strong> ארוחת בוקר וחטיפים לילדים בקצב שלכם</li>
  <li><strong>כביסה:</strong> מגבות חוף ובגדים מלאי חול בלי לחץ</li>
  <li><strong>חניה:</strong> מעבר בין חופים בלי מונית כל בוקר</li>
  <li><strong>אזורי שינה נפרדים:</strong> שינה מוקדמת לילדים בלי לסיים את הערב לכולם</li>
</ul>
<h2>קצב יום משפחתי מוכן בסירוס</h2>
<ol>
  <li>שחייה בבוקר במפרץ מוגן (אזור דלפיני / קיני).<sup><a href="#ref1">[1]</a></sup></li>
  <li>חזרה הביתה בצהריים לארוחה וצל.</li>
  <li>גלידה או טיול קצר בארמופולי אחר הצהריים.<sup><a href="#ref3">[3]</a></sup></li>
  <li>ארוחת ערב מוקדמת ליד המים לסיום רגוע.</li>
</ol>
<div class="svs-callout">
  <strong>בסיס משפחתי ליד דלפיני</strong>
  Sea View Serenity מותאם למשפחות ולקבוצות: נוף לים, מטבח מלא, חניה, כביסה וטיול קצר לחוף דלפיני.
  <a class="svs-cta" href="BOOK">בדקו תאריכים</a>
</div>
<h2>טיפ להזמנה בשבועות חופשת בית ספר</h2>
<p>הביקוש הקיצוני מתרכז עדיין ביולי–אוגוסט — הזמינו מוקדם; מאי–יוני או ספטמבר הם חלופות נוחות אם לוח הלימודים מאפשר.<sup><a href="#ref4">[4]</a></sup></p>""",
        },
    }

def ermoupoli_itinerary():
    return {
        "el": {
            "title": "Ερμούπολη + παραλία: ενδρομολόγιο μίας ημέρας στη Σύρο που χωράει στην πράξη | Sea View Serenity",
            "description": "Συνδυάστε το νεοκλασικό κέντρο της Ερμούπολης με κολύμπι στη δυτική ακτή — εύκολο πρόγραμμα ημέρας για όσους μένουν σε ενοικιαζόμενο στην ακτή.",
            "keywords": "τι να κάνω στη Σύρο, ενδρομολόγιο Ερμούπολη, ημερήσια εκδρομή Σύρος, Άνω Σύρος, πόλη και παραλία Σύρος",
            "kicker": KICKER["el"],
            "hero_alt": "Θέα της Ερμούπολης στη Σύρο",
            "hero_caption": "Η Ερμούπολη, πρωτεύουσα της Σύρου — νεοκλασική πόλη-λιμάνι.",
            "mid_alt": "Παραλία Δελφίνι στη Σύρο",
            "mid_caption": "Παραλία Δελφίνι — ήσυχος κόλπος στη δυτική ακτή.",
            "body": """<p>Μετά τη διαμονή, μία από τις πιο συχνές αναζητήσεις είναι <strong>«τι να κάνω στη Σύρο»</strong> — ειδικά για όσους θέλουν πολιτισμό <em>και</em> κολύμπι στο ίδιο ταξίδι. Η Ερμούπολη είναι στο κέντρο: νεοκλασικές οδούς, κληρονομιά ορθόδοξη και καθολική στους δίδυμους λόφους, φεστιβάλ και ζωντανή πόλη όλο το χρόνο.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Πρωί: Ερμούπολη χωρίς βιαστικό ρυθμό</h2>
<ul>
  <li>Ξεκινήστε από την πλατεία Μιαούλη και το νεοκλασικό κέντρο.</li>
  <li>Ανέβασμα προς την Άνω Σύρο για το μεσαιωνικό καθολικό τετράγωνο και θέα στο λιμάνι.<sup><a href="#ref1">[1]</a></sup></li>
  <li>Μουσεία/θέατρο προαιρετικά — η Σύρος τονίζει ζωντανή κουλτούρα παρά «μαραθώνιο» επισκέψεων.<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>Απόγευμα: εναλλαγή σε θάλασσα</h2>
<p>Μετά τον καφέ στην πόλη, κινηθείτε δυτικά. Το Κίνι προσφέρει προστατευμένη αμμώδη κόλπο και ατμόσφαιρα ηλιοβασιλέματος· το Δελφίνι και η Βαρβαρoύσα είναι μικρότερες επιλογές· η Γαλησσάς μεγαλύτερη οργανωμένη αμμώδης παραλία.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-delfini-beach.jpg" alt="Παραλία Δελφίνι στη Σύρο" loading="lazy" width="1200" height="675" />
  <figcaption>Παραλία Δελφίνι — ήσυχος κόλπος στη δυτική ακτή.</figcaption>
</figure>
<h2>Βράδυ: ένα λιμάνι ή έναν κόλπο — όχι και τα δύο γεμάτα</h2>
<p>Δείπνο δίπλα στη βάση σας στο νερό ή επιστροφή στην Ερμούπολη για βόλτα. Ως λειτουργική πρωτεύουσα, τα βράδια μένουν αυθεντικά.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<div class="svs-callout">
  <strong>Το πρόγραμμα δουλεύει καλύτερα από σπίτι στη δυτική ακτή</strong>
  Κοντά στο Δελφίνι δεν διασχίζετε το νησί δύο φορές για κάθε κολύμπι. Εξερευνήστε την Ερμούπολη όταν θέλετε πόλη· γυρίστε σε θέα θάλασσας.
  <a class="svs-cta" href="BOOK">Μείνετε κοντά στην παραλία</a>
</div>
<h2>Αναβάθμιση σε δύο ημέρες</h2>
<ol>
  <li><strong>Ημέρα 1:</strong> Ερμούπολη + Άνω Σύρος + ηλιοβασίλεμα στο Κίνι.</li>
  <li><strong>Ημέρα 2:</strong> Ήρεμο πρωί στο Δελφίνι, μετά νότιος αμμώδης κόλπος (Γαλησσάς ή Αγαθόπες).<sup><a href="#ref2">[2]</a></sup></li>
</ol>""",
        },
        "fr": {
            "title": "Ermoupoli + plage : itinéraire d’une journée à Syros qui tient la route | Sea View Serenity",
            "description": "Alliez le centre néoclassique d’Ermoupoli à une baignade sur la côte ouest — un programme facile pour les voyageurs en location au bord de la mer.",
            "keywords": "que faire à Syros, itinéraire Ermoupoli, excursion Syros, Ano Syros, ville et plage Syros",
            "kicker": KICKER["fr"],
            "hero_alt": "Vue d’Ermoupoli sur l’île de Syros, Grèce",
            "hero_caption": "Ermoupoli, capitale de Syros — ville-port néoclassique.",
            "mid_alt": "Plage de Delfini à Syros, Grèce",
            "mid_caption": "Delfini — crique plus calme sur la côte ouest.",
            "body": """<p>Après le logement, beaucoup tapent <strong>« que faire à Syros »</strong> — surtout pour mêler culture <em>et</em> baignade. Ermoupoli est au cœur du voyage : rues néoclassiques, double colline orthodoxe et catholique, festivals et ville vivante hors saison plage.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Matin : Ermoupoli sans course</h2>
<ul>
  <li>Départ place Miaouli et cœur civique néoclassique.</li>
  <li>Montée vers Ano Syros pour le quartier catholique médiéval et la vue sur le port.<sup><a href="#ref1">[1]</a></sup></li>
  <li>Musées/théâtre en option — Syros mise sur la culture vivante plutôt qu’un marathon de cases.<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>Après-midi : passez en mode mer</h2>
<p>Après le café en ville, filez à l’ouest. Kini offre une crique sablonneuse protégée et de beaux couchers ; Delfini et Varvarousa sont plus petites ; Galissas reste la grande baie organisée.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-delfini-beach.jpg" alt="Plage de Delfini à Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Delfini — crique plus calme sur la côte ouest.</figcaption>
</figure>
<h2>Soir : un port ou une crique — pas les deux bondés</h2>
<p>Dîner au bord de l’eau près de votre base ou retour à Ermoupoli pour une volta. Capitale administrative, les soirées sonnent locales.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<div class="svs-callout">
  <strong>Mieux depuis une maison sur la côte ouest</strong>
  Près de Delfini, vous ne traversez pas l’île deux fois pour chaque baignade. Ermoupoli quand vous voulez la ville ; retour face à la mer.
  <a class="svs-cta" href="BOOK">Séjourner près de la plage</a>
</div>
<h2>Version sur deux jours</h2>
<ol>
  <li><strong>Jour 1 :</strong> Ermoupoli + Ano Syros + coucher de soleil à Kini.</li>
  <li><strong>Jour 2 :</strong> Matinée lente à Delfini, puis baie sablonneuse au sud (Galissas ou Agathopes).<sup><a href="#ref2">[2]</a></sup></li>
</ol>""",
        },
        "de": {
            "title": "Ermoupoli + Strand: ein Tagesplan auf Syros, der wirklich passt | Sea View Serenity",
            "description": "Verbinden Sie Ermoupolis neoklassisches Zentrum mit einem Bad an der Westküste — ein leichter Tagesplan für Gäste in einer Unterkunft am Meer.",
            "keywords": "Syros Sehenswürdigkeiten, Ermoupoli Route, Tagesausflug Syros, Ano Syros, Stadt und Strand Syros",
            "kicker": KICKER["de"],
            "hero_alt": "Blick auf Ermoupoli auf Syros, Griechenland",
            "hero_caption": "Ermoupoli, Hauptstadt von Syros — neoklassische Hafenstadt.",
            "mid_alt": "Strand Delfini auf Syros, Griechenland",
            "mid_caption": "Delfini — ruhigere Bucht an der Westküste.",
            "body": """<p>Nach der Unterkunft kommt oft <strong>„was tun auf Syros“</strong> — wer Kultur <em>und</em> Schwimmen will. Ermoupoli steht im Mittelpunkt: neoklassische Straßen, orthodoxes und katholisches Erbe auf zwei Hügeln, Festivals und eine lebendige Stadt.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Vormittag: Ermoupoli ohne Hetze</h2>
<ul>
  <li>Start am Miaouli-Platz und im neoklassischen Zentrum.</li>
  <li>Aufstieg nach Ano Syros für das mittelalterliche katholische Viertel und Hafenblick.<sup><a href="#ref1">[1]</a></sup></li>
  <li>Museum/Theater optional — Syros setzt auf lebendige Kultur statt Checklisten-Marathon.<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>Nachmittag: Meer statt Stadt</h2>
<p>Nach dem Kaffee Richtung Westen. Kini bietet geschützte Sandbucht und Sonnenuntergang; Delfini und Varvarousa sind kleiner; Galissas die große organisierte Sandbucht.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-delfini-beach.jpg" alt="Strand Delfini auf Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Delfini — ruhigere Bucht an der Westküste.</figcaption>
</figure>
<h2>Abend: ein Hafen oder eine Bucht — nicht beides voll</h2>
<p>Abendessen am Wasser bei Ihrer Basis oder zurück nach Ermoupoli zur Volta. Als Verwaltungshauptstadt wirken Abende authentisch.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<div class="svs-callout">
  <strong>Am besten von einem Haus an der Westküste</strong>
  Nahe Delfini querieren Sie nicht zweimal die Insel fürs Schwimmen. Ermoupoli für Stadtlust — danach Meerblick zu Hause.
  <a class="svs-cta" href="BOOK">Nahe dem Strand übernachten</a>
</div>
<h2>Zwei-Tage-Upgrade</h2>
<ol>
  <li><strong>Tag 1:</strong> Ermoupoli + Ano Syros + Sonnenuntergang in Kini.</li>
  <li><strong>Tag 2:</strong> Ruhiger Morgen in Delfini, dann südliche Sandbucht (Galissas oder Agathopes).<sup><a href="#ref2">[2]</a></sup></li>
</ol>""",
        },
        "it": {
            "title": "Ermoupoli + spiaggia: itinerario di un giorno a Syros che funziona davvero | Sea View Serenity",
            "description": "Unite il centro neoclassico di Ermoupoli a un tuffo sulla costa occidentale — piano facile per chi soggiorna in una casa sul mare.",
            "keywords": "cosa fare a Syros, itinerario Ermoupoli, gita Syros, Ano Syros, città e spiaggia Syros",
            "kicker": KICKER["it"],
            "hero_alt": "Vista di Ermoupoli sull'isola di Syros, Grecia",
            "hero_caption": "Ermoupoli, capitale di Syros — città-porto neoclassica.",
            "mid_alt": "Spiaggia di Delfini a Syros, Grecia",
            "mid_caption": "Delfini — cala più tranquilla sulla costa occidentale.",
            "body": """<p>Dopo l’alloggio, spesso si cerca <strong>«cosa fare a Syros»</strong> — soprattutto per unire cultura <em>e</em> mare. Ermoupoli è al centro: strade neoclassiche, eredità ortodossa e cattolica sulle colline gemelle, festival e città viva tutto l’anno.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Mattina: Ermoupoli senza fretta</h2>
<ul>
  <li>Partenza da piazza Miaouli e centro civico neoclassico.</li>
  <li>Salita verso Ano Syros per il quartiere cattolico medievale e la vista sul porto.<sup><a href="#ref1">[1]</a></sup></li>
  <li>Musei/teatro opzionali — Syros punta sulla cultura viva, non sul maratona di checklist.<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>Pomeriggio: modalità mare</h2>
<p>Dopo il caffè in città, verso ovest. Kini offre cala sabbiosa protetta e tramonto; Delfini e Varvarousa sono più piccole; Galissas la grande baia organizzata.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-delfini-beach.jpg" alt="Spiaggia di Delfini a Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Delfini — cala più tranquilla sulla costa occidentale.</figcaption>
</figure>
<h2>Sera: un porto o una cala — non entrambi affollati</h2>
<p>Cena sull’acqua vicino alla base o ritorno a Ermoupoli per una volta. Capitale amministrativa, le serate restano autentiche.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<div class="svs-callout">
  <strong>Funziona meglio da una casa sulla costa occidentale</strong>
  Vicino a Delfini non attraversate l’isola due volte per ogni bagno. Ermoupoli quando volete città; poi vista mare a casa.
  <a class="svs-cta" href="BOOK">Soggiorna vicino alla spiaggia</a>
</div>
<h2>Estensione a due giorni</h2>
<ol>
  <li><strong>Giorno 1:</strong> Ermoupoli + Ano Syros + tramonto a Kini.</li>
  <li><strong>Giorno 2:</strong> Mattina lenta a Delfini, poi baia sabbiosa a sud (Galissas o Agathopes).<sup><a href="#ref2">[2]</a></sup></li>
</ol>""",
        },
        "he": {
            "title": "ארמופולי + חוף: מסלול יום אחד בסירוס שבאמת עובד | Sea View Serenity",
            "description": "שלבו את המרכז הניאוקלאסי של ארמופולי עם שחייה בחוף המערבי — תוכנית יום קלה למי שנשאר בשכירות על הים.",
            "keywords": "מה לעשות בסירוס, מסלול ארמופולי, טיול יום סירוס, אנו סירוס, עיר וחוף סירוס",
            "kicker": KICKER["he"],
            "hero_alt": "נוף לארמופולי באי סירוס, יוון",
            "hero_caption": "ארמופולי, בירת סירוס — עיר נמל ניאוקלאסית.",
            "mid_alt": "חוף דלפיני בסירוס, יוון",
            "mid_caption": "דלפיני — מפרץ שקט יותר בחוף המערבי.",
            "body": """<p>אחרי בחירת הלינה, חיפוש נפוץ הוא <strong>«מה לעשות בסירוס»</strong> — במיוחד למי שרוצה תרבות <em>וגם</em> שחייה. ארמופולי במרכז: רחובות ניאוקלאסיים, מורשת אורתודוקסית וקתולית על גבעות תאומות, פסטיבלים ועיר חיה כל השנה.<sup><a href="#ref1">[1]</a></sup></p>
<h2>בוקר: ארמופולי בלי למהר</h2>
<ul>
  <li>התחילו בכיכר מיאולי ובמרכז האזרחי הניאוקלאסי.</li>
  <li>עלו לאנו סירוס לרובע הקתולי הביניימי ולנוף על הנמל.<sup><a href="#ref1">[1]</a></sup></li>
  <li>מוזיאונים/תיאטרון אופציונליים — סירוס מדגישה תרבות חיה ולא מרתון רשימות.<sup><a href="#ref1">[1]</a></sup></li>
</ul>
<h2>אחר הצהריים: מעבר למצב ים</h2>
<p>אחרי קפה בעיר, ימינה למערב. קיני מציע מפרץ חולי מוגן ושקיעות; דלפיני וורבורוסה קטנים יותר; גליסאס המפרץ החולי המאורגן הגדול.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-delfini-beach.jpg" alt="חוף דלפיני בסירוס" loading="lazy" width="1200" height="675" />
  <figcaption>דלפיני — מפרץ שקט יותר בחוף המערבי.</figcaption>
</figure>
<h2>ערב: נמל אחד או מפרץ אחד — לא שניהם עמוסים</h2>
<p>ארוחת ערב על המים ליד הבסיס או חזרה לארמופולי לסיבוב. כבירה מנהלית, הערבים מרגישים מקומיים.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<div class="svs-callout">
  <strong>המסלול עובד טוב יותר מבית בחוף המערבי</strong>
  ליד דלפיני לא חוצים את האי פעמיים לכל שחייה. ארמופולי כשאתם רוצים עיר; חוזרים לנוף ים.
  <a class="svs-cta" href="BOOK">לינה ליד החוף</a>
</div>
<h2>שדרוג ליומיים</h2>
<ol>
  <li><strong>יום 1:</strong> ארמופולי + אנו סירוס + שקיעה בקיני.</li>
  <li><strong>יום 2:</strong> בוקר רגוע בדלפיני, ואז מפרץ חולי בדרום (גליסאס או אגתופס).<sup><a href="#ref2">[2]</a></sup></li>
</ol>""",
        },
    }

def syros_food():
    return {
        "el": {
            "title": "Οδηγός φαγητού στη Σύρο για επισκέπτες βίλας: αγορές, λουκούμι και ταβέρνες στην ακτή | Sea View Serenity",
            "description": "Τι να φάτε στη Σύρο — από τυρί ΠΟΠ Σαν Μιχάλη και λουκούμι μέχρι θαλασσινά — όταν έχετε κουζίνα και θέλετε γεύση τόπου.",
            "keywords": "φαγητό Σύρος, λουκούμι Σύρος, τυρί Σαν Μιχάλη, που να φάτε Σύρο, γαστρονομία Σύρος, αγορές βίλα",
            "kicker": KICKER["el"],
            "hero_alt": "Καφές με λουκούμι",
            "hero_caption": "Καφές με λουκούμι — το γλυκό για το οποίο φημίζεται η Σύρος.",
            "mid_alt": "Κουζίνα βίλας έτοιμη για μαγείρεμα στη Σύρο",
            "mid_caption": "Πρακτική κουζίνα μετατρέπει αγορές και Σαν Μιχάλη σε δείπνο στη βεράντα.",
            "body": """<p>Αν κλείσατε βίλα με κουζίνα, το φαγητό γίνεται μέρος του σχεδιασμού των διακοπών. Η Σύρος ξεχωρίζει: γαστρονομία θαλάσσιας παράδοσης και εμπορικής κουλτούρας της Ερμούπολης — τυριά, αλλαντικά και γλυκά με ταυτότητα.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Τι να βάλετε στο καλάθι</h2>
<ul>
  <li><strong>Σαν Μιχάλη ΠΟΠ:</strong> σκληρό τυρί αγελαδινό, πικάντικο, με καρύδια — χαρακτηριστικό του νησιού.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Λουκούμι:</strong> ροδό, μαστίχα, περγαμόντι και άλλα, παραδοσιακή παραγωγή γενεών.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup></li>
  <li><strong>Χαλβαδόπιτα:</strong> γλυκό τύπου nougat, ιδανικό για δώρο.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Λούζα και λουκάνικα:</strong> αλλαντικά που κάνουν απλό δείπνο στη βίλα τοπικό.<sup><a href="#ref2">[2]</a></sup></li>
</ul>
<h2>Βράδια κουζίνας vs βράδια ταβέρνας</h2>
<p>Καλός ρυθμός: δύο δείπνα στο σπίτι, μία ταβέρνα θαλασσινών δίπλα στο νερό και μια περιπέτεια φαγητού στην Ερμούπολη.<sup><a href="#ref3">[3]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="Κουζίνα βίλας έτοιμη για μαγείρεμα στη Σύρο" loading="lazy" width="1200" height="675" />
  <figcaption>Πρακτική κουζίνα μετατρέπει αγορές και Σαν Μιχάλη σε δείπνο στη βεράντα.</figcaption>
</figure>
<h2>Γιατί η γαστρονομία ενισχύει την επιλογή σπιτιού</h2>
<p>Όσοι ψάχνουν «βίλα με κουζίνα Σύρος» ή «αυτοεξυπηρέτηση Κυκλάδες» θέλουν ευελιξία μαγειρικής — η ταυτότητα προϊόντων της Σύρου δίνει λόγο extra για σπίτι αντί για μόνο δωμάτιο.<sup><a href="#ref1">[1]</a></sup></p>
<div class="svs-callout">
  <strong>Μαγειρέψτε με θέα θάλασσας</strong>
  Η πλήρης κουζίνα του Sea View Serenity φτιάχτηκε γι’ αυτό: αγορές το πρωί, παραλία το μεσημέρι, δείπνο στη βεράντα το βράδυ.
  <a class="svs-cta" href="BOOK">Κλείστε το σπίτι</a>
</div>""",
        },
        "fr": {
            "title": "Guide gastronomique de Syros pour hôtes en villa : marchés, loukoumi et tavernes en bord de mer | Sea View Serenity",
            "description": "Que manger à Syros — fromage AOP San Michali, loukoumi et fruits de mer — quand vous avez une cuisine et voulez le goût local.",
            "keywords": "cuisine Syros, loukoumi Syros, fromage San Michali, où manger Syros, gastronomie Syros, courses villa",
            "kicker": KICKER["fr"],
            "hero_alt": "Café servi avec loukoumi",
            "hero_caption": "Café et loukoumi — la douceur emblématique de Syros.",
            "mid_alt": "Cuisine de villa prête pour cuisiner à Syros",
            "mid_caption": "Une vraie cuisine transforme le marché et le San Michali en dîner sur la terrasse.",
            "body": """<p>Avec une villa et sa cuisine, la nourriture devient partie du voyage. Syros se démarque : tradition maritime et culture commerçante d’Ermoupoli — fromages, charcuteries et douceurs identitaires.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Sur la liste des courses</h2>
<ul>
  <li><strong>San Michali AOP :</strong> fromage de vache ferme, piquant et noisetté — signature de l’île.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Loukoumi :</strong> rose, mastic, bergamote et autres saveurs, savoir-faire de générations.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup></li>
  <li><strong>Halvadopita :</strong> nougat local, parfait en cadeau.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Louza et saucissons :</strong> charcuterie qui localise un simple souper à la villa.<sup><a href="#ref2">[2]</a></sup></li>
</ul>
<h2>Soirs cuisine vs soirs taverne</h2>
<p>Bon rythme : deux dîners maison, une taverne de poisson au bord de l’eau et une balade gourmande à Ermoupoli.<sup><a href="#ref3">[3]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="Cuisine de villa prête pour cuisiner à Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Une vraie cuisine transforme le marché et le San Michali en dîner sur la terrasse.</figcaption>
</figure>
<h2>Pourquoi la gastronomie pousse vers une maison</h2>
<p>Qui cherche « villa avec cuisine Syros » ou « autonome Cyclades » veut de la flexibilité — l’identité produit de Syros renforce le choix d’une maison plutôt qu’une chambre seule.<sup><a href="#ref1">[1]</a></sup></p>
<div class="svs-callout">
  <strong>Cuisiner face à la mer</strong>
  La cuisine complète de Sea View Serenity est faite pour cela : marché le matin, plage l’après-midi, long dîner en terrasse le soir.
  <a class="svs-cta" href="BOOK">Réserver la maison</a>
</div>""",
        },
        "de": {
            "title": "Syros-Foodguide für Villagäste: Märkte, Loukoumi und Tavernen am Meer | Sea View Serenity",
            "description": "Was man auf Syros isst — PDO-Käse San Michali, Loukoumi und Meeresfrüchte — wenn Sie eine Küche haben und lokal essen wollen.",
            "keywords": "Essen Syros, Loukoumi Syros, Käse San Michali, wo essen Syros, Gastronomie Syros, Einkauf Villa",
            "kicker": KICKER["de"],
            "hero_alt": "Kaffee mit Loukoumi",
            "hero_caption": "Kaffee mit Loukoumi — die Süßigkeit, für die Syros bekannt ist.",
            "mid_alt": "Villaküche bereit zum Kochen auf Syros",
            "mid_caption": "Eine echte Küche macht aus Markteinkauf und San Michali ein Terrassenabendessen.",
            "body": """<p>Mit Villa und Küche wird Essen Teil der Reiseplanung. Syros überzeugt: maritime Tradition und Handelskultur Ermoupolis — Käse, Wurst und Süßes mit Identität.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Auf die Einkaufsliste</h2>
<ul>
  <li><strong>San Michali PDO:</strong> fester Kuhkäse, würzig und nussig — Insel-Klassiker.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Loukoumi:</strong> Rose, Mastix, Bergamotte u. a., Generationen-Tradition.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup></li>
  <li><strong>Halvadopita:</strong> Nougat-Süßigkeit, ideal als Mitbringsel.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Louza und Würste:</strong> Wurstwaren für ein lokales Villa-Abendessen.<sup><a href="#ref2">[2]</a></sup></li>
</ul>
<h2>Küchenabende vs Tavernenabende</h2>
<p>Guter Rhythmus: zwei Abendessen zu Hause, eine Fischtaverne am Wasser und ein Essgang durch Ermoupoli.<sup><a href="#ref3">[3]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="Villaküche bereit zum Kochen auf Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Eine echte Küche macht aus Markteinkauf und San Michali ein Terrassenabendessen.</figcaption>
</figure>
<h2>Warum Gastronomie für ein Haus spricht</h2>
<p>Wer «Villa mit Küche Syros» oder «Selbstverpflegung Kykladen» sucht, will Kochflexibilität — Syros’ Produkte machen ein Haus attraktiver als nur ein Zimmer.<sup><a href="#ref1">[1]</a></sup></p>
<div class="svs-callout">
  <strong>Kochen mit Meerblick</strong>
  Die volle Küche von Sea View Serenity ist dafür gebaut: Markt am Morgen, Strand mittags, langes Terrassendinner abends.
  <a class="svs-cta" href="BOOK">Haus buchen</a>
</div>""",
        },
        "it": {
            "title": "Guida al cibo di Syros per ospiti in villa: mercati, loukoumi e taverne sul mare | Sea View Serenity",
            "description": "Cosa mangiare a Syros — formaggio DOP San Michali, loukoumi e pesce — quando avete la cucina e volete sapore locale.",
            "keywords": "cibo Syros, loukoumi Syros, formaggio San Michali, dove mangiare Syros, gastronomia Syros, spesa villa",
            "kicker": KICKER["it"],
            "hero_alt": "Caffè servito con loukoumi",
            "hero_caption": "Caffè con loukoumi — il dolce per cui Syros è famosa.",
            "mid_alt": "Cucina della villa pronta per cucinare a Syros",
            "mid_caption": "Una cucina attrezzata trasforma mercato e San Michali in cena in terrazza.",
            "body": """<p>Con villa e cucina, il cibo diventa parte del viaggio. Syros eccelle: tradizione marina e cultura commerciale di Ermoupoli — formaggi, salumi e dolci con identità.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Lista della spesa</h2>
<ul>
  <li><strong>San Michali DOP:</strong> formaggio stagionato di vacca, piccante e nocciolato — simbolo dell’isola.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Loukoumi:</strong> rosa, mastice, bergamotto e altri gusti, tradizione di generazioni.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup></li>
  <li><strong>Halvadopita:</strong> dolce tipo nougat, ottimo da portare a casa.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>Louza e salsicce:</strong> salumi che rendono locale una cena semplice in villa.<sup><a href="#ref2">[2]</a></sup></li>
</ul>
<h2>Sere in cucina vs taverna</h2>
<p>Ritmo ideale: due cene in casa, una taverna di pesce sull’acqua e una passeggiata gastronomica a Ermoupoli.<sup><a href="#ref3">[3]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="Cucina della villa pronta per cucinare a Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Una cucina attrezzata trasforma mercato e San Michali in cena in terrazza.</figcaption>
</figure>
<h2>Perché la gastronomia spinge verso una casa</h2>
<p>Chi cerca «villa con cucina Syros» o «self catering Cicladi» vuole flessibilità — i prodotti di Syros rafforzano la scelta di una casa rispetto a una sola camera.<sup><a href="#ref1">[1]</a></sup></p>
<div class="svs-callout">
  <strong>Cucinate con vista mare</strong>
  La cucina completa di Sea View Serenity è fatta per questo: spesa al mattino, spiaggia a metà giornata, lunga cena in terrazza la sera.
  <a class="svs-cta" href="BOOK">Prenota la casa</a>
</div>""",
        },
        "he": {
            "title": "מדריך אוכל בסירוס לאורחי וילה: שווקים, לוקומי וטברנות על הים | Sea View Serenity",
            "description": "מה לאכול בסירוס — גבינת San Michali, לוקומי ופירות ים — כשיש מטבח ורוצים טעם מקומי.",
            "keywords": "אוכל סירוס, לוקומי סירוס, גבינת San Michali, איפה לאכול סירוס, גסטרונומיה סירוס, קניות לווילה",
            "kicker": KICKER["he"],
            "hero_alt": "קפה עם לוקומי",
            "hero_caption": "קפה עם לוקומי — הממתק שסירוס מפורסמת בו.",
            "mid_alt": "מטבח וילה מוכן לבישול בסירוס",
            "mid_caption": "מטבח מעשי הופך קניות ו-San Michali לארוחת ערב במרפסת.",
            "body": """<p>כשיש וילה עם מטבח, האוכל חלק מתכנון החופשה. סירוס בולטת: מסורת ימית ותרבות מסחרית של ארמופולי — גבינות, נקניקים ומתוקים עם זהות.<sup><a href="#ref1">[1]</a></sup></p>
<h2>על רשימת הקניות</h2>
<ul>
  <li><strong>San Michali PDO:</strong> גבינת פרה קשה, חריפה ואגוזית — סמל האי.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>לוקומי:</strong> ורד, מסטיקה, ברגמוט ועוד, מסורת של דורות.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup></li>
  <li><strong>חלבדופיטה:</strong> מתוק בסגנון נוגט, מצוין כמתנה.<sup><a href="#ref1">[1]</a></sup></li>
  <li><strong>לוזה ונקניקים:</strong> מעדנים שהופכים ארוחת ערב פשוטה בווילה למקומית.<sup><a href="#ref2">[2]</a></sup></li>
</ul>
<h2>ערבי מטבח מול טברנה</h2>
<p>קצב טוב: שתי ארוחות בבית, טברנת דגים על המים וטיול אוכל בארמופולי.<sup><a href="#ref3">[3]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="מטבח וילה מוכן לבישול בסירוס" loading="lazy" width="1200" height="675" />
  <figcaption>מטבח מעשי הופך קניות ו-San Michali לארוחת ערב במרפסת.</figcaption>
</figure>
<h2>למה הגסטרונומיה מחזקת בחירה בבית</h2>
<p>מי שמחפש «וילה עם מטבח סירוס» או «ארוחה עצמית קיקלדים» רוצה גמישות — זהות המוצרים של סירוס מחזקת בחירה בבית על פני חדר בלבד.<sup><a href="#ref1">[1]</a></sup></p>
<div class="svs-callout">
  <strong>בשלו עם נוף לים</strong>
  המטבח המלא של Sea View Serenity בנוי לזה: שוק בבוקר, חוף בצהריים, ארוחת ערב ארוכה במרפסת בערב.
  <a class="svs-cta" href="BOOK">הזמינו את הבית</a>
</div>""",
        },
    }

def rental_checklist():
    return {
        "el": {
            "title": "Checklist ενοικίασης διακοπών στην Ελλάδα: τι να επιβεβαιώσετε πριν κλείσετε | Sea View Serenity",
            "description": "Πρακτική checklist για παραθαλάσσιες μισθώσεις στην Ελλάδα — τοποθεσία, χωρητικότητα, κουζίνα, parking και πραγματικότητες κράτησης στην κορυφή της σεζόν.",
            "keywords": "checklist ενοικίαση διακοπών Ελλάδα, Airbnb Ελλάδα συμβουλές, κράτηση βίλα Ελλάδα, amenities παραλία, συμβουλές Κυκλάδες",
            "kicker": KICKER["el"],
            "hero_alt": "Σαλόνι με τζάκι σε βίλα στη Σύρο",
            "hero_caption": "Κοιτάξτε πέρα από τις φωτογραφίες: πραγματικός χώρος, διάταξη και άνεση το βράδυ.",
            "mid_alt": "Κουζίνα σε ενοικίαση διακοπών στην Ελλάδα",
            "mid_caption": "Κουζίνα, πλυντήριο, parking και Wi‑Fi καθορίζουν αν η εβδομάδα στην ακτή είναι εύκολη.",
            "body": """<p>Πριν επιβεβαιώσετε οποιαδήποτε <strong>ενοικίαση διακοπών στην Ελλάδα</strong>, τρέξτε checklist. Οι βραχυχρόνιες μισθώσεις είναι πλέον κύριο μέρος της προσφοράς, ειδικά σε νησιωτικούς μήνες αιχμής.<sup><a href="#ref1">[1]</a></sup></p>
<h2>1) Τοποθεσία στον χάρτη, όχι μόνο στο κείμενο</h2>
<ul>
  <li>Σταθεροποιήστε το ακίνητο και μετρήστε περπάτημα μέχρι την παραλία που σας ενδιαφέρει.</li>
  <li>Προτιμήστε ακριβή τοπωνύμια («κοντά στη Δελφίνι, Σύρος») αντί για γενικό «θέα Κυκλάδες».</li>
  <li>Ελέγξτε αν η «διάσημη» παραλία είναι αυτή που θα χρησιμοποιείτε καθημερινά.</li>
</ul>
<h2>2) Χωρητικότητα και διαμόρφωση ύπνου</h2>
<p>Ο αριθμός επισκεπτών μπορεί να κρύβει καναπέ-κρεβάτια. Για οικογένειες και παρέες, επιβεβαιώστε πραγματικά υπνοδωμάτια και μπάνια.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="Κουζίνα σε ενοικίαση διακοπών στην Ελλάδα" loading="lazy" width="1200" height="675" />
  <figcaption>Κουζίνα, πλυντήριο, parking και Wi‑Fi καθορίζουν αν η εβδομάδα στην ακτή είναι εύκολη.</figcaption>
</figure>
<h2>3) Κουζίνα, πλυντήριο, parking, Wi‑Fi</h2>
<p>Αυτά τα τέσσερα amenities αποφασίζουν αν η εβδομάδα στην ακτή νιώθει εύκολη — και είναι τα φίλτρα που χρησιμοποιούν οι συχνοί ταξιδιώτες.</p>
<h2>4) Σεζόν και χρόνος κράτησης</h2>
<p>Το τουριστικό εισερχόμενο παραμένει ισχυρό, με το Νότιο Αιγαίο κορυφαίο σε διανυκτερεύσεις.<sup><a href="#ref3">[3]</a></sup> Το καλοκαίρι 2026 δείχνει νωρίτερες κρατήσεις και έντονη συγκέντρωση στην αιχμή.<sup><a href="#ref4">[4]</a></sup> Μην αντιμετωπίζετε τον Αύγουστο ως last minute για καλά σπίτια στην ακτή.</p>
<h2>5) Σαφήνεια σε άμεση κράτηση</h2>
<ol>
  <li>Τι περιλαμβάνεται (σεντόνια, καθαριότητα, πληροφορίες άφιξης);</li>
  <li>Ποια είναι η πολιτική ακύρωσης;</li>
  <li>Ποιον επικοινωνείτε την ημέρα άφιξης;</li>
  <li>Συμφωνεί η ταυτότητα της αγγελίας σε φωτογραφίες, χάρτη και λίστα amenities;</li>
</ol>
<div class="svs-callout">
  <strong>Εφαρμόστε την checklist στο Sea View Serenity</strong>
  Δυτική Σύρος κοντά στη Δελφίνι, χώρος για οικογένειες/ομάδες, πλήρης κουζίνα, parking, πλυντήριο και άμεση κράτηση από τον ιστότοπό μας.
  <a class="svs-cta" href="BOOK">Κλείστε τώρα</a>
</div>""",
        },
        "fr": {
            "title": "Checklist location vacances en Grèce : quoi vérifier avant de réserver | Sea View Serenity",
            "description": "Checklist pratique pour locations au bord de mer en Grèce — lieu, capacité, cuisine, parking et réalités de réservation en haute saison.",
            "keywords": "checklist location Grèce, conseils Airbnb Grèce, réserver villa Grèce, équipements bord de mer, conseils Cyclades",
            "kicker": KICKER["fr"],
            "hero_alt": "Salon avec cheminée dans une villa à Syros",
            "hero_caption": "Au-delà des photos hero : espace réel, agencement et confort le soir.",
            "mid_alt": "Cuisine dans une location vacances en Grèce",
            "mid_caption": "Cuisine, lave-linge, parking et Wi‑Fi font la différence pour une semaine facile au bord de la mer.",
            "body": """<p>Avant de confirmer une <strong>location vacances en Grèce</strong>, utilisez une checklist. Les locations courte durée font désormais partie normale de l’offre, surtout aux mois de pointe insulaires.<sup><a href="#ref1">[1]</a></sup></p>
<h2>1) Carte vs promesses</h2>
<ul>
  <li>Épinglez le bien et chronométrez la marche jusqu’à la plage visée.</li>
  <li>Privilégiez des lieux précis (« près de Delfini, Syros ») aux « vue mer Cyclades » vagues.</li>
  <li>Vérifiez que la plage fameuse est celle que vous utiliserez chaque jour.</li>
</ul>
<h2>2) Capacité et couchages</h2>
<p>Le nombre d’hôtes peut cacher des canapés-lits. Familles et groupes : vérifiez chambres et salles de bain réelles.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="Cuisine dans une location vacances en Grèce" loading="lazy" width="1200" height="675" />
  <figcaption>Cuisine, lave-linge, parking et Wi‑Fi font la différence pour une semaine facile au bord de la mer.</figcaption>
</figure>
<h2>3) Cuisine, lave-linge, parking, Wi‑Fi</h2>
<p>Ces quatre équipements décident si la semaine au bord de la mer reste simple — ce sont aussi les filtres des voyageurs habitués.</p>
<h2>4) Saison et délai de réservation</h2>
<p>Le tourisme entrant reste massif, la mer Égée méridionale leader en nuitées.<sup><a href="#ref3">[3]</a></sup> L’été 2026 montre des réservations plus précoces et une forte concentration en pic.<sup><a href="#ref4">[4]</a></sup> N’attendez pas août pour une bonne maison en bord de mer.</p>
<h2>5) Clarté en réservation directe</h2>
<ol>
  <li>Qu’est-ce qui est inclus (linge, ménage, infos d’arrivée) ?</li>
  <li>Quelle politique d’annulation ?</li>
  <li>Qui contacter le jour d’arrivée ?</li>
  <li>Cohérence entre photos, carte et liste d’équipements ?</li>
</ol>
<div class="svs-callout">
  <strong>Appliquez la checklist à Sea View Serenity</strong>
  Côte ouest de Syros près de Delfini, espace familles/groupes, cuisine complète, parking, buanderie et réservation directe sur notre site.
  <a class="svs-cta" href="BOOK">Réserver maintenant</a>
</div>""",
        },
        "de": {
            "title": "Checkliste Ferienunterkunft Griechenland: Vor der Buchung prüfen | Sea View Serenity",
            "description": "Praktische Checkliste für Unterkünfte am Meer in Griechenland — Lage, Kapazität, Küche, Parkplatz und Buchungsrealität in der Hochsaison.",
            "keywords": "Ferienunterkunft Griechenland Checkliste, Airbnb Griechenland Tipps, Villa buchen Griechenland, Ausstattung Meer, Kykladen Unterkunft",
            "kicker": KICKER["de"],
            "hero_alt": "Wohnzimmer mit Kamin in einer Villa auf Syros",
            "hero_caption": "Hinter Hero-Fotos: echter Raum, Grundriss und Abendkomfort prüfen.",
            "mid_alt": "Küche in einer Ferienunterkunft in Griechenland",
            "mid_caption": "Küche, Waschmaschine, Parkplatz und WLAN entscheiden, ob die Woche am Meer leicht wirkt.",
            "body": """<p>Vor jeder <strong>Ferienunterkunft in Griechenland</strong> eine Checkliste durchgehen. Kurzzeitmieten sind Standard im Angebot, besonders in Spitzenmonaten auf den Inseln.<sup><a href="#ref1">[1]</a></sup></p>
<h2>1) Lage auf der Karte, nicht nur im Text</h2>
<ul>
  <li>Objekt markieren und Gehzeit zum Wunschstrand messen.</li>
  <li>Präzise Ortsnamen („nahe Delfini, Syros“) statt vages „Kykladen-Meerblick“.</li>
  <li>Ist der bekannte Strand der, den Sie täglich nutzen?</li>
</ul>
<h2>2) Kapazität und Schlafplätze</h2>
<p>Gästezahlen können Schlafsofas verschleiern. Familien und Gruppen: echte Schlafzimmer und Bäder bestätigen.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="Küche in einer Ferienunterkunft in Griechenland" loading="lazy" width="1200" height="675" />
  <figcaption>Küche, Waschmaschine, Parkplatz und WLAN entscheiden, ob die Woche am Meer leicht wirkt.</figcaption>
</figure>
<h2>3) Küche, Wäsche, Parkplatz, WLAN</h2>
<p>Diese vier Punkte machen den Unterschied — und sind Standardfilter für erfahrene Reisende.</p>
<h2>4) Saison und Vorlauf</h2>
<p>Der eingehende Tourismus bleibt stark, Südägäis führend bei Übernachtungen.<sup><a href="#ref3">[3]</a></sup> Sommer 2026: frühere Buchungen, scharfe Spitzenkonzentration.<sup><a href="#ref4">[4]</a></sup> August ist kein Last-Minute-Markt für gute Häuser am Meer.</p>
<h2>5) Klarheit bei Direktbuchung</h2>
<ol>
  <li>Was ist inklusive (Bettwäsche, Reinigung, Ankunftsinfos)?</li>
  <li>Welche Stornoregel?</li>
  <li>Wen erreicht man am Ankunftstag?</li>
  <li>Stimmen Fotos, Karte und Ausstattungsliste überein?</li>
</ol>
<div class="svs-callout">
  <strong>Checkliste auf Sea View Serenity anwenden</strong>
  Syros-Westküste nahe Delfini, Platz für Familien/Gruppen, volle Küche, Parkplatz, Wäsche und Direktbuchung über unsere Website.
  <a class="svs-cta" href="BOOK">Jetzt buchen</a>
</div>""",
        },
        "it": {
            "title": "Checklist affitto vacanze Grecia: cosa verificare prima di prenotare | Sea View Serenity",
            "description": "Checklist pratica per case sul mare in Grecia — posizione, capienza, cucina, parcheggio e realtà di prenotazione in alta stagione.",
            "keywords": "checklist affitto vacanze Grecia, consigli Airbnb Grecia, prenotare villa Grecia, servizi mare, consigli Cicladi",
            "kicker": KICKER["it"],
            "hero_alt": "Soggiorno con caminetto in villa a Syros",
            "hero_caption": "Oltre le foto principali: spazio reale, layout e comfort serale.",
            "mid_alt": "Cucina in un affitto vacanze in Grecia",
            "mid_caption": "Cucina, lavatrice, parcheggio e Wi‑Fi decidono se la settimana al mare è facile.",
            "body": """<p>Prima di confermare un <strong>affitto vacanze in Grecia</strong>, usate una checklist. Le locazioni brevi sono ormai parte standard dell’offerta, soprattutto nei mesi di punta sulle isole.<sup><a href="#ref1">[1]</a></sup></p>
<h2>1) Mappa vs testo dell’annuncio</h2>
<ul>
  <li>Fissate l’immobile e cronometrate la passeggiata fino alla spiaggia che conta.</li>
  <li>Nomi precisi («vicino a Delfini, Syros») invece di vago «vista mare Cicladi».</li>
  <li>La spiaggia famosa è quella che userete ogni giorno?</li>
</ul>
<h2>2) Capienza e disposizione notti</h2>
<p>I posti letto possono nascondere divani. Famiglie e gruppi: verificate camere e bagni reali.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="Cucina in un affitto vacanze in Grecia" loading="lazy" width="1200" height="675" />
  <figcaption>Cucina, lavatrice, parcheggio e Wi‑Fi decidono se la settimana al mare è facile.</figcaption>
</figure>
<h2>3) Cucina, lavatrice, parcheggio, Wi‑Fi</h2>
<p>Questi quattro servizi fanno la differenza — sono anche i filtri dei viaggiatori abituali.</p>
<h2>4) Stagione e anticipo</h2>
<p>Il turismo in entrata resta forte, Egeo meridionale leader in pernotti.<sup><a href="#ref3">[3]</a></sup> Estate 2026: prenotazioni più early e picco concentrato.<sup><a href="#ref4">[4]</a></sup> Non trattate agosto come last minute per belle case al mare.</p>
<h2>5) Chiarezza in prenotazione diretta</h2>
<ol>
  <li>Cosa è incluso (biancheria, pulizie, info arrivo)?</li>
  <li>Politica di cancellazione?</li>
  <li>Chi contattare il giorno dell’arrivo?</li>
  <li>Coerenza tra foto, mappa e elenco servizi?</li>
</ol>
<div class="svs-callout">
  <strong>Usate la checklist su Sea View Serenity</strong>
  Costa occidentale di Syros vicino a Delfini, spazio famiglie/gruppi, cucina completa, parcheggio, lavanderia e prenotazione diretta sul sito.
  <a class="svs-cta" href="BOOK">Prenota ora</a>
</div>""",
        },
        "he": {
            "title": "רשימת בדיקה לשכירות חופשה ביוון: מה לאמת לפני ההזמנה | Sea View Serenity",
            "description": "רשימת בדיקה מעשית לדירות על הים ביוון — מיקום, קיבולת, מטבח, חניה ומציאות הזמנה בעונת השיא.",
            "keywords": "רשימת בדיקה שכירות חופשה יוון, טיפים Airbnb יוון, הזמנת וילה יוון, מתקנים על הים, טיפים קיקלדים",
            "kicker": KICKER["he"],
            "hero_alt": "סלון עם אח בווילה בסירוס",
            "hero_caption": "מעבר לתמונות הראשיות: חלל אמיתי, תכנון ונוחות בערב.",
            "mid_alt": "מטבח בשכירות חופשה ביוון",
            "mid_caption": "מטבח, כביסה, חניה ו-Wi‑Fi קובעים אם השבוע על הים מרגיש קל.",
            "body": """<p>לפני אישור <strong>שכירות חופשה ביוון</strong>, עברו רשימת בדיקה. שכירויות לטווח קצר הן כבר חלק מרכזי מההיצע, במיוחד בחודשי שיא באיים.<sup><a href="#ref1">[1]</a></sup></p>
<h2>1) מיקום במפה מול טקסט</h2>
<ul>
  <li>נעצו את הנכס ומדדו הליכה לחוף שחשוב לכם.</li>
  <li>שמות מדויקים («ליד דלפיני, סירוס») ולא «נוף לים קיקלדים» מעורפל.</li>
  <li>האם החוף המפורסם הוא זה שתשתמשו בו מדי יום?</li>
</ul>
<h2>2) קיבולת ופריסת שינה</h2>
<p>מספר אורחים עלול להסתיר ספות. למשפחות וקבוצות — אמתו חדרי שינה ואמבטיות אמיתיים.<sup><a href="#ref2">[2]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/villa-kitchen.jpg" alt="מטבח בשכירות חופשה ביוון" loading="lazy" width="1200" height="675" />
  <figcaption>מטבח, כביסה, חניה ו-Wi‑Fi קובעים אם השבוע על הים מרגיש קל.</figcaption>
</figure>
<h2>3) מטבח, כביסה, חניה, Wi‑Fi</h2>
<p>ארבעת המתקנים האלה קובעים אם השבוע על הים קל — וגם המסננים של מטיילים מנוסים.</p>
<h2>4) עונה וזמן הזמנה מראש</h2>
<p>התיירות הנכנסת נשארת חזקה, הים האגאי הדרומי מוביל בלינות.<sup><a href="#ref3">[3]</a></sup> קיץ 2026 מציג הזמנות מוקדמות יותר וריכוז חד בשיא.<sup><a href="#ref4">[4]</a></sup> אל תתייחסו לאוגוסט כשוק last minute לבתים טובים על הים.</p>
<h2>5) בהירות בהזמנה ישירה</h2>
<ol>
  <li>מה כלול (מצעים, ניקיון, מידע הגעה)?</li>
  <li>מדיניות ביטול?</li>
  <li>את מי מתקשרים ביום ההגעה?</li>
  <li>עקביות בין תמונות, מפה ורשימת מתקנים?</li>
</ol>
<div class="svs-callout">
  <strong>הפעילו את הרשימה על Sea View Serenity</strong>
  חוף מערבי סירוס ליד דלפיני, מקום למשפחות/קבוצות, מטבח מלא, חניה, כביסה והזמנה ישירה באתר שלנו.
  <a class="svs-cta" href="BOOK">הזמינו עכשיו</a>
</div>""",
        },
    }

def beaches_guide():
    return {
        "el": {
            "title": "Κίνι, Δελφίνι και Γαλησσάς: πρακτικός οδηγός παραλιών στη Σύρο | Sea View Serenity",
            "description": "Συγκρίνετε Κίνι, Δελφίνι και Γαλησσά για κολύμπι, οικογένειες και ηλιοβασιλέματα — ώστε να διαλέξετε τη σωστή βάση παραλίας.",
            "keywords": "παραλίες Σύρος, παραλία Κίνι, παραλία Δελφίνι Σύρος, παραλία Γαλησσάς, καλύτερες παραλίες Σύρος, δυτική ακτή Σύρου",
            "kicker": KICKER["el"],
            "hero_alt": "Παραλία Δελφίνι στη Σύρο",
            "hero_caption": "Δελφίνι — ήσυχος κόλπος στη δυτική ακτή.",
            "mid_alt": "Παραλία Γαλησσάς στη Σύρο",
            "mid_caption": "Γαλησσάς — μεγάλος αμμώδης κόλπος δημοφιλής σε οικογένειες.",
            "body": """<p>Οι αναζητήσεις για <strong>παραλία Κίνι</strong>, <strong>Δελφίνι Σύρος</strong>, <strong>Γαλησσάς</strong> και «καλύτερες παραλίες Σύρου» οδηγούν τις κρατήσεις — ξεκινήστε από επίσημες πηγές.</p>
<h2>Γαλησσάς: η εύκολη all-rounder</h2>
<p>Μεγάλος κόλπος με λεπτή άμμο και εύκολη πρόσβαση, με το εκκλησάκι της Αγίας Πακού στο άκρο — πλήρης μέρα στην παραλία, συμπεριλαμβανομένης προσβασιμότητας.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-galissas-beach.jpg" alt="Παραλία Γαλησσάς στη Σύρο" loading="lazy" width="1200" height="675" />
  <figcaption>Γαλησσάς — μεγάλος αμμώδης κόλπος δημοφιλής σε οικογένειες.</figcaption>
</figure>
<h2>Κίνι: ηλιοβασίλεμα και ταβέρνες</h2>
<p>Ρηχός αμμώδης κόλπος με ταβέρνες στο νερό και ισχυρή φήμη ηλιοβασιλέματος — με δυνατότητες προσβασιμότητας για μεικτές ομάδες ηλικιών.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Δελφίνι: ήσυχο και κοντά σε «μείνε τοπικά»</h2>
<p>Μικρότεροι δυτικοί κόλποι κοντά στο Κίνι, με σύντομο δρόμο ή βάρκα — γι’ αυτό όσοι θέλουν ήσυχη διαμονή προτιμούν σπίτι εδώ: λιγότερες μετακινήσεις, περισσότερα κολύμβια.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Πώς να διαλέξετε βάση παραλίας</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.95rem">
  <thead>
    <tr>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">Αν θέλετε…</th>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">Ξεκινήστε από</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Μεγαλύτερο εύκολο αμμώδη κόλπο</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Γαλησσάς</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Ηλιοβασίλεμα + ταβέρνες στην άμμο</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Κίνι</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Ήσυχος κόλπος κοντά σε ενοικίαση</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Δελφίνι</td></tr>
    <tr><td style="padding:0.45rem 0.4rem">Άμμος στο νότο, προστατευμένη από μελτέμι</td><td style="padding:0.45rem 0.4rem">Αγαθόπες / νότια ακτή<sup><a href="#ref1">[1]</a></sup></td></tr>
  </tbody>
</table>
<div class="svs-callout">
  <strong>Κοιμηθείτε κοντά στον κόλπο που θα ξαναπιείτε</strong>
  Το Sea View Serenity απέχει λίγα βήματα από τη Δελφίνι, με το Κίνι κοντά για δείπνα στο ηλιοβασίλεμα και τη Γαλησσά προσβάσιμη για μεγαλύτερη μέρα παραλίας.
  <a class="svs-cta" href="BOOK">Κλείστε διαμονή στη Δελφίνι</a>
</div>
<p>Οι παραλίες δουλεύουν καλύτερα μαζί με την Ερμούπολη παρά αντίθετα.<sup><a href="#ref2">[2]</a></sup> Το καλό ταξίδι είναι συνήθως κόλπος + πόλη + μία νότια μέρα παραλίας.</p>""",
        },
        "fr": {
            "title": "Kini, Delfini et Galissas : guide pratique des plages de Syros | Sea View Serenity",
            "description": "Comparez Kini, Delfini et Galissas pour la baignade, les familles et les couchers de soleil — et choisissez la bonne base plage.",
            "keywords": "plages Syros, plage Kini, plage Delfini Syros, plage Galissas, meilleures plages Syros, côte ouest Syros",
            "kicker": KICKER["fr"],
            "hero_alt": "Plage de Delfini à Syros, Grèce",
            "hero_caption": "Delfini — crique plus calme sur la côte ouest.",
            "mid_alt": "Plage de Galissas à Syros, Grèce",
            "mid_caption": "Galissas — grande baie de sable prisée des familles.",
            "body": """<p>Les recherches <strong>Kini beach</strong>, <strong>Delfini Syros</strong>, <strong>Galissas</strong> et « meilleures plages Syros » structurent les réservations — partez des guides officiels.</p>
<h2>Galissas : l’option facile</h2>
<p>Grande baie de sable fin et accès simple, avec la chapelle d’Agia Pakou au bout — journée plage complète, accessibilité comprise.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-galissas-beach.jpg" alt="Plage de Galissas à Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Galissas — grande baie de sable prisée des familles.</figcaption>
</figure>
<h2>Kini : soleil couchant et tavernes</h2>
<p>Crique sablonneuse peu profonde, tavernes au bord de l’eau et réputation de coucher de soleil — avec équipements d’accessibilité pour groupes mixtes.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Delfini : plus calme, rythme local</h2>
<p>Petites criques ouest près de Kini, en voiture court ou en bateau — d’où l’attrait pour une maison ici : moins de transferts, plus de baignades.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Choisir votre base plage</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.95rem">
  <thead>
    <tr>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">Si vous voulez…</th>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">Commencez par</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">La plus grande baie sablonneuse facile</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Galissas</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Coucher de soleil + tavernes sur le sable</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Kini</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Crique calme près d’une location</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Delfini</td></tr>
    <tr><td style="padding:0.45rem 0.4rem">Sable au sud abrité du meltemi</td><td style="padding:0.45rem 0.4rem">Agathopes / sud<sup><a href="#ref1">[1]</a></sup></td></tr>
  </tbody>
</table>
<div class="svs-callout">
  <strong>Dormez près de la crique que vous réutiliserez</strong>
  Sea View Serenity est à quelques minutes de Delfini, Kini proche pour les dîners au coucher du soleil, Galissas accessible pour une grande journée plage.
  <a class="svs-cta" href="BOOK">Réserver près de Delfini</a>
</div>
<p>Les plages fonctionnent mieux avec Ermoupoli qu’à sa place.<sup><a href="#ref2">[2]</a></sup> Le bon voyage mélange crique, ville et une journée plage au sud.</p>""",
        },
        "de": {
            "title": "Kini, Delfini und Galissas: praktischer Syros-Strandführer | Sea View Serenity",
            "description": "Vergleichen Sie Kini, Delfini und Galissas für Schwimmen, Familien und Sonnenuntergänge — und wählen Sie die richtige Strandbasis.",
            "keywords": "Strände Syros, Strand Kini, Strand Delfini Syros, Strand Galissas, beste Strände Syros, Westküste Syros",
            "kicker": KICKER["de"],
            "hero_alt": "Strand Delfini auf Syros, Griechenland",
            "hero_caption": "Delfini — ruhigere Bucht an der Westküste.",
            "mid_alt": "Strand Galissas auf Syros, Griechenland",
            "mid_caption": "Galissas — große Sandbucht, beliebt bei Familien.",
            "body": """<p>Suchbegriffe wie <strong>Kini Strand</strong>, <strong>Delfini Syros</strong>, <strong>Galissas</strong> und „beste Strände Syros“ prägen Buchungen — starten Sie mit offiziellen Quellen.</p>
<h2>Galissas: der unkomplizierte Allrounder</h2>
<p>Große Bucht mit feinem Sand und leichtem Zugang, Kapelle Agia Pakou am Ende — voller Strandtag inklusive Barrierefreiheit.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-galissas-beach.jpg" alt="Strand Galissas auf Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Galissas — große Sandbucht, beliebt bei Familien.</figcaption>
</figure>
<h2>Kini: Sonnenuntergang und Tavernen</h2>
<p>Flache Sandbucht, Tavernen am Wasser und starke Sunset-Reputation — mit Zugang für gemischte Altersgruppen.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Delfini: ruhiger, nah am „lokal bleiben“-Rhythmus</h2>
<p>Kleinere Westbuchten nahe Kini, kurz per Straße oder Boot — deshalb bevorzugen Ruhesuchende ein Haus hier: weniger Transfer, mehr Schwimmen.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Strandbasis wählen</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.95rem">
  <thead>
    <tr>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">Wenn Sie wollen…</th>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">Starten Sie mit</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Größte leichte Sandbucht</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Galissas</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Sonnenuntergang + Tavernen im Sand</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Kini</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Ruhige Bucht nahe Ferienhaus</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Delfini</td></tr>
    <tr><td style="padding:0.45rem 0.4rem">Südlicher Sand, meltemigeschützt</td><td style="padding:0.45rem 0.4rem">Agathopes / Südküste<sup><a href="#ref1">[1]</a></sup></td></tr>
  </tbody>
</table>
<div class="svs-callout">
  <strong>Schlafen Sie nah an der Bucht, die Sie wieder nutzen</strong>
  Sea View Serenity liegt kurz zu Fuß von Delfini, Kini für Sonnenuntergangsessen, Galissas für einen großen Strandtag.
  <a class="svs-cta" href="BOOK">Aufenthalt nahe Delfini buchen</a>
</div>
<p>Strände ergänzen Ermoupoli am besten.<sup><a href="#ref2">[2]</a></sup> Die starke Reise mischt Bucht, Stadt und einen südlichen Strandtag.</p>""",
        },
        "it": {
            "title": "Kini, Delfini e Galissas: guida pratica alle spiagge di Syros | Sea View Serenity",
            "description": "Confrontate Kini, Delfini e Galissas per nuotate, famiglie e tramonti — e scegliete la base spiaggia giusta.",
            "keywords": "spiagge Syros, spiaggia Kini, spiaggia Delfini Syros, spiaggia Galissas, migliori spiagge Syros, costa occidentale Syros",
            "kicker": KICKER["it"],
            "hero_alt": "Spiaggia di Delfini a Syros, Grecia",
            "hero_caption": "Delfini — cala più tranquilla sulla costa occidentale.",
            "mid_alt": "Spiaggia di Galissas a Syros, Grecia",
            "mid_caption": "Galissas — ampia baia sabbiosa molto scelta dalle famiglie.",
            "body": """<p>Le ricerche su <strong>spiaggia Kini</strong>, <strong>Delfini Syros</strong>, <strong>Galissas</strong> e «migliori spiagge Syros» guidano le prenotazioni — partite da fonti ufficiali.</p>
<h2>Galissas: la scelta facile</h2>
<p>Grande baia di sabbia fine e accesso semplice, cappella di Agia Pakou in fondo — giornata spiaggia completa, accessibilità inclusa.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-galissas-beach.jpg" alt="Spiaggia di Galissas a Syros" loading="lazy" width="1200" height="675" />
  <figcaption>Galissas — ampia baia sabbiosa molto scelta dalle famiglie.</figcaption>
</figure>
<h2>Kini: tramonto e taverne</h2>
<p>Cala sabbiosa bassa, taverne sull’acqua e ottima fama al tramonto — con servizi di accessibilità per gruppi misti.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Delfini: più silenziosa, ritmo locale</h2>
<p>Piccole calate occidentali vicino a Kini, breve strada o barca — per questo chi cerca quiete preferisce una casa qui: meno trasferimenti, più tuffi.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Scegliere la base spiaggia</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.95rem">
  <thead>
    <tr>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">Se volete…</th>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">Partite da</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">La più grande baia sabbiosa facile</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Galissas</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Tramonto + taverne sulla sabbia</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Kini</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Cala tranquilla vicino all’affitto</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">Delfini</td></tr>
    <tr><td style="padding:0.45rem 0.4rem">Sabbia a sud riparata dal meltemi</td><td style="padding:0.45rem 0.4rem">Agathopes / costa sud<sup><a href="#ref1">[1]</a></sup></td></tr>
  </tbody>
</table>
<div class="svs-callout">
  <strong>Dormite vicino alla cala che riuserete</strong>
  Sea View Serenity è a breve passeggiata da Delfini, Kini vicina per cene al tramonto, Galissas raggiungibile per una grande giornata spiaggia.
  <a class="svs-cta" href="BOOK">Prenota vicino a Delfini</a>
</div>
<p>Le spiagge funzionano meglio insieme a Ermoupoli.<sup><a href="#ref2">[2]</a></sup> Il viaggio vincente mescola cala, città e una giornata al sud.</p>""",
        },
        "he": {
            "title": "קיני, דלפיני וגליסאס: מדריך מעשי לחופי סירוס | Sea View Serenity",
            "description": "השוו בין קיני, דלפיני וגליסאס לשחייה, משפחות ושקיעות — ובחרו בסיס חוף נכון לשהייה.",
            "keywords": "חופי סירוס, חוף קיני, חוף דלפיני סירוס, חוף גליסאס, החופים הטובים בסירוס, חוף מערבי סירוס",
            "kicker": KICKER["he"],
            "hero_alt": "חוף דלפיני בסירוס, יוון",
            "hero_caption": "דלפיני — מפרץ שקט יותר בחוף המערבי.",
            "mid_alt": "חוף גליסאס בסירוס, יוון",
            "mid_caption": "גליסאס — מפרץ חולי גדול שאהוב על משפחות.",
            "body": """<p>חיפושים כמו <strong>חוף קיני</strong>, <strong>דלפיני סירוס</strong>, <strong>גליסאס</strong> ו«החופים הטובים בסירוס» מניעים הזמנות — התחילו ממקורות רשמיים.</p>
<h2>גליסאס: האופציה הקלה</h2>
<p>מפרץ גדול עם חול עדין וגישה נוחה, כנסיית אגיה פקו בקצה — יום חוף מלא, כולל נגישות.<sup><a href="#ref1">[1]</a></sup></p>
<figure class="svs-figure">
  <img src="../media/syros-galissas-beach.jpg" alt="חוף גליסאס בסירוס" loading="lazy" width="1200" height="675" />
  <figcaption>גליסאס — מפרץ חולי גדול שאהוב על משפחות.</figcaption>
</figure>
<h2>קיני: שקיעה וטברנות</h2>
<p>מפרץ חולי רדוד, טברנות על המים ומוניטין שקיעה חזק — עם מתקני נגישות לקבוצות מעורבות.<sup><a href="#ref1">[1]</a></sup></p>
<h2>דלפיני: שקט וקרוב לקצב מקומי</h2>
<p>מפרצונים קטנים במערב ליד קיני, בדרך קצרה או בסירה — לכן מחפשי שקט בוחרים בית כאן: פחות נסיעות, יותר שחייה.<sup><a href="#ref1">[1]</a></sup></p>
<h2>איך לבחור בסיס חוף</h2>
<table style="width:100%;border-collapse:collapse;font-size:0.95rem">
  <thead>
    <tr>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">אם אתם רוצים…</th>
      <th style="text-align:left;border-bottom:1px solid #d9e2ec;padding:0.4rem">התחילו ב</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">מפרץ חולי גדול ונוח</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">גליסאס</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">שקיעה + טברנות על החול</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">קיני</td></tr>
    <tr><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">מפרץ שקט ליד שכירות</td><td style="padding:0.45rem 0.4rem;border-bottom:1px solid #eee">דלפיני</td></tr>
    <tr><td style="padding:0.45rem 0.4rem">חול בדרום מוגן ממלטמי</td><td style="padding:0.45rem 0.4rem">אגתופס / דרום<sup><a href="#ref1">[1]</a></sup></td></tr>
  </tbody>
</table>
<div class="svs-callout">
  <strong>לנו קרוב למפרץ שתחזרו אליו</strong>
  Sea View Serenity במרחק הליכה מדלפיני, קיני קרובה לארוחות שקיעה וגליסאס נגישה ליום חוף גדול.
  <a class="svs-cta" href="BOOK">הזמינו לינה ליד דלפיני</a>
</div>
<p>החופים עובדים טוב יחד עם ארמופולי.<sup><a href="#ref2">[2]</a></sup> הטיול המוצלח מערבב מפרץ, עיר ויום חוף אחד בדרום.</p>""",
        },
    }

DATA = {
    "how-to-get-to-syros-from-athens-ferry-flight": how_to_get_to(),
    "family-vacation-syros-seaside-house": family_vacation(),
    "ermoupoli-and-beach-day-syros-itinerary": ermoupoli_itinerary(),
    "syros-food-guide-for-villa-guests": syros_food(),
    "greece-vacation-rental-checklist-before-you-book": rental_checklist(),
    "kini-delfini-galissas-syros-beaches-guide": beaches_guide(),
}

if __name__ == "__main__":
    json.dump(DATA, sys.stdout, ensure_ascii=False, separators=(",", ":"))
