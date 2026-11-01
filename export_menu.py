import json
import os
import random
import sys

RECIPES_FILE = "recipes.json"

def load_data():
    if not os.path.exists(RECIPES_FILE):
        print(f"[!] {RECIPES_FILE} not found.")
        sys.exit(1)
    with open(RECIPES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_export_menu(courses_count=5, covers=4, output_filename="Tasting_Menu_Prep_Sheet.txt"):
    data = load_data()
    slots = ["opener", "climax", "dessert"] if courses_count == 3 else ["opener", "mid", "climax", "predessert", "dessert"]
    
    selected_menu = []
    scale = covers / 2.0

    for slot in slots:
        candidates = [r for r in data if r.get("slot") == slot]
        if not candidates:
            candidates = data
        pick = random.choice(candidates)
        selected_menu.append(pick)

    # Build the document
    lines = []
    lines.append("=" * 65)
    lines.append(f"             L'ATELIER DEGUSTATION PREP SHEET")
    lines.append(f"                  COVERS: {covers} | COURSES: {courses_count}")
    lines.append("=" * 65)
    lines.append("")

    for i, c in enumerate(selected_menu, 1):
        lines.append(f"COURSE 0{i}: {c['dish'].upper()}")
        lines.append(f"SLOT: {c['slot'].upper()} | ORIGIN: {c['restaurant']} ({c['chef']})")
        lines.append(f"SENSORY ROLE: {c['sensoryRole']}")
        lines.append("-" * 65)
        lines.append("SCALED MISE-EN-PLACE:")
        for comp in c.get("components", []):
            scaled_qty = round(comp.get("qty", 50) * scale, 1)
            lines.append(f"  [ ] {comp['name']:<35} {scaled_qty:>6} {comp.get('unit', 'g')}")
        lines.append("")
        lines.append("TECHNICAL EXECUTION:")
        lines.append(f"  {c.get('technique')}")
        lines.append("")
        lines.append("SOMMELIER ACCORD:")
        lines.append(f"  Wine:       {c.get('pairing', {}).get('wine', 'N/A')}")
        lines.append(f"  Zero-Proof: {c.get('pairing', {}).get('zeroProof', 'N/A')}")
        lines.append("=" * 65)
        lines.append("")

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[+] Successfully exported {courses_count}-course prep sheet for {covers} covers!")
    print(f"[+] Saved file: {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    generate_export_menu(courses_count=5, covers=4)