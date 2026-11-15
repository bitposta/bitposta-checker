"""Owner UX contract: the balance is on top, and an unregistered address is not a dead end."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ACTIVITY = ROOT / "app/src/main/java/com/saebm/btcnfccustomer/MainActivity.java"
LOOKUP = ROOT / "core/src/main/java/com/saebm/btcnfccustomer/core/LookupClient.java"


def method_body(source, name):
    """Extract one method's braces-balanced body, so order/absence checks stay local."""
    start = re.search(r"private (?:static )?\w[\w<>\[\]]* " + re.escape(name) + r"\(", source)
    if start is None:
        start = re.search(r"@Override public \w[\w<>\[\]]* " + re.escape(name) + r"\(", source)
    if start is None:
        raise AssertionError("method not found: " + name)
    opening = source.index("{", start.end() - 1)
    depth = 0
    for index in range(opening, len(source)):
        if source[index] == "{":
            depth += 1
        elif source[index] == "}":
            depth -= 1
            if depth == 0:
                return source[opening + 1:index]
    raise AssertionError("unbalanced method: " + name)


class LookupUxContract(unittest.TestCase):
    def test_balance_is_rendered_before_address_serial_seller_and_warnings(self):
        body = method_body(ACTIVITY.read_text(), "renderLookup")
        order = [
            "موجودی تأییدشده، به ساتوشی",
            "Sats.btc(lookup.balance.confirmedSats)",
            "تغییر موجودی در انتظار تأیید، به ساتوشی",
            "آدرس عمومی کیف پول",
            "شمارهٔ سریال",
            "یادداشت عمومی فروشنده",
            "explorerButtons(lookup.address)",
            "این عدد تضمین نمی‌کند که همهٔ پول همین حالا قابل خرج کردن است.",
        ]
        positions = [body.index(token) for token in order]
        self.assertEqual(positions, sorted(positions),
                         "card order must be balance, pending delta, address, serial, seller, explorers, warnings")
        # The confirmed balance is the very first thing added to the card, so no scrolling is needed.
        self.assertLess(body.index("موجودی تأییدشده، به ساتوشی"), body.index("آدرس عمومی کیف پول"))
        self.assertLess(body.index("Sats.btc(lookup.balance.confirmedSats)"),
                        body.index("تغییر موجودی در انتظار تأیید، به ساتوشی"))

    def test_unregistered_address_offers_three_explorers_instead_of_a_bare_error(self):
        source = ACTIVITY.read_text()
        deliver = method_body(source, "deliverLookup")
        # The 404 branch for an address must build a card, not stop at a status line.
        self.assertIn("renderUnregisteredAddress(lookupValue)", deliver)
        self.assertIn("آدرس عمومی نامعتبر است؛ این آدرس در پایگاه‌داده ما ثبت نشده است.", deliver)
        card = method_body(source, "renderUnregisteredAddress")
        self.assertIn("این آدرس در پایگاه‌داده ما ثبت نشده است", card)
        self.assertIn("explorerButtons(address)", card)
        self.assertIn("BitcoinAddress.isValid(address)", card)
        # This path never shows a balance, and never implies zero.
        self.assertNotIn("confirmedSats", card)
        self.assertNotIn("pendingDeltaSats", card)

    def test_every_explorer_button_is_consent_gated_and_nothing_opens_automatically(self):
        source = ACTIVITY.read_text()
        buttons = method_body(source, "explorerButtons")
        self.assertIn("LookupClient.explorers(address)", buttons)
        self.assertIn("confirmOpen(explorer.url", buttons)
        # The consent dialog is the only way out; no direct intent and no automatic open.
        self.assertNotIn("startActivity", buttons)
        self.assertNotIn("ACTION_VIEW", buttons)
        self.assertNotIn("confirmOpen(", method_body(source, "renderUnregisteredAddress"))

    def test_three_explorer_urls_are_built_locally_in_core(self):
        core = LOOKUP.read_text()
        for url in ("https://mempool.space/address/",
                    "https://blockstream.info/address/",
                    "https://blockchain.com/explorer/addresses/btc/"):
            with self.subTest(url=url):
                self.assertIn(url, core)
        # Built from the validated address only, never from a site-supplied link.
        self.assertIn("BitcoinAddress.isValid(address)", core)
        self.assertIn("public static java.util.List<Explorer> explorers(String address)", core)

    def test_lookup_section_puts_serial_first_and_still_asks_before_sending(self):
        home = method_body(ACTIVITY.read_text(), "showInquiry")
        self.assertLess(home.index('"serial-input"'), home.index('"address-input"'))
        self.assertLess(home.index('"serial-submit"'), home.index('"address-submit"'))
        self.assertIn("submitLookup(true)", home)
        self.assertIn("submitLookup(false)", home)
        # The section only wires buttons: nothing is requested while the screen is built.
        self.assertNotIn("fetchLookup(", home)
        self.assertNotIn("LookupClient.production", home)


if __name__ == "__main__":
    unittest.main()
