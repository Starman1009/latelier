"""Conservative deterministic parsing. Original text is always retained."""
import math
import re
from fractions import Fraction

FRACTIONS = dict(zip('½¼¾⅓⅔⅛⅜⅝⅞', ['1/2','1/4','3/4','1/3','2/3','1/8','3/8','5/8','7/8']))
UNITS = {}
for canonical, aliases in {
    'cup':'cup cups', 'tbsp':'tbsp tablespoon tablespoons tbs tblsp',
    'tsp':'tsp teaspoon teaspoons', 'oz':'oz ounce ounces', 'lb':'lb lbs pound pounds',
    'g':'g gram grams', 'kg':'kg kilogram kilograms', 'ml':'ml milliliter milliliters millilitre millilitres',
    'l':'l liter liters litre litres', 'clove':'clove cloves', 'pinch':'pinch pinches',
    'can':'can cans tin tins', 'bunch':'bunch bunches', 'piece':'piece pieces pcs',
    'stick':'stick sticks', 'slice':'slice slices'
}.items():
    UNITS.update({alias:canonical for alias in aliases.split()})

NUMBER = r'(?:\d+\s+\d+/\d+|\d+/\d+|\d+(?:\.\d+)?)'

def quantity(value):
    try:
        result = sum((Fraction(x) for x in value.split()), Fraction())
        return float(result) if result > 0 else None
    except (ValueError, ZeroDivisionError):
        return None

def parse_ingredient(line):
    raw = str(line).strip()
    text = raw
    for symbol, replacement in FRACTIONS.items():
        text = text.replace(symbol, ' '+replacement)
    text = re.sub(r'\s+', ' ', text).strip()
    result = dict(name=raw, qty=None, unit='unspecified', original_measure=raw,
                  dept='pantry', preparation='', quantity_status='unspecified', package=None)
    if not text:
        return result
    if re.search(r'\b(to taste|as needed)\b', text, re.I):
        result.update(name=re.sub(r'[,;]?\s*\b(to taste|as needed)\b', '', text, flags=re.I).strip(),
                      unit='to_taste', quantity_status='to_taste')
        return result
    # Ranges are retained; selecting one endpoint would invent a quantity.
    if re.match(NUMBER+r'\s*(?:[-–—]|to)\s*'+NUMBER, text):
        result['quantity_status'] = 'range'
        return result
    match = re.match('('+NUMBER+r')\s*(.*)$', text)
    if not match:
        return result
    qty, rest = quantity(match[1]), match[2].strip()
    if qty is None or not rest:
        return result
    # Count packages separately from their net weights: 1 (14-ounce) can.
    package = re.match(r'^\(([^)]+)\)\s*(.*)$', rest)
    if package:
        result['package'] = package[1]
        rest = package[2]
    unit_match = re.match(r'^([A-Za-z]+)\.?\s*(.*)$', rest)
    unit = UNITS.get(unit_match[1].lower()) if unit_match else None
    if unit:
        rest = unit_match[2]
    else:
        unit = 'piece'
    parts = re.split(r',\s*', rest, maxsplit=1)
    name = parts[0].strip()
    prep = parts[1] if len(parts)>1 else ''
    leading = re.match(r'^(finely chopped|roughly chopped|chopped|cubed|sifted|drained|peeled|minced)\s+(.+)$', name, re.I)
    if leading:
        prep = ', '.join(x for x in [leading[1], prep] if x)
        name = leading[2]
    if not name:
        return result
    result.update(name=name, qty=qty, unit=unit, preparation=prep, quantity_status='specified')
    return result

# These are explicit user-requested reference factors, not universal densities.
# Conversion is opt-in, requires an exact ingredient + preparation match and a
# US customary measure convention. It never replaces original quantities.
DENSITIES = {
    ('all-purpose flour','cup'):120, ('bread flour','cup'):120,
    ('granulated white sugar','cup'):200, ('packed brown sugar','cup'):220,
    ('butter','cup'):227, ('butter','stick'):113.4, ('butter','tbsp'):14.2,
    ('honey','cup'):340, ('molasses','cup'):340,
    ('olive oil','cup'):216, ('vegetable oil','cup'):216,
    ('diamond crystal kosher salt','tbsp'):8.5, ('fine table salt','tbsp'):17,
}

def density_conversion(component, convention=None):
    if convention != 'US customary' or component.get('preparation') or component.get('package'):
        return None
    key = (component['name'].casefold(), component['unit'])
    if key in (('heavy cream','cup'),('whole milk','cup')) and isinstance(component.get('qty'),(int,float)) and component['qty']>0:
        return {'qty':round(component['qty']*240,6),'unit':'ml','approximate':True,
                'basis':'User-specified 240 ml cup convention; no mass conversion',
                'convention':convention,'original_measure':component['original_measure']}
    factor = DENSITIES.get(key)
    qty = component.get('qty')
    if factor is None or not isinstance(qty, (int,float)) or not math.isfinite(qty) or qty<=0:
        return None
    return {'qty':round(qty*factor,6), 'unit':'g', 'approximate':True,
            'basis':'User-specified reference table; verify against the recipe publisher',
            'convention':convention, 'original_measure':component['original_measure']}
