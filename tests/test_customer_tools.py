import pathlib
import unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
class CustomerTools(unittest.TestCase):
 def test_native_tools_have_explicit_fetch_and_lifecycle_fence(self):
  source=(ROOT/'app/src/main/java/com/saebm/btcnfccustomer/MainActivity.java').read_text()
  # The costs feature is gone entirely: no local pricing, no market fetch, no screen.
  for token in ['this::showContact', 'contact-links.json', 'کلید خصوصی']:
   self.assertIn(token,source)
  for removed in ['fetchMarket', 'marketClient', 'marketGate', '/api/market', 'showCosts',
                  'home-costs', 'contact-costs', '"costs"']:
   self.assertNotIn(removed,source)
  self.assertNotIn('WebView',source)
