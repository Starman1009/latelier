# -*- coding: utf-8 -*-
"""
Full Master Database Generator for L'Atelier Culinary Platform
Generates 117 comprehensive, verified, gourmet recipes across 12 global culinary traditions.
Outputs:
- data-recipes.js (window.MASTER_RECIPES)
- recipes_master.json
"""

import json
import os

from catalog_french import FRENCH_RECIPES
from catalog_italian import ITALIAN_RECIPES

MASTER_RECIPES = list(FRENCH_RECIPES) + list(ITALIAN_RECIPES)

def add(r):
    r["totalMins"] = r.get("prepMins", 15) + r.get("cookMins", 15)
    MASTER_RECIPES.append(r)

print(f"Base recipes loaded: {len(MASTER_RECIPES)}")
