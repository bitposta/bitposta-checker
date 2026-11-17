"""Source contracts pinning that the app has no costs section at all.

The owner removed the costs feature from the app: no local pricing, no fetch of
the site's /api/market, and no costs screen or entry point. The site is the only
place costs are shown. These checks keep that removal from being quietly undone:

* the pricing/fetch classes must not come back into ``core`` or ``MainActivity``;
* no costs entry point, screen, allowlist entry or bundled page may return;
* the remaining offline pages keep working.
"""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CORE = ROOT / 'core/src/main/java/com/saebm/btcnfccustomer/core'
APP = ROOT / 'app/src/main/java/com/saebm/btcnfccustomer'
ASSETS = ROOT / 'app/src/main/assets/public'


class AppHasNoCostsSection(unittest.TestCase):
    def test_no_pricing_classes_remain_in_core(self):
        for name in ('QuoteCalculator.java', 'MarketResponse.java', 'MarketClient.java'):
            with self.subTest(name=name):
                self.assertFalse((CORE / name).exists(),
                                 f'{name} must not exist: the app has no cost model')

    def test_the_app_never_prices_or_fetches_a_market_table(self):
        activity = (APP / 'MainActivity.java').read_text(encoding='utf-8')
        for token in ('/api/market', 'MarketResponse', 'MarketClient', 'QuoteCalculator',
                      'convert_sats', 'transfer_sats', 'satoshi_toman', 'network_fee_rate',
                      'marketClient', 'marketGate', 'fetchMarket'):
            with self.subTest(token=token):
                self.assertNotIn(token, activity, f'{token} means the app prices locally again')

    def test_the_costs_screen_and_its_entry_points_are_gone(self):
        activity = (APP / 'MainActivity.java').read_text(encoding='utf-8')
        for token in ('showCosts', 'home-costs', 'contact-costs', 'quote-amount',
                      'open-costs-site'):
            with self.subTest(token=token):
                self.assertNotIn(token, activity, f'{token} must not return')
        # The removed controls' Farsi label must not linger either. Written with an
        # escaped escape so this file cannot match itself.
        self.assertNotIn('\u0642\u06cc\u0645\u062a \u0648 \u0647\u0632\u06cc\u0646\u0647\u200c\u0647\u0627',
                         activity)

    def test_costs_is_not_an_offline_public_page(self):
        activity = (APP / 'MainActivity.java').read_text(encoding='utf-8')
        declaration = re.search(r'PUBLIC_PAGES = \{([^}]*)\}', activity)
        self.assertIsNotNone(declaration, 'PUBLIC_PAGES allowlist declaration missing')
        assert declaration is not None
        self.assertNotIn('"costs"', declaration.group(1))
        self.assertFalse((ASSETS / 'costs.txt').exists(),
                         'the bundled costs page must not come back')

    def test_the_remaining_offline_pages_still_work(self):
        for page in ('guide', 'terms', 'payment', 'security'):
            with self.subTest(page=page):
                self.assertTrue((ASSETS / f'{page}.txt').is_file())
        self.assertTrue((ASSETS / 'manifest.json').is_file())
        self.assertNotIn('costs', (ASSETS / 'manifest.json').read_text(encoding='utf-8'))

    def test_the_payment_page_no_longer_redirects_to_costs(self):
        activity = (APP / 'MainActivity.java').read_text(encoding='utf-8')
        body = activity.split('private void showPublic')[1].split('private void openPublic')[0]
        self.assertIn('openPublic(page)', body)
        self.assertNotIn('"costs"', body)


if __name__ == '__main__':
    unittest.main()
