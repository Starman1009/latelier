if __name__ == "__main__":
    raise SystemExit("Legacy catalog writer disabled: use python -m ingestion.pipeline --help. Original algorithms retained for reference; they must not overwrite reviewed data.")

import json
import os
from datetime import datetime, timedelta

RECIPES_FILE = "recipes.json"
OUTPUT_MD = "Master_Brigade_Plan.md"

STATION_RULES = {
    "opener": ("Garde Manger", "Cold Larder, Crudos, Caviar & Vinaigrettes"),
    "mid": ("Poissonnier / Entremetier", "Seafood Poaching, Searing & Silky Purées"),
    "climax": ("Grillardin / Saucier", "High-Heat Maillard Proteins & Demi-Glace/Gastriques"),
    "predessert": ("Pâtissier", "Sub-Zero Granitas, Sorbets & Hydrosols"),
    "dessert": ("Pâtissier", "Custards, Ganaches, Soufflés & Crisp Sablés")
}

def compile_brigade_dossier(service_time_str="19:30"):
    if not os.path.exists(RECIPES_FILE):
        print(f"[!] {RECIPES_FILE} not found.")
        return

    with open(RECIPES_FILE, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    # Pick a balanced 5-course arc
    slots = ["opener", "mid", "climax", "predessert", "dessert"]
    menu = []
    for s in slots:
        matches = [r for r in catalog if r.get("slot") == s]
        if matches:
            menu.append(matches[0])

    target_dt = datetime.strptime(service_time_str, "%H:%M")

    lines = [
        "# L'ATELIER PROFESSIONAL MISE EN PLACE & BRIGADE DOSSIER",
        f"**Target Service Pickup (T-0):** {service_time_str} | **HACCP Cold Zone:** <= 4.0°C | **HACCP Hot Zone:** >= 57.2°C",
        "---",
        "## I. MULTI-RECIPE CONSOLIDATED SHOPPING & PREP LIST"
    ]

    for c in menu:
        lines.append(f"\n### {c['dish']} ({c['slot'].upper()})")
        for comp in c.get("components", []):
            lines.append(f"- [ ] **{comp['name']}**: {comp['qty']} {comp['unit']} *(Dept: {comp.get('dept', 'pantry')})*")

    lines.append("\n---\n## II. BACKWARD-SCHEDULED CRITICAL PATH TIMELINE")
    offsets = [-180, -120, -75, -30, -10]

    for idx, c in enumerate(menu):
        t_start = (target_dt + timedelta(minutes=offsets[idx])).strftime("%I:%M %p")
        st_name, st_desc = STATION_RULES.get(c.get("slot", "mid"), ("Entremetier", "General Station"))
        lines.append(f"\n### {t_start} (T{offsets[idx]}m) — Course 0{idx+1}: {c['dish']}")
        lines.append(f"- **Assigned Brigade Station:** `{st_name}` ({st_desc})")
        lines.append(f"- **Execution Protocol:** {c.get('technique')}")
        lines.append(f"- **Plating Blueprint:** {c.get('plating')}")
        lines.append(f"- **HACCP & Quality Storage:** Hold prepped components at <=4.0°C; hot-hold emulsions at 60°C in bain-marie.")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("=================================================================")
    print(f"  [+] BRIGADE MISE EN PLACE DOSSIER GENERATED: {OUTPUT_MD}")
    print(f"  [+] Backward-scheduled from T-0 ({service_time_str}) across {len(menu)} courses.")
    print("=================================================================")

if __name__ == "__main__":
    compile_brigade_dossier("19:30")