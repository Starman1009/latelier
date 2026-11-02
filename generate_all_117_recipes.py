# -*- coding: utf-8 -*-
"""
Compiles all 117 Master Recipes for L'Atelier Culinary Platform.
Outputs:
- data-recipes.js
- recipes_master.json
"""

import json
import os
import sys

from catalog_french import FRENCH_RECIPES
from catalog_italian import ITALIAN_RECIPES
from catalog_asian import ASIAN_RECIPES

ALL_MASTER_RECIPES = list(FRENCH_RECIPES) + list(ITALIAN_RECIPES) + list(ASIAN_RECIPES)

print(f"Base imported: {len(ALL_MASTER_RECIPES)} recipes.")
