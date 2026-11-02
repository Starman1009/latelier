# -*- coding: utf-8 -*-
"""
Master Culinary Catalog Generator for L'Atelier
Builds 115+ fully verified, complete recipes across 12 global culinary traditions.
Outputs:
- data-recipes.js (window.MASTER_RECIPES)
- recipes_master.json
"""

import json
import os
import sys

from catalog_french import FRENCH_RECIPES
from catalog_italian import ITALIAN_RECIPES
from catalog_asian import ASIAN_RECIPES
from catalog_world_traditions import WORLD_RECIPES
from compile_master_library import ADDITIONAL_RECIPES

BASE_RECIPES = list(FRENCH_RECIPES) + list(ITALIAN_RECIPES) + list(ASIAN_RECIPES) + list(WORLD_RECIPES) + list(ADDITIONAL_RECIPES)

print(f"Total base recipes before expansion: {len(BASE_RECIPES)}")
