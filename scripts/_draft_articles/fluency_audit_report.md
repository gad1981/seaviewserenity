# Fluency audit: 13 new articles × el / fr / de / it / he

Source: `i18n/articles.json`. Scope: 13 new slugs × 5 languages. Metadata (title, description, keywords, kicker) was read for all 65 entries. Bodies were spot-checked with the opening paragraph and a mid-section for 5 articles in each language (6 for `he`). Automated checks covered all 65 bodies.

## Automated checks (all 65 entries)

- **HTML:** tag sequences are well formed. The only parser flags were `<img … />` inside `<figure>`, which are false positives. No broken or unclosed tags.
- **English leftovers:** no English sentences in any body. The Latin-script text that remains is proper names or credits (Visit Greece, Sea View Serenity, Ferryhopper, Seajets, Blue Star Ferries, KTEL, HNMS, image credits). Greek has a few loanwords: `beach bar`, `beach clubs`, `snorkelling`, `windsurfing`, `microchip`, `island hopping`, `brand`, `delicatessen`. All are natural in modern Greek travel writing and were left alone.
- **Kickers:** consistent and correct in every language.
  - el: `Άρθρα · Σύρος και διακοπές δίπλα στη θάλασσα`
  - fr: `Articles · Syros et séjours en bord de mer`
  - de: `Artikel · Syros & Urlaub am Meer`
  - it: `Articoli · Syros e soggiorni al mare`
  - he: `מאמרים · סירוס ולינה ליד הים`
- **Place-name consistency:** four inconsistencies found and fixed (see below).

## Verdict per language

| Lang | Verdict | Notes |
|---|---|---|
| el | **Good** (publishable) | Natural travel-guide Greek, with good use of "βίλα", "μελτέμι" and "νησί-πρωτεύουσα". Fixed the Ντελφίνι/Δελφίνι inconsistency, one ungrammatical opening, and a few calques. |
| fr | **Very good** | Clean register and correct typography, including the NBSP before `:` and `;`. Fixed a missing-object calque ("Nous accueillons dans une maison"), `meltem`/`meltemi` inconsistency, and a few awkward phrases. |
| de | **Very good** | Natural Sie-form tone. Fixed one calque ("Strandurlauber der ersten Stunde"), a garbled sentence about Mykonos, "ehrliche Logistik" in a title, and a clumsy "Gastgeber eines Hauses". |
| it | **Very good** | Fluent voi-form. Fixed a "Ospitiamo in una casa" calque, "il tempo in parallelo è il vero prodotto", a "trasforma … in una settimana flessibile" calque, the title "logistica sincera", and apostrophe and `ed` typography. |
| he | **Good** | Natural overall. Fixed the ארמופוליס/ארמופולי inconsistency (spelled two ways) and several literal phrases ("דברים לעשות", "זמן מקביל הוא המוצר", "עובד" meaning "works"). |

## Fixes applied (slug · lang · what)

46 fields were edited across 12 slugs. 60 individual replacements were logged, because some were multi-occurrence regexes. HTML tag structure is unchanged: the tag sequence in every body is identical to before, apart from the alt text of one image.

### el
- `multi-gen-group-villa-syros` · body: "Μια διακοπές … ακούγονται" → "Οι διακοπές …" (grammatical agreement).
- `multi-gen-group-villa-syros` · title: "ειλικρινής οργάνωση" (calque of "honest logistics") → "οργάνωση χωρίς υπερβολές".
- `pet-friendly-syros-villa-stay` · body: "Να πώς πάνε ειλικρινά τα πράγματα" → "Να πώς έχουν πραγματικά τα πράγματα".
- `pet-friendly-syros-villa-stay` · body: "μέρος της αγάπης για τα ταξίδια με κατοικίδια" → "μέρος του ταξιδιού με κατοικίδιο".
- `getting-around-syros-car-rental-bus` · body: "με σκοπιμότητα" → "σκόπιμα".
- `day-trips-from-syros-tinos-mykonos` · body: "το ίδιο site" → "η ίδια ιστοσελίδα".
- `day-trips…`, `pet-friendly…`, `packing-meltemi…`, `grocery-self-catering…` (title, description, body and keywords), `winter-year-round…` · "Ντελφίνι" → "Δελφίνι" (15 occurrences). This matches the standard spelling used in the rest of the site and the other 30 occurrences.

### fr
- `where-to-stay-syros-areas-compared` · body: "Nous accueillons dans une maison" → "Nous accueillons nos hôtes dans une maison".
- `where-to-stay-syros-areas-compared` · body: "plages de Syros Pavillon bleu" → "plages de Syros labellisées Pavillon bleu".
- `grocery-self-catering-delfini-kini` · body: "Faites le ménage de la vaisselle" → "Faites la vaisselle".
- `packing-meltemi-wind-guide-syros` · body: "c'est aussi la météo ; autant que votre valise … l'acceptent" → "c'est aussi composer avec la météo : mieux vaut que votre valise et votre programme s'y adaptent sans drame". NBSPs were kept.
- `kini-restaurants-sunset-dining` · body: "où vous trouver à la fin d'une journée" → "où il faut être à la fin d'une journée".
- `where-to-stay…`, `seven-day…`, `kini-restaurants…`, `syros-in-may-june…`, `things-to-do…` and `day-trips…` (body) · "meltemi" → "meltem", the French form already used in the titles and the packing article (6 text occurrences).
- One regex pass also hit an internal link slug (`packing-meltemi-wind-guide-syros`) in `day-trips…`/fr. I caught this during the tag-diff check and restored the href.

