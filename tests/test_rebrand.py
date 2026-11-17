"""Rebrand contract for the customer app: bitposta.com replaces every old domain.

Written before the change so it fails on the pre-rebrand tree. Backward
compatibility is deliberately not required: the legacy hosts leave the
allowlists rather than staying beside the new one.
"""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
CORE = ROOT / "core/src/main/java/com/saebm/btcnfccustomer/core"
APP = ROOT / "app/src/main"
ASSETS = APP / "assets/public"

BRAND = "bitposta.com"
LEGACY = ("btc4.fun", "b.tc4fun.ir", "bitcoin4.fun", "btc4-fun")
PRINTABLE_EMAIL = "09113458375@bitposta.com"

SOURCES = (
    CORE / "RequestPolicy.java",
    CORE / "LookupClient.java",
    CORE / "QrPayload.java",
    APP / "java/com/saebm/btcnfccustomer/MainActivity.java",
    ASSETS / "contact-links.json",
    ASSETS / "guide.txt",
    ASSETS / "security.txt",
)


class CustomerRebrand(unittest.TestCase):
    def test_no_legacy_domain_survives_in_shipped_sources(self):
        for path in SOURCES:
            with self.subTest(path=path.name):
                text = path.read_text()
                for legacy in LEGACY:
                    self.assertNotIn(legacy, text)

    def test_the_new_host_is_the_lookup_and_image_host(self):
        policy = (CORE / "RequestPolicy.java").read_text()
        client = (CORE / "LookupClient.java").read_text()
        self.assertIn(f"https://{BRAND}/api/tags/", policy)
        self.assertIn(f"https://{BRAND}/api/wallets/", policy)
        self.assertIn(f"https://{BRAND}/api/addresses/", policy)
        self.assertIn(f'LOOKUP_PREFIX = "https://{BRAND}/s/"', client)
        self.assertIn(f'IMAGE_HOST = "{BRAND}"', client)
        self.assertIn(f'"https://{BRAND}/"', client)

    def test_qr_allowlist_accepts_only_the_two_owned_hosts(self):
        source = (CORE / "QrPayload.java").read_text()
        self.assertIn(BRAND, source)
        self.assertIn("btc.saeb.id.ir", source)
        for legacy in ("btc4.fun", "b.tc4fun.ir", "bitcoin4.fun"):
            with self.subTest(legacy=legacy):
                self.assertNotIn(legacy, source)

    def test_contact_links_use_the_new_mailbox_and_accounts(self):
        links = (ASSETS / "contact-links.json").read_text()
        self.assertIn(f"mailto:{PRINTABLE_EMAIL}", links)
        self.assertIn("https://t.me/bitposta", links)
        self.assertIn("https://www.instagram.com/bitposta.ir/", links)
        self.assertIn("https://x.com/bitposta", links)

    def test_security_page_lists_only_the_two_owned_domains(self):
        text = (ASSETS / "security.txt").read_text()
        self.assertIn(BRAND, text)
        self.assertIn("btc.saeb.id.ir", text)

    def test_offline_guides_point_at_the_new_lookup_paths(self):
        guide = (ASSETS / "guide.txt").read_text()
        self.assertIn(f"https://{BRAND}/s/SERIAL", guide)
        self.assertIn(f"https://go.{BRAND}/SERIAL", guide)

    def test_application_id_is_unchanged_so_installs_upgrade(self):
        gradle = (ROOT / "app/build.gradle").read_text()
        self.assertIn("com.saebm.btcnfccustomer", gradle)


if __name__ == "__main__":
    unittest.main()
