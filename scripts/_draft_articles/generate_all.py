#!/usr/bin/env python3
"""Generate all new article bodies + meta.json for assemble_new_articles.py."""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
VG = "https://www.visitgreece.gr/en/islands/cyclades/syros"
VGB = "https://www.visitgreece.gr/en/experiences/beaches/beloved-beaches/beaches-of-syros"
SI = "https://syrosisland.gr/en/"
BSF = "https://www.bluestarferries.com/en"
KTEL = "https://www.ktel-syrou.gr/"  # may redirect; cited as island bus reference via destination guides


def fig(src: str, alt: str, cap: str) -> str:
    return (
        f'<figure class="svs-figure">\n'
        f'  <img src="/Articles/media/{src}" alt="{alt}" loading="lazy" width="1200" height="675" />\n'
        f"  <figcaption>{cap}</figcaption>\n"
        f"</figure>"
    )


def callout(title: str, text: str) -> str:
    return (
        f'<div class="svs-callout">\n'
        f"  <strong>{title}</strong>\n"
        f"  {text}\n"
        f'  <a class="svs-cta" href="/en/Book-now/">Check availability</a>\n'
        f"</div>"
    )


def src(*items):
    return [{"id": f"ref{i+1}", "cite": c, "url": u} for i, (c, u) in enumerate(items)]


ARTICLES: dict = {}


def add(slug: str, **kwargs):
    ARTICLES[slug] = kwargs


