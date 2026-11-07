#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from i18n import seaside, syros_vs, best_time, greece_str  # noqa: E402

out = {
    "seaside-accommodation-syros-delfini-beach": seaside.entries(),
    "syros-vs-santorini-mykonos-calmer-cyclades": syros_vs.entries(),
    "best-time-to-visit-syros-seaside-holiday": best_time.entries(),
    "greece-short-term-rentals-2026-what-travellers-want": greece_str.entries(),
}

dest = ROOT.parent / "Articles" / "translations-4-articles.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
json.dump(out, sys.stdout, ensure_ascii=False)
