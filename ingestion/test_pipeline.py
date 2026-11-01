import asyncio
import io
import json
import tempfile
import unittest
from pathlib import Path
from .ingredients import parse_ingredient, density_conversion
from .model import RecipeJSONLD, base_yield, from_schema, validate
from .pipeline import Store, Fetcher, json_array, wiki_rows

class ParsingTests(unittest.TestCase):
    def test_fractions_and_prep(self):
        c=parse_ingredient('2 1/2 tablespoons unsalted butter, cubed and chilled')
        self.assertEqual((c['qty'],c['unit'],c['name'],c['preparation']),(2.5,'tbsp','unsalted butter','cubed and chilled'))
        self.assertAlmostEqual(parse_ingredient('⅓ cup flour')['qty'],1/3)
        self.assertEqual(parse_ingredient('1½ cups flour')['qty'],1.5)
    def test_package_and_ambiguous(self):
        c=parse_ingredient('1 (14-ounce) can San Marzano tomatoes')
        self.assertEqual((c['qty'],c['unit'],c['package']),(1,'can','14-ounce'))
        for text in ['flour','1/0 cup flour','1–2 cups flour','0 g flour']:
            self.assertIsNone(parse_ingredient(text)['qty'])
        self.assertEqual(parse_ingredient('salt, to taste')['quantity_status'],'to_taste')
    def test_density_is_explicit(self):
        c=parse_ingredient('2 cups all-purpose flour')
        self.assertIsNone(density_conversion(c))
        self.assertEqual(density_conversion(c,'US customary')['qty'],240)
        self.assertIsNone(density_conversion(parse_ingredient('1 cup milk'),'US customary'))
        self.assertIsNone(density_conversion(parse_ingredient('1 cup flour, sifted'),'US customary'))
    def test_yield_not_guessed(self):
        self.assertIsNone(base_yield('Serves 4 to 6')['servings'])
        self.assertIsNone(base_yield('24 cookies')['servings'])
        self.assertEqual(base_yield('Serves 4')['servings'],4)
    def test_jsonld_graph_and_sections(self):
        data={'@graph':[{'@type':['Recipe'],'name':'Example','recipeYield':'4 servings',
              'recipeIngredient':['2 cups flour'],'recipeInstructions':[{'@type':'HowToSection','itemListElement':[{'text':'Mix carefully.'},{'text':'Follow the source cooking instructions.'}]}]}]}
        p=RecipeJSONLD();p.feed('<script type="application/ld+json">'+json.dumps(data)+'</script>')
        r=from_schema(next(p.recipes()),'https://example.com/recipe','Example')
        self.assertIn('2. Follow',r['technique']);self.assertFalse(r['cookable']);self.assertEqual(validate(r),[])
        r['cookable']=True;self.assertIn('false_cookable_claim',validate(r))
    def test_stream_and_resume(self):
        self.assertEqual(list(json_array(io.StringIO('[{"a":1},{"b":"é"}]'))),[{'a':1},{'b':'é'}])
        with self.assertRaises(ValueError):list(json_array(io.StringIO('[{"a":1}')))
        with tempfile.TemporaryDirectory() as d:
            s=Store(Path(d)/'seen.db');s.mark('https://example.com/a','processed');s.close()
            s=Store(Path(d)/'seen.db');self.assertTrue(s.seen('https://example.com/a'));s.mark('https://example.com/b','failed');self.assertFalse(s.seen('https://example.com/b'));s.close()
    def test_wiki_template_not_invented(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'wiki.xml';p.write_text('<mediawiki><page><title>Cookbook:Example</title><revision><text>== Ingredients ==\n* {{quantity|2|cup}} flour\n== Procedure ==\n# Mix.</text></revision></page></mediawiki>')
            r=next(wiki_rows(p));self.assertFalse(r['cookable']);self.assertIn('wikitext_requires_review',r['review']['issues'])
    def test_403_stops_host(self):
        with tempfile.TemporaryDirectory() as d:
            s=Store(Path(d)/'db');f=Fetcher(['example.com'],s);calls=[]
            def raw(url):
                calls.append(url)
                return (200,{},b'User-agent: *\nAllow: /',url) if url.endswith('robots.txt') else (403,{},b'',url)
            f.raw=raw
            async def run():
                with self.assertRaises(PermissionError):await f.get('https://example.com/recipe')
                with self.assertRaises(ValueError):await f.get('https://example.com/other')
            asyncio.run(run());self.assertEqual(len(calls),2);s.close()

if __name__=='__main__':unittest.main()