### de
- `where-to-stay-syros-areas-compared` · body: "Kein Ort für Strandurlauber der ersten Stunde." → "Keine Basis für alle, denen der Strand an erster Stelle steht."
- `where-to-stay-syros-areas-compared` · body: "Wir sind Gastgeber eines Hauses, etwa zehn Gehminuten …" → "Wir vermieten ein Haus, etwa zehn Gehminuten …".
- `day-trips-from-syros-tinos-mykonos` · body: "mag oft einen Tag in Mykonos bei Tageslicht, schauen und wieder fahren." → "… einen Tag auf Mykonos: bei Tageslicht ankommen, schauen, wieder zurückfahren." (This fixes the island preposition and the broken syntax.)
- `multi-gen-group-villa-syros` · title: "ehrliche Logistik" → "Logistik ohne Schönfärberei".

### it
- `where-to-stay-syros-areas-compared` and `syros-in-may-june-september` · body: "Ospitiamo in una casa" → "Accogliamo gli ospiti in una casa".
- `getting-around-syros-car-rental-bus` · body: "un'auto trasforma una bella settimana in una settimana flessibile" → "un'auto rende molto più flessibile una bella settimana".
- `multi-gen-group-villa-syros` · body: "Il tempo in parallelo è il vero prodotto." → "Stare insieme, ma ciascuno con i propri tempi, è il vero segreto."
- `multi-gen-group-villa-syros` · body: "Dite se qualcuno ha bisogno" → "Segnalateci se qualcuno ha bisogno".
- `multi-gen-group-villa-syros` · title: "logistica sincera" → "logistica senza giri di parole".
- `syros-in-may-june-september` · body: "e Ermoupoli" → "ed Ermoupoli", to match the title of `ano-syros-…`.
- Straight `'` → typographic `’` in text nodes (not in HTML attributes) for `day-trips`, `pet-friendly`, `packing-meltemi`, `grocery`, `winter-year-round` and `multi-gen`. In `winter-year-round` this covers title, description, body and keywords. The other Italian articles already used `’`.

### he
- `ארמופוליס` → `ארמופולי` in `day-trips`, `pet-friendly`, `packing-meltemi` and `grocery` (description, body, hero caption and an image alt). The Hebrew name was spelled two ways, and `ארמופולי` is used in 76 other places.
- `multi-gen-group-villa-syros` · body: "זמן מקביל הוא המוצר." → "זמן מקביל, כל אחד בפינתו, הוא העיקר."
- `multi-gen-group-villa-syros` · body: link text "יום ארמופולי וחוף שלנו מראה דרך אחת לשלב את הקצב" → "המסלול שלנו ליום בארמופולי ובחוף מראה דרך אחת לחלק את הזמן". The `href` is unchanged.
- `multi-gen-group-villa-syros` · title: "לוגיסטיקה כנה" → "לוגיסטיקה בלי קישוטים".
- `grocery-self-catering-delfini-kini` · body: "וחלקם קצרים יותר בימי ראשון" (missing noun) → "וחלקם פועלים שעות מצומצמות בימי ראשון".
- `things-to-do-on-syros` · description: "לדברים לעשות" → "למה שאפשר לעשות".
- `things-to-do-on-syros` · body: "הדברים הכי שווים לעשות" → "הדברים שהכי כדאי לעשות".
- `things-to-do-on-syros` · body: "הבריחות הקרובות" → "יעדי הבריחה הקרובים".
- `syros-in-may-june-september` · description: "חיי המעבורות" → "מעבורות".
- `packing-meltemi-wind-guide-syros` · body: "הרחובות של ארמופוליס עובדים גם כשהחופים לא" → "…נעימים…" ("עובדים" was a calque of "work").
- `winter-year-round-syros` · title: "למה האי הבירה עובד גם מחוץ לקיץ" → "למה אי הבירה מתאים גם מחוץ לקיץ".

## Remaining issues (not changed, low severity)

1. **Greek register.** Some articles use informal singular (σύ: where-to-stay, getting-around, things-to-do, multi-gen) and others formal plural (pet-friendly, day-trips, grocery). Each article is consistent internally, but the site is not consistent across articles. Pick one register and normalise in a later pass.
2. **Hebrew.** `Visit Greece` is treated inconsistently as plural (מדגישים, מתארים) and singular (מתארת, מציגה). Latin-brand prefixes mix `־` (maqaf) and `-` (e.g. `ו־Visit Greece` vs `ש-Visit Greece`, `ל-6`). In `winter-year-round`, `To Karavaki` stays in Latin script with a gloss. Acceptable, but a Greek-script or Hebrew transliteration would be more consistent.
3. **German.** "Strand Delfini" is used throughout; "Delfini-Strand" is arguably more idiomatic but not wrong. The title "Syros Sehenswürdigkeiten: …" is SEO-style rather than conversational prose, so consider "Was man auf Syros unternehmen kann: …". "Auf der Streckenseite von Ferryhopper" is slightly stiff.
4. **French.** The recurring "en toute franchise" in the multi-gen title is fine. "tournée de courses" is slightly idiomatic and could be "tournée des commerces" if a native reader prefers it.
5. **Internal links.** Links in the el/fr/he bodies point to `/en/Articles/...`. In de/it, about 29 of 70 links are already localized (`/de/…`, `/it/…`). If the HTML builder doesn't rewrite these, the el/fr/he pages will send readers to English articles. This is a build or structure question, so I did not change it.
6. **Coverage.** Bodies for the remaining articles in each language were not fully read. They were covered only by the automated checks (HTML, English leftovers, place-name variants) and by metadata review. Based on consistent quality in the sampled ones, I'd expect no major problems.

## Counts

- Fields modified: 46 across 12 slugs. 60 logged replacements.
- el 14, fr 11, de 4, it 16, he 15 logged replacements.
- `articles.json` was left valid and re-serialised in the original format (indent 2, UTF-8, trailing newline). Only entries in the 12 listed slugs changed. HTML was not rebuilt.
