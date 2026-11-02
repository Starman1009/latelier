# -*- coding: utf-8 -*-
"""
Generator for all 105+ Master Recipes for L'Atelier Culinary Platform.
Synthesizes the complete, authentic culinary library with all 20 required fields.
"""

import json
import os

from catalog_french import FRENCH_RECIPES
from catalog_italian import ITALIAN_RECIPES
from catalog_asian import ASIAN_RECIPES
from catalog_world_traditions import WORLD_RECIPES
from compile_master_library import ADDITIONAL_RECIPES
from catalog_data_definitions import RAW_RECIPES_DATA

ALL_RECIPES = list(FRENCH_RECIPES) + list(ITALIAN_RECIPES) + list(ASIAN_RECIPES) + list(WORLD_RECIPES) + list(ADDITIONAL_RECIPES) + list(RAW_RECIPES_DATA)

print(f"Base loaded: {len(ALL_RECIPES)} fully handcrafted recipes.")
