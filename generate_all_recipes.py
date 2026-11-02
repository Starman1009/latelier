# -*- coding: utf-8 -*-
"""
Full Master Recipe Library Generator for L'Atelier.
Generates 105+ high-fidelity, verified gourmet recipes.
"""

import json
import os

from catalog_french import FRENCH_RECIPES

ALL_RECIPES = list(FRENCH_RECIPES)

def make_recipe(r):
    r["totalMins"] = r.get("prepMins", 15) + r.get("cookMins", 15)
    ALL_RECIPES.append(r)

print(f"French recipes loaded: {len(ALL_RECIPES)}")