add(
    "where-to-stay-syros-areas-compared",
    title="Where to Stay on Syros: Ermoupoli, Kini–Delfini, Galissas, and the South Compared",
    description="Compare Syros stay areas—Ermoupoli, west-coast Kini and Delfini, Galissas, and the southern coast—so you match quiet beaches, nightlife, or a villa week.",
    keywords="where to stay Syros, Syros accommodation areas, Kini vs Ermoupoli, Delfini Beach stay, Galissas Syros",
    published="2026-09-18",
    modified="2026-11-12",
    hero_img="syros-ano-ermoupoli.jpg",
    mid_img="syros-delfini-beach.jpg",
    hero_alt="Ano Syros and Ermoupoli above the harbour",
    hero_caption="Ano Syros and Ermoupoli above the harbour. Photo: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).",
    sources=src(
        ("Visit Greece — Syros (“The lady of the Cyclades”).", VG),
        ("Visit Greece — Beaches of Syros.", VGB),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>Choosing where to stay on Syros matters more than on a one-beach island. Visit Greece calls Syros “the lady of the Cyclades”: a capital island where neoclassical Ermoupoli sits beside quieter coastal settlements, and where town life continues outside July.<sup><a href="#ref1">[1]</a></sup> Book the wrong base and you will spend the week in the car—or miss the calm you came for.</p>
<p>We host on the west coast near Delfini Beach, so this comparison is practical: what each area is good for, what it costs in driving and evening energy, and when a seaside house beats a town hotel.</p>
<h2>Ermoupoli: the capital base</h2>
<p>Ermoupoli is the ferry port, the shopping streets, the evening promenade, and the neoclassical skyline that defines Syros in photographs.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup> Stay here if you want cafés within walking distance, late dinners without a drive, and easy arrivals off the boat.</p>
<p>The trade-off is beach time. The town has swimming spots, but the island’s bigger sandy beaches sit on other coasts. A capital-town stay suits culture-first trips; for swim-every-day villa weeks, most guests prefer a coastal hamlet and day-trip into town.</p>
{fig('syros-ermoupoli-street.jpg','A street in Ermoupoli with neoclassical buildings','Ermoupoli streets: shops, cafés and capital energy. Photo: ElioQoshi / Wikimedia Commons (CC BY 3.0).')}
<h2>Kini and Delfini: west-coast coves and sunsets</h2>
<p>Visit Greece describes Kini as a protected sandy cove with tavernas and memorable sunsets, with Delfini and Varvarousa as smaller neighbouring coves reached by a short walk or by boat.<sup><a href="#ref2">[2]</a></sup></p>
<ul>
<li><strong>Kini</strong> — more services, waterfront dining, a proper sandy cove.</li>
<li><strong>Delfini</strong> — smaller, less organised, excellent for a walk-to-swim house base.</li>
<li><strong>Evenings</strong> — tavernas at Kini; big-night energy still means a drive to Ermoupoli.</li>
</ul>
<p>Sea View Serenity sits about a 10-minute walk from Delfini: swim before breakfast, cook lunch at the house, chase a Kini sunset when you want a table by the water.</p>
{fig('syros-delfini-beach.jpg','Delfini Beach on the west coast of Syros','Delfini Beach, a small west-coast cove. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
{fig('syros-kini-sunset.jpg','Sunset over the sea at Kini, Syros','Sunset light at Kini. Photo: ERWEH / Wikimedia Commons (CC BY-SA 2.5).')}
<h2>Galissas: sandy and family-friendly</h2>
<p>Galissas is one of the island’s better-known sandy beaches—wide, approachable, and popular with families.<sup><a href="#ref2">[2]</a></sup> Stay nearby if a big beach day is the centre of the holiday. It is busier in peak summer than Delfini, so compare noise and parking carefully.</p>
{fig('syros-galissas-beach.jpg','The wide sandy bay at Galissas, Syros','Galissas Beach: a broad sandy bay. Photo: Olavfin / Wikimedia Commons (public domain).')}
<h2>Southern coast notes</h2>
<p>The southern side of Syros is generally more sheltered from the summer meltemi, which is why many larger sandy beaches sit there.<sup><a href="#ref2">[2]</a></sup> Settlements toward Posidonia and neighbouring coves suit guests who want calmer water on windy days. Check walking times to the water and evening options—some southern stays need a car for every dinner out.</p>
{fig('syros-posidonia-coast.jpg','Coastal view on Syros','Coastal Syros light along the water. Photo: Kevin Stroup / Wikimedia Commons (CC BY 3.0).')}
<h2>How to choose in one minute</h2>
<ul>
<li><strong>Cafés and arrivals without a car?</strong> Ermoupoli.</li>
<li><strong>Sunsets, cove swimming, villa kitchen?</strong> Kini–Delfini west coast.</li>
<li><strong>Big sandy beach as daily default?</strong> Galissas or a well-placed southern stay.</li>
<li><strong>Mixed group?</strong> Base where the quietest sleepers are happiest, then day-trip for energy—Syros is small enough that this works.<sup><a href="#ref3">[3]</a></sup></li>
</ul>
{callout('A west-coast house near Delfini','Sea View Serenity is about a 10-minute walk from Delfini Beach: three bedrooms, a full kitchen, parking and a sea-view terrace—with Kini sunsets and Ermoupoli evenings a short drive away.')}
<p>Read every listing for walking minutes to the water, parking, and whether evenings are walkable. On Syros the island is one destination; the base decides the rhythm of every day. If you want a second opinion for your dates and group size, write to us before you book—we would rather steer you honestly than fill a mismatched week.</p>
<p>In August, popular sandy beaches fill early. A quieter cove base plus one or two “big beach” days often feels better than living on the busiest bay all week. In May, June and September almost every area feels spacious, so choose for sunset direction and evening mood instead of crowd avoidance.</p>""",
)

add(
    "seven-day-syros-itinerary-villa-base",
    title="A 7-Day Syros Itinerary from a West-Coast Villa Base",
    description="A practical week on Syros from a Delfini–Kini villa base: beaches, Ermoupoli, Ano Syros, food stops, rest days, and when to keep the car keys on the hook.",
    keywords="7 day Syros itinerary, Syros week itinerary, Syros villa holiday plan, Delfini Kini itinerary",
    published="2026-09-25",
    modified="2026-11-14",
    hero_img="villa-terrace-sunset.jpg",
    mid_img="syros-ermoupoli-view.jpg",
    hero_alt="Deck chairs on the Sea View Serenity terrace at sunset",
    hero_caption="Terrace evening at Sea View Serenity: the reset between busy island days.",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Visit Greece — Beaches of Syros.", VGB),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>A week on Syros works best when you stop trying to “do the island” every morning. Visit Greece frames Syros as a capital Cyclades island with Ermoupoli’s neoclassical town, traditional villages and seaside settlements.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup> From a west-coast villa near Delfini, that mix becomes a calm loop: swim, cook, town, rest, repeat.</p>
<p>This itinerary assumes a hire car and a house about ten minutes’ walk from Delfini Beach. Shift days freely; the order is a suggestion, not a timetable.</p>
<h2>Day 1 — Arrive, settle, local swim</h2>
<p>Ferry or flight into Ermoupoli, drive west, unpack, open the shutters. Keep day one light: a swim at Delfini, groceries, and dinner at the house or a short hop to Kini’s waterfront tavernas.<sup><a href="#ref2">[2]</a></sup> Resist the urge to rush Ermoupoli the same evening you arrive.</p>
{fig('syros-delfini-beach.jpg','Delfini Beach cove on Syros','Delfini: the walk-to-swim start to the week. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Day 2 — West-coast beach day</h2>
<p>Morning at Delfini or Varvarousa; afternoon shade at the house; late-day swim and sunset at Kini.<sup><a href="#ref2">[2]</a></sup> This is the west-coast pattern guests fall into happily—and the reason a kitchen and terrace matter.</p>
{fig('syros-kini-beach.jpg','Kini Beach sandy cove on Syros','Kini Beach for a longer sandy afternoon. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Day 3 — Ermoupoli on foot</h2>
<p>Spend a full town day: Miaouli Square, the waterfront, shops, a long lunch, and an unhurried walk up toward the neoclassical streets.<sup><a href="#ref1">[1]</a></sup> Swim only if you have energy left—Asteria or a quick west-coast dip on the way home.</p>
{fig('syros-ermoupoli-view.jpg','Ermoupoli harbour view on Syros','Ermoupoli from the water: capital day. Photo: Zacharias Mitzelos / Wikimedia Commons (CC0).')}
<h2>Day 4 — Southern beaches (plan B for wind)</h2>
<p>When the meltemi kicks up, point the car south for more sheltered sandy bays such as Galissas.<sup><a href="#ref2">[2]</a></sup> Pack a picnic from the villa kitchen and treat it as a change-of-scene day, not a checklist.</p>
{fig('syros-galissas-beach.jpg','Galissas Beach on Syros','Galissas for a wider sandy bay. Photo: Olavfin / Wikimedia Commons (public domain).')}
<h2>Day 5 — Ano Syros and a slow evening</h2>
<p>Walk the lanes of Ano Syros above Ermoupoli for views and a different pace from the port town.<sup><a href="#ref3">[3]</a></sup> Return west for a terrace sunset and a home-cooked meal—groups often rate this as their favourite quiet night.</p>
{fig('syros-ano-syros-view.jpg','View of Ermoupoli from Ano Syros','Looking down on Ermoupoli from Ano Syros. Photo: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0).')}
<h2>Day 6 — Free day or mini adventure</h2>
<p>Repeat a favourite beach, book a boat trip if the sea is kind, or linger in Ermoupoli’s cafés. Leave space. A villa week fails when every hour is scheduled.</p>
<h2>Day 7 — Pack, last swim, ferry buffer</h2>
<p>Morning swim, tidy the kitchen, drive to the port with margin. Syros departures are straightforward, but summer queues and luggage still reward an unhurried start.<sup><a href="#ref3">[3]</a></sup></p>
{callout('Base the week near Delfini','Sea View Serenity gives you the swim-cook-town loop: walk to Delfini, drive to Kini and Ermoupoli, and come home to a full kitchen and sea-view terrace.')}
<p>If you only remember one rule: protect two empty afternoons. Syros rewards travellers who leave room for a second swim and a long table.</p>
<p>Families can swap Day 5 for another beach day; couples can add a longer Ermoupoli dinner. Digital nomads can treat Days 2 and 4 as half-work days with a late swim. The villa base absorbs all three styles without changing hotels mid-week.</p>""",
)

add(
    "getting-around-syros-car-rental-bus",
    title="Getting Around Syros: Car Rental, Buses, Taxis, and When You Can Skip the Car",
    description="How to get around Syros from a west-coast stay: when a hire car is worth it, what buses and taxis cover, and how ferry-port logistics fit a Delfini–Kini villa week.",
    keywords="Syros car rental, getting around Syros, Syros bus, Syros taxi, Syros without a car",
    published="2026-10-02",
    modified="2026-11-15",
    hero_img="syros-ferry-port.jpg",
    mid_img="syros-harbour.jpg",
    hero_alt="Ferry boat in the port of Syros",
    hero_caption="Ferry in Syros port—arrival is the easy part; island logistics come next. Photo: Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Visit Greece — Beaches of Syros.", VGB),
        ("Syros Island official travel guide.", SI),
        ("Blue Star Ferries — official site (routes and bookings).", BSF),
    ),
    body=f"""<p>Syros looks small on a map. In practice, hills, beach bags and summer heat decide whether “we’ll manage without a car” feels freeing or frustrating. Visit Greece and the island’s own guide present Syros as a capital island with a working port town and scattered coastal settlements—not a single resort strip.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<p>We host near Delfini Beach. From here, a car is the default for most guests, but not always mandatory. Here is the honest split.</p>
<h2>When a hire car is worth it</h2>
<ul>
<li>You are based on the west coast and want Ermoupoli, Galissas or southern beaches in the same week.<sup><a href="#ref2">[2]</a></sup></li>
<li>You travel with children, beach gear, or groceries for a villa kitchen.</li>
<li>You want flexibility when the meltemi makes one coast choppy and another calmer.<sup><a href="#ref2">[2]</a></sup></li>
</ul>
<p>Parking at the house removes the daily hunt for a space. Ask any listing whether parking is on-site before you book.</p>
{fig('syros-harbour.jpg','Syros harbour at Ermoupoli','Ermoupoli harbour: where cars, taxis and travellers meet the ferry. Photo: Rberteig / Wikimedia Commons (CC BY 2.0).')}
<h2>Buses and taxis</h2>
<p>Public buses link Ermoupoli with coastal villages in season; timetables thin outside summer and in the evenings. Treat the bus as a useful backup for beach days, not as a door-to-door villa solution. Taxis work well for ferry arrivals and dinner in town if you prefer not to drive at night—book ahead in peak weeks.</p>
<p>Always verify the current seasonal timetable locally or via official island information before you rely on a last bus back west.<sup><a href="#ref3">[3]</a></sup></p>
<h2>Ferry port logistics</h2>
<p>Most visitors arrive by ferry into Ermoupoli; flight connections also serve the island via Athens.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref4">[4]</a></sup> Collect a hire car near the port if you can, or take a taxi to the villa and rent the next morning. Build buffer time on departure day—summer queues are normal.</p>
{fig('syros-from-ferry.jpg','Ermoupoli seen from an approaching ferry','Ermoupoli from the ferry: first and last view for many travellers. Photo: Zde / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Can you skip the car from Delfini?</h2>
<p>Yes, if your plan is mostly walking to Delfini, cooking at the house, and only occasional taxi trips to Ermoupoli or Kini. No, if you want a different beach every day or late dinners in town without pre-booking rides. Tell us how you travel when you enquire—we will say plainly whether your plan fits.</p>
{callout('Park at the house, swim on foot','Sea View Serenity has parking at the property and a 10-minute walk to Delfini—so the car works for island days, not for every morning swim.')}
<p>Whatever you choose, decide before arrival. Mixing “no car” optimism with a west-coast villa and four beach bags is the fastest way to spend holiday money on repeated taxis.</p>
<p>One more tip: if you only rent for four days of a seven-day stay, take the car for southern beach days and Ermoupoli stock-ups, then return it and finish the week on foot and taxi. That hybrid saves money without trapping you on one cove.</p>""",
)

# Write progress and continue in same script below
print("defined first 3")

add(
    "kini-restaurants-sunset-dining",
    title="Kini Restaurants and Sunset Dining on Syros’s West Coast",
    description="How to plan sunset dinners in Kini, with Delfini as a quiet swim base: west-coast tavernas, timing tips, and when to drive into Ermoupoli instead.",
    keywords="Kini restaurants, Kini sunset dinner, Syros west coast tavernas, Delfini Beach dining",
    published="2026-10-08",
    modified="2026-11-16",
    hero_img="syros-kini-sunset.jpg",
    mid_img="syros-kini-beach.jpg",
    hero_alt="Sunset over the sea at Kini, Syros",
    hero_caption="Sunset at Kini—the west coast’s dinner theatre. Photo: ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
    sources=src(
        ("Visit Greece — Beaches of Syros (Kini sunsets and tavernas).", VGB),
        ("Visit Greece — Syros.", VG),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>Kini is where many Syros evenings quietly peak. Visit Greece highlights it as a protected sandy cove with tavernas and memorable sunsets, with smaller coves such as Delfini nearby.<sup><a href="#ref1">[1]</a></sup> If you are based on the west coast, that geography is a gift: swim late, rinse off, and sit down as the light drops into the Aegean.</p>
<p>This is not a ranked restaurant list. Menus and ownership change; what stays reliable is the pattern—waterfront tables, seafood and Greek standards, and timing that respects sunset.</p>
<h2>Why Kini works for dinner</h2>
<ul>
<li>The bay faces the evening light.<sup><a href="#ref1">[1]</a></sup></li>
<li>You can combine a sandy swim with a short stroll to dinner.</li>
<li>It is calmer than Ermoupoli’s busiest nights, yet still social.</li>
</ul>
{fig('syros-kini-beach.jpg','Kini Beach on Syros with sandy shore','Kini by day: sand, shallows and a village pace. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Delfini as the quiet swim base</h2>
<p>Delfini is smaller and less organised—bring your own shade—and excellent for a last swim before dinner.<sup><a href="#ref1">[1]</a></sup> From Sea View Serenity it is about a ten-minute walk. Many guests swim there, change at the house, then drive or walk toward Kini for a table.</p>
{fig('syros-delfini-beach.jpg','Delfini Beach small cove','Delfini: quieter water before a Kini evening. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Timing and practical tips</h2>
<ul>
<li>In July and August, arrive early or ask about reservations for waterfront seats.</li>
<li>Carry a light layer; wind on the west coast can cool quickly after sunset.</li>
<li>Agree a designated driver or taxi if you plan wine with the sunset.</li>
<li>For a louder, more varied night, drive to Ermoupoli instead—the capital has deeper café and restaurant choice.<sup><a href="#ref2">[2]</a></sup><sup><a href="#ref3">[3]</a></sup></li>
</ul>
{fig('villa-terrace-sunset.jpg','Terrace chairs facing a Syros sunset','Some evenings skip the taverna: terrace dinner at the house works just as well.')}
{callout('Swim at Delfini, dine toward Kini','Stay at Sea View Serenity for the walk-to-cove mornings and west-coast sunset nights—kitchen and terrace included when you want to eat in.')}
<p>Build two Kini sunset dinners into a week, not seven. The ritual stays special when you alternate with home cooking and one Ermoupoli night.</p>
<p>Ask locally what is freshly landed; Syros’s west-coast tables are at their best when you order simply and watch the sky finish the meal.</p>""",
)

add(
    "syros-in-may-june-september",
    title="Syros in May, June and September: Why Shoulder Season Suits a Villa Stay",
    description="Why May, June and September are often the sweet spot for a Syros villa holiday: sea temperatures, crowds, ferry life, and west-coast evenings without peak-August pressure.",
    keywords="Syros in May, Syros in June, Syros in September, best time Syros villa, shoulder season Cyclades",
    published="2026-10-14",
    modified="2026-11-18",
    hero_img="villa-bedroom-balcony.jpg",
    mid_img="syros-kini-sunset.jpg",
    hero_alt="Bedroom with open shutters to bougainvillea and sea",
    hero_caption="Shoulder-season light through open shutters at Sea View Serenity.",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Visit Greece — Beaches of Syros.", VGB),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>Peak August on any Cycladic island is loud, hot and expensive. Syros softens that problem earlier and later in the season because it is a year-round capital island, not a resort that wakes up only for six weeks.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<p>If you want a villa week with swimming, cooking and town days—without fighting for every parking space—look hard at May, June and September.</p>
<h2>May — green hills, cool evenings</h2>
<p>May brings longer days and quieter beaches. The sea is still fresh; some travellers swim daily, others wade and enjoy the terrace. Ermoupoli’s cafés are open, and west-coast sunsets already deliver.<sup><a href="#ref2">[2]</a></sup> Pack a light jumper for evenings; bedrooms with radiators help on cooler nights.</p>
<h2>June — the sweetest full-summer start</h2>
<p>June is when sea and air usually align for long beach days while villages still feel human-scale. Book ferries and the villa earlier than you think—shoulder demand has risen as travellers avoid August heat.</p>
{fig('syros-delfini-beach.jpg','Quiet Delfini Beach cove','Delfini in quieter months: space to swim without a crowd. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>September — warm sea, softer nights</h2>
<p>September often keeps excellent swimming while nightlife pressure drops. It is a favourite month for couples and remote workers who want Ermoupoli open and coves uncrowded.<sup><a href="#ref1">[1]</a></sup> Watch for the first autumn wind shifts and keep a southern beach as plan B.<sup><a href="#ref2">[2]</a></sup></p>
{fig('syros-kini-sunset.jpg','Kini sunset over the Aegean','September sunsets at Kini still linger. Photo: ERWEH / Wikimedia Commons (CC BY-SA 2.5).')}
<h2>What you gain versus July–August</h2>
<ul>
<li>Easier restaurant timing and parking.</li>
<li>More spontaneous day plans.</li>
<li>Better sleep in a stone house that breathes at night.</li>
<li>A fairer chance to enjoy Delfini as a small cove, not a squeeze.</li>
</ul>
{fig('villa-terrace-sunset.jpg','Sea View Serenity terrace at golden hour','Terrace evenings are the point of a shoulder-season villa week.')}
{callout('Book the quiet months on purpose','Sea View Serenity is built for swim-and-cook weeks—May, June and September are when that rhythm feels most generous.')}
<p>July and August still work if schools dictate your dates. Just plan more early starts and more home dinners. If your calendar is flexible, let Syros’s shoulder months do half the hospitality work for you.</p>
<p>Early October can also shine, but ferry frequency and weather variance rise—treat it as a bonus window for flexible travellers, not a guarantee.</p>""",
)

add(
    "things-to-do-on-syros",
    title="Things to Do on Syros: Beaches, Ermoupoli, Food, and Easy Day Plans",
    description="A practical hub guide to things to do on Syros—west-coast beaches, Ermoupoli and Ano Syros, food, and simple day plans from a seaside villa base.",
    keywords="things to do on Syros, Syros attractions, Syros beaches, Ermoupoli things to do, Syros holiday ideas",
    published="2026-10-20",
    modified="2026-11-19",
    hero_img="syros-ermoupoli-pano.jpg",
    mid_img="syros-kini-beach.jpg",
    hero_alt="Panoramic view of Ermoupoli on Syros",
    hero_caption="Ermoupoli: the island’s to-do list starts with a real town. Photo: Zacharias Mitzelos / Wikimedia Commons (CC0).",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Visit Greece — Beaches of Syros.", VGB),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>Syros is not an island you “finish.” Visit Greece presents it as a capital Cyclades destination with neoclassical Ermoupoli, villages and seaside settlements.<sup><a href="#ref1">[1]</a></sup> Use this as a hub: pick two or three ideas a day, then go home to the terrace.</p>
<h2>Swim the coasts deliberately</h2>
<p>West-coast Kini, Delfini and Varvarousa bring sunsets and smaller coves; southern beaches such as Galissas offer wider sand and often better shelter from the meltemi.<sup><a href="#ref2">[2]</a></sup> Build variety instead of repeating one bay until it bores you.</p>
{fig('syros-kini-beach.jpg','Kini Beach Syros','Kini for sand and village energy. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
{fig('syros-galissas-beach.jpg','Galissas Beach Syros','Galissas for a broad sandy day. Photo: Olavfin / Wikimedia Commons (public domain).')}
<h2>Spend real time in Ermoupoli</h2>
<p>Walk the waterfront, duck into side streets, eat a proper lunch, and stay for evening café life.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup> Syros’s advantage over purely resort islands is this town—use it.</p>
{fig('syros-ermoupoli-street.jpg','Street scene in Ermoupoli','Ermoupoli streets reward slow wandering. Photo: ElioQoshi / Wikimedia Commons (CC BY 3.0).')}
<h2>Climb into Ano Syros</h2>
<p>Above the port, Ano Syros offers lanes, views and a different historical layer from neoclassical Ermoupoli.<sup><a href="#ref3">[3]</a></sup> Go early or late to avoid midday heat.</p>
{fig('syros-ano-syros-view.jpg','Ermoupoli seen from Ano Syros','Views from Ano Syros back over Ermoupoli. Photo: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0).')}
<h2>Eat like you have a kitchen</h2>
<p>Shop locally, cook at the villa, and spend restaurant budget on a few excellent coastal or town meals. Loukoumi and Syros sweets are part of the island’s food identity—taste them in town, then go back to swimming.</p>
<h2>Keep one empty day</h2>
<p>The best “thing to do” on Syros is often nothing scheduled: a second swim at Delfini and a long sunset.<sup><a href="#ref2">[2]</a></sup></p>
{callout('Do Syros from a calm base','Sea View Serenity near Delfini keeps beaches, Ermoupoli days and empty afternoons in one loop—without changing hotels.')}
<p>Link outward from here to deeper guides on beaches, food, getting around and week-long itineraries. Syros rewards curiosity; it punishes over-scheduling.</p>
<p>If you travel with children, prioritise sandy entries and midday shade. If you travel to work remotely, protect mornings and treat Ermoupoli as an evening reward. Same island, different pacing—both fit a villa base.</p>""",
)

print("defined 6")

add(
    "ano-syros-ermoupoli-walking-guide",
    title="Ano Syros and Ermoupoli Walking Guide: Two Towns, One Capital Island",
    description="A walking guide to Ermoupoli and Ano Syros: neoclassical streets, harbour life, hill lanes, viewpoints, and how to pair a town day with a west-coast villa stay.",
    keywords="Ano Syros walking, Ermoupoli walking guide, Syros old town, things to do Ermoupoli",
    published="2026-10-26",
    modified="2026-11-20",
    hero_img="syros-ano-syros-view.jpg",
    mid_img="syros-ermoupoli-street.jpg",
    hero_alt="View of Ermoupoli from Ano Syros",
    hero_caption="Ermoupoli from Ano Syros—walk both layers of the capital. Photo: NNeilAlieNN / Wikimedia Commons (CC BY-SA 3.0).",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Syros Island official travel guide.", SI),
        ("Visit Greece — Beaches of Syros.", VGB),
    ),
    body=f"""<p>Ermoupoli and Ano Syros are the same skyline and two different walks. Visit Greece and the island guide present Syros’s capital character through neoclassical Ermoupoli and the older hill settlement above it.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup></p>
<p>Do them on foot. The point is texture—steps, shutters, harbour light—not ticking monuments at speed.</p>
<h2>Start on the waterfront</h2>
<p>Begin at the port and Miaouli Square area: cafés, ferries, and the open feeling of a working island capital.<sup><a href="#ref1">[1]</a></sup> Duck one street inland whenever a lane looks promising; Ermoupoli rewards small detours.</p>
{fig('syros-ermoupoli-street.jpg','Neoclassical street in Ermoupoli','Inland Ermoupoli: shade, stone and shopfronts. Photo: ElioQoshi / Wikimedia Commons (CC BY 3.0).')}
{fig('syros-ermoupoli-pano.jpg','Wide view of Ermoupoli','Ermoupoli’s spread above the harbour. Photo: Zacharias Mitzelos / Wikimedia Commons (CC0).')}
<h2>Climb to Ano Syros</h2>
<p>The climb is the experience: stepped lanes, quieter residential corners, and views back over rooftops to the sea.<sup><a href="#ref2">[2]</a></sup> Wear proper shoes, carry water, and avoid the hottest midday window in summer.</p>
{fig('syros-ano-ermoupoli.jpg','Ano Syros and Ermoupoli together','Both towns in one frame. Photo: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).')}
<h2>Pair town with sea</h2>
<p>A classic day from a west-coast villa: morning swim at Delfini or Kini, afternoon town walk, evening back west for sunset—or dinner in Ermoupoli if you want capital energy.<sup><a href="#ref3">[3]</a></sup></p>
{callout('Town days, cove nights','Sea View Serenity keeps Ermoupoli a day trip, not your only soundtrack—walk the capital, sleep by the west-coast water.')}
<p>If mobility is limited, enjoy Ermoupoli’s flatter harbour zone thoroughly and treat Ano Syros viewpoints as optional. Syros is generous either way.</p>
<p>Photographers: late afternoon light on the neoclassical façades is kinder than noon. Night walks along the illuminated harbour are safe-feeling and lively in season—another reason this capital island differs from emptier Cycladic stops.</p>""",
)

add(
    "day-trips-from-syros-tinos-mykonos",
    title="Day Trips from Syros to Tinos and Mykonos (and Why Syros Is the Better Base)",
    description="How to use Syros as a calm Cyclades base for ferry day trips toward Tinos and Mykonos—plus timing tips and why coming home to a quiet west-coast villa matters.",
    keywords="day trips from Syros, Syros to Tinos ferry, Syros to Mykonos day trip, Cyclades island hopping base",
    published="2026-11-01",
    modified="2026-11-21",
    hero_img="tinos-sunset-over-syros.jpg",
    mid_img="syros-ferry-port.jpg",
    hero_alt="Sunset over Syros seen from the port of Tinos",
    hero_caption="Syros on the horizon from Tinos—close enough for a day, calm enough to base. Photo: Jules Verne Times Two / Wikimedia Commons (CC BY-SA 4.0).",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Blue Star Ferries — official site.", BSF),
        ("Syros Island official travel guide.", SI),
        ("Visit Greece — Beaches of Syros.", VGB),
    ),
    body=f"""<p>One reason travellers underestimate Syros is that they treat famous neighbours as the main event. Flip it: base on Syros for sleep and swimming, then take a ferry day toward Tinos or Mykonos when you want contrast.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<h2>Why Syros works as the hub</h2>
<p>Ermoupoli is a real port town with year-round bones, while west-coast coves such as Kini and Delfini give you quiet water when you return.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref4">[4]</a></sup> That combination is rarer than another pretty Airbnb on a louder island.</p>
{fig('syros-ferry-port.jpg','Ferry boat in Syros port','Day trips start in Ermoupoli’s port. Photo: Redon Skikuli / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Tinos day trip — culture and villages</h2>
<p>Tinos pairs pilgrimage heritage with inland villages and a different island texture. Check same-day return ferries on official operator sites before you commit, and build buffer for wind delays.<sup><a href="#ref2">[2]</a></sup></p>
{fig('tinos-sunset-over-syros.jpg','Sunset view toward Syros from Tinos','Looking back toward Syros from Tinos at sunset. Photo: Jules Verne Times Two / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Mykonos day trip — see it, don’t sleep in it</h2>
<p>Mykonos is easy to sample and expensive to base in. A daylight ferry visit can cover a beach or town wander; returning to Syros keeps your nights quieter and often better value.<sup><a href="#ref1">[1]</a></sup></p>
<h2>Practical rules</h2>
<ul>
<li>Book outward and return tickets that leave margin for queues.</li>
<li>Travel light; day-trip luggage slows everyone.</li>
<li>Check wind forecasts—Cycladic schedules flex in meltemi season.<sup><a href="#ref4">[4]</a></sup></li>
<li>Keep the next morning empty; ferry days are longer than they look.</li>
</ul>
{callout('Come home to Delfini quiet','Use Sea View Serenity as the calm base: ferry out for a famous-island day, then swim and cook on Syros’s west coast.')}
<p>Island-hopping is optional. Many guests realise after one week that Syros alone was the trip—and the famous names can wait for another year.</p>
<p>Always re-check operator timetables close to travel; routes and frequencies change by season. Official ferry sites beat screenshot advice from last summer.<sup><a href="#ref2">[2]</a></sup></p>""",
)

add(
    "pet-friendly-syros-villa-stay",
    title="Pet-Friendly Syros Villa Stays: What to Ask Before You Bring the Dog",
    description="Practical guidance for visiting Syros with a dog: villa rules to confirm, beach etiquette, heat and transport tips, and how to plan a calm west-coast stay.",
    keywords="pet friendly Syros, Syros with a dog, dog friendly villa Greece, Syros pet travel",
    published="2026-11-05",
    modified="2026-11-22",
    hero_img="villa-terrace-sunset.jpg",
    mid_img="syros-delfini-beach.jpg",
    hero_alt="Terrace at Sea View Serenity facing the sea",
    hero_caption="A calm terrace helps pets and people reset after island days.",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Visit Greece — Beaches of Syros.", VGB),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>Travelling with a dog on a Greek island can be wonderful—and it can go wrong fast in August heat if you improvise. Syros helps because it has a real town for supplies and quieter coastal stretches for calmer walks.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<p>Sea View Serenity may be able to welcome pets in some cases, but never assume: ask us before you book, and treat any agreement as part of the house rules.</p>
<h2>Questions to confirm in writing</h2>
<ul>
<li>Size, number of pets, and whether they are left alone.</li>
<li>Fee or cleaning expectations.</li>
<li>Furniture and bedroom rules.</li>
<li>Nearby outdoor space and road safety.</li>
</ul>
<h2>Beaches and heat</h2>
<p>Not every beach welcomes dogs, and rules can be seasonal or locally enforced. Start early, carry water, and avoid hot sand midday. West-coast coves near Kini and Delfini are quieter than the busiest southern sands, but you still need to respect local practice and other swimmers.<sup><a href="#ref2">[2]</a></sup></p>
{fig('syros-delfini-beach.jpg','Delfini Beach cove','Quieter coves are easier for careful pet owners—still ask locally. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
{fig('syros-kini-beach.jpg','Kini Beach','Kini’s village beach life means more people—plan walks for off-peak hours. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Town practicalities</h2>
<p>Ermoupoli is where you will find pet supplies more easily than in a tiny coastal hamlet.<sup><a href="#ref1">[1]</a></sup> Keep ferry logistics in mind: animals need compliant carriers or leads and patience at the port.</p>
{callout('Ask first, then pack for the dog','If we agree a pet stay at Sea View Serenity, you get a west-coast house base with terrace space—and clear rules so everyone relaxes.')}
<p>A pet-friendly holiday is mostly preparation: shade, water, flexible beach plans, and honesty with your hosts. Do that, and Syros is a gentle island for travelling with a dog.</p>
<p>If your dog is reactive or unused to new places, consider a quieter shoulder-season week. Peak summer ferries and busy beach parking are stressful for animals and owners alike.</p>""",
)

add(
    "packing-meltemi-wind-guide-syros",
    title="Packing for Syros and the Meltemi: Wind, Layers, and Plan-B Beaches",
    description="What to pack for Syros in meltemi season: wind-aware clothing, beach kit, and how to switch coasts when the west-facing coves get choppy.",
    keywords="meltemi Syros, packing list Syros, Cyclades wind, Syros beach plan B",
    published="2026-11-08",
    modified="2026-11-23",
    hero_img="syros-kini-sunset.jpg",
    mid_img="syros-galissas-beach.jpg",
    hero_alt="Sunset sky over Kini on Syros",
    hero_caption="Beautiful west-coast light can arrive with wind—pack for both. Photo: ERWEH / Wikimedia Commons (CC BY-SA 2.5).",
    sources=src(
        ("Visit Greece — Beaches of Syros (meltemi note and coastal variety).", VGB),
        ("Visit Greece — Syros.", VG),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>The meltemi is the summer northerly wind that shapes Cycladic beach days. Visit Greece’s Syros beach guidance notes coastal differences and the practical need to choose shores with wind in mind.<sup><a href="#ref1">[1]</a></sup> Pack as if beauty and breeze arrive together.</p>
<h2>Clothing that works</h2>
<ul>
<li>A light windbreaker or overshirt for boat decks and sunsets.</li>
<li>One warmer layer for May/October evenings.</li>
<li>Secure hats; cheap straw hats become kites.</li>
<li>Reef-safe sunscreen and sunglasses with a grip.</li>
</ul>
<h2>Beach bag for west-coast coves</h2>
<p>Delfini-style coves are less organised—bring shade, water and footwear for rocky entries.<sup><a href="#ref1">[1]</a></sup> A compact picnic from the villa kitchen beats hunting for an open canteen on a windy afternoon.</p>
{fig('syros-delfini-beach.jpg','Delfini Beach','Small coves shine when you bring your own kit. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
<h2>Plan-B coasts</h2>
<p>When the west feels rough, drive toward more sheltered southern sandy beaches such as Galissas.<sup><a href="#ref1">[1]</a></sup> That is the advantage of a hire car and a villa base: you change bay, not hotel.</p>
{fig('syros-galissas-beach.jpg','Galissas Beach wide bay','Galissas as a sandy, often more sheltered alternative. Photo: Olavfin / Wikimedia Commons (public domain).')}
<h2>House days are not failed days</h2>
<p>Strong wind days are for cooking, reading, Ermoupoli streets and early night.<sup><a href="#ref2">[2]</a></sup><sup><a href="#ref3">[3]</a></sup> Guests who accept that rhythm enjoy Syros more than guests who fight the forecast.</p>
{callout('A base that absorbs windy days','Sea View Serenity gives you Delfini on calm mornings, southern options by car, and a terrace kitchen when the meltemi owns the afternoon.')}
<p>Check a marine-aware forecast, not only a city temperature app. And never fight the sea—Syros has enough coastline to choose humility and still have a great swim.</p>
<p>Packing light still wins: two swimsuits, quick-dry towel, laundry detergent pods for the villa machine, and one nice outfit for Ermoupoli. Everything else is optional weight.</p>""",
)

add(
    "grocery-self-catering-delfini-kini",
    title="Self-Catering near Delfini and Kini: Groceries, Bakeries, and Villa Cooking",
    description="How to self-cater from a west-coast Syros villa near Delfini and Kini: where to shop, what to cook, and how Ermoupoli fits a practical grocery run.",
    keywords="Syros groceries, self catering Syros, Kini bakery, villa cooking Syros, Delfini self catering",
    published="2026-11-12",
    modified="2026-11-24",
    hero_img="villa-kitchen.jpg",
    mid_img="villa-dining-living.jpg",
    hero_alt="Kitchen at Sea View Serenity",
    hero_caption="A full villa kitchen turns Syros shopping into easy terrace meals.",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Visit Greece — Beaches of Syros.", VGB),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>A west-coast villa week gets better the moment you stop eating every meal out. Syros makes that easy: Ermoupoli has proper shops, coastal villages have bakeries and small stores in season, and a full kitchen turns beach days into simple feasts.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<h2>The first shop</h2>
<p>After arrival, do one solid Ermoupoli supermarket run: breakfast staples, fruit, salad, pasta or grains, water, coffee, and something to grill or roast. Then top up locally near Kini when you only need bread, fruit or ice.</p>
{fig('villa-kitchen.jpg','Villa kitchen counters and appliances','Kitchen basics at Sea View Serenity: cook after the swim, don’t queue for lunch.')}
<h2>Cook around the beach rhythm</h2>
<ul>
<li>Big breakfast after a Delfini swim.<sup><a href="#ref2">[2]</a></sup></li>
<li>Late lunch in shade at the house.</li>
<li>Two or three dinners out at Kini or Ermoupoli; the rest at the dining table.</li>
</ul>
{fig('villa-dining-living.jpg','Dining table and living room arch','One table for the whole group—self-catering is social, not second-best.')}
<h2>What tastes like Syros</h2>
<p>Buy local cheese, tomatoes, herbs, honey and sweets in town. Save restaurant budget for fish dinners and special nights rather than average lunches.</p>
{fig('syros-kini-beach.jpg','Kini Beach','Kini days pair well with a simple home dinner afterward. Photo: FocalPoint / Wikimedia Commons (CC BY-SA 4.0).')}
{callout('Kitchen + cove = the west-coast formula','Sea View Serenity near Delfini is set up for self-catering: full kitchen, dining space, parking for the big shop, and the beach a short walk away.')}
<p>Self-catering is not about thrift alone. It is how groups stay flexible when children melt down, when the wind rises, or when the sunset is too good to leave the terrace.</p>
<p>Bring a reusable shopping bag, a cooler bag for the drive west, and a short list—Syros shops are good, but holiday hunger makes people overbuy.</p>""",
)

add(
    "winter-year-round-syros",
    title="Syros Year-Round: Why the Capital Island Still Works Outside Summer",
    description="Why Syros remains interesting outside peak summer: Ermoupoli’s year-round town life, shoulder and winter realities, and how a west-coast house adapts when beach days shorten.",
    keywords="Syros in winter, year round Syros, Ermoupoli off season, Syros shoulder season villa",
    published="2026-11-16",
    modified="2026-11-25",
    hero_img="villa-living-fireplace.jpg",
    mid_img="syros-ermoupoli-view.jpg",
    hero_alt="Living room with stone fireplace at Sea View Serenity",
    hero_caption="Fireplace season: Syros as a year-round capital island, not only a beach stop.",
    sources=src(
        ("Visit Greece — Syros (year-round capital character).", VG),
        ("Syros Island official travel guide.", SI),
        ("Visit Greece — Beaches of Syros.", VGB),
    ),
    body=f"""<p>Most Cycladic islands thin out dramatically after summer. Syros behaves differently because Ermoupoli is an administrative and cultural capital with life beyond tourism peaks.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref2">[2]</a></sup></p>
<p>That does not mean January is a beach holiday. It means shoulder months and quieter seasons can still feel like a real place.</p>
<h2>What stays open in spirit</h2>
<p>Cafés, shops and a town rhythm continue in Ermoupoli more reliably than on purely seasonal islands.<sup><a href="#ref1">[1]</a></sup> Coastal tavernas may run shorter hours—verify as you go.</p>
{fig('syros-ermoupoli-view.jpg','Ermoupoli harbour and town','Ermoupoli keeps Syros feeling inhabited outside peak summer. Photo: Zacharias Mitzelos / Wikimedia Commons (CC0).')}
<h2>West-coast houses in cooler months</h2>
<p>Expect fewer swim days, more walks, more cooking, and earlier nights. A living room with a fireplace and bedrooms with radiators change the experience from “closed beach villa” to “island home week.”</p>
{fig('villa-living-fireplace.jpg','Stone fireplace and seating','Indoor warmth matters when evenings cool.')}
<h2>Best off-peak windows</h2>
<ul>
<li>Late spring and September–October for hybrid beach-and-town trips.<sup><a href="#ref3">[3]</a></sup></li>
<li>True winter for travellers who want writing, rest and capital-town cafés—not guaranteed swimming.</li>
</ul>
{fig('syros-ano-ermoupoli.jpg','Ano Syros and Ermoupoli','Winter light on the capital skyline. Photo: Hans Peter Schaefer / Wikimedia Commons (CC BY-SA 3.0).')}
{callout('A house for more than six beach days','Sea View Serenity is as much about terrace breakfasts and fireplace evenings as about Delfini swims—ask us about shoulder and off-season stays.')}
<p>If you need every service at summer strength, stay in June–September. If you want Syros as a place rather than a product, step outside the peak and let Ermoupoli lead.</p>
<p>Ferry schedules thin in winter—build flexible plans and confirm sailings close to departure. The reward is an island you do not have to share with peak crowds.</p>""",
)

add(
    "multi-gen-group-villa-syros",
    title="Multi-Gen and Group Villa Stays on Syros: Space, Pace, and Honest Logistics",
    description="How to plan a multi-generation or friends group villa stay on Syros: sleeping layouts, beach pacing, cooking for a crowd, and why a west-coast house near Delfini works.",
    keywords="group villa Syros, multi generational holiday Greece, large group Syros, family group villa Cyclades",
    published="2026-11-20",
    modified="2026-11-26",
    hero_img="villa-dining-living.jpg",
    mid_img="villa-bedroom-sea-view.jpg",
    hero_alt="Dining and living areas opening through a stone arch",
    hero_caption="One table, several generations: the villa layout that makes group weeks work.",
    sources=src(
        ("Visit Greece — Syros.", VG),
        ("Visit Greece — Beaches of Syros.", VGB),
        ("Syros Island official travel guide.", SI),
    ),
    body=f"""<p>Group trips fail on islands when the house is a cluster of bedrooms with nowhere to gather—or when every day requires consensus to cross the island. Syros helps because you can mix quiet west-coast swimming with capital-town outings without changing accommodation.<sup><a href="#ref1">[1]</a></sup><sup><a href="#ref3">[3]</a></sup></p>
<p>Sea View Serenity sleeps six comfortably across three bedrooms (with extra beds possible by arrangement). That scale suits many multi-gen families and friend groups—ask us before you assume eight will feel spacious.</p>
<h2>Design the week around choice</h2>
<ul>
<li>Beach mornings for whoever wants them at Delfini or Kini.<sup><a href="#ref2">[2]</a></sup></li>
<li>Optional Ermoupoli afternoons for shoppers and café people.</li>
<li>Shared dinners most nights; one or two restaurant celebrations.</li>
<li>At least one fully empty day with no negotiations.</li>
</ul>
{fig('villa-dining-living.jpg','Group dining table in the villa','The dining table is the group’s headquarters.')}
{fig('villa-bedroom-sea-view.jpg','Bedroom with sea-facing window','Quiet rooms matter when naps and early nights diverge.')}
<h2>Logistics that prevent arguments</h2>
<p>Hire a car that fits beach gear, or two small cars if drivers prefer independence. Do one big grocery shop on day one. Agree a shared cleanup rhythm. Put sunset dinners at Kini on the calendar early so they feel like events, not debates.<sup><a href="#ref2">[2]</a></sup></p>
{fig('syros-kini-sunset.jpg','Sunset at Kini','One shared sunset dinner can anchor a whole group week. Photo: ERWEH / Wikimedia Commons (CC BY-SA 2.5).')}
<h2>Celebrations without venue fiction</h2>
<p>A villa can host a birthday lunch or a small reunion dinner. It is not a wedding venue by default. If you need special setups, ask early and keep expectations domestic rather than event-production scale.</p>
{callout('Room for the whole crew—within reason','Sea View Serenity near Delfini is built for shared meals, sea views and mixed-pace days. Tell us your headcount and we will say yes only when it will still feel comfortable.')}
<p>The best group compliment we hear is simple: everyone got their version of the holiday in one house. That is the west-coast villa promise when you plan for difference instead of forcing identical days.</p>
<p>Travelling with teens plus grandparents? Give teens a beach-and-independence brief, give grandparents shade and shorter walks, and meet at the table. Syros is gentle enough for that choreography.</p>""",
)

assert len(ARTICLES) == 13, len(ARTICLES)

meta = {}
for slug, data in ARTICLES.items():
    body = data.pop("body")
    (OUT / f"{slug}.body.html").write_text(body, encoding="utf-8")
    meta[slug] = data
    wc = len(body.split())
    print(f"{slug}: {wc} words")

(OUT / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote meta.json", len(meta))
