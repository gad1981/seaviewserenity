# Sea View Serenity Website

Multilingual static site for [seaviewserenity.gr](https://seaviewserenity.gr) with `/en` style i18n.

## Locales
- `/en/` English
- `/el/` Ελληνικά
- `/fr/` Français
- `/de/` Deutsch
- `/it/` Italiano
- `/he/` עברית (RTL)

Root `/` redirects to `/en/`.

## Pages (per locale)
- Home, The Villa, Book now
- Articles hub + 10 SEO guides (shared media in `/Articles/media/`)

## Rebuild i18n pages

```bash
python3 scripts/build_i18n.py
```

UI strings: `i18n/ui.json`  
Article translations: `i18n/articles.json`

## Local preview

```bash
npx serve .
```

## Deploy

```bash
npx vercel --prod
```
