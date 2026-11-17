import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ContactDestinationContract(unittest.TestCase):
    def test_actual_java_allowlist_accepts_bundle_not_arbitrary_hosts(self):
        source = (ROOT / 'app/src/main/java/com/saebm/btcnfccustomer/MainActivity.java').read_text()
        guard = source.split('private void openContact(String url)', 1)[1].split('consent =', 1)[0]
        encoded = re.search(r'url\.matches\("([^"\n]+)"\)', guard).group(1)
        pattern = encoded.replace('\\\\', '\\')
        links = json.loads((ROOT / 'app/src/main/assets/public/contact-links.json').read_text())
        for url in links.values():
            self.assertIsNotNone(re.fullmatch(pattern, url), url)
        for url in ['https://evil.example/contact', 'https://btc.saeb.id.ir.evil.example/', 'https://btc.saeb.id.ir/?uid=123', 'https://bitposta.com/contact']:
            self.assertIsNone(re.fullmatch(pattern, url), url)
        # The deleted market instrumentation used to repeat the allowlist proof; the
        # real contract is asserted above. What remains to pin is that showContact
        # renders one control per bundled link, each carrying a contact-<key> tag.
        show_contact = source.split('private void showContact()', 1)[1].split('private void openContact', 1)[0]
        self.assertIn('contact-links.json', show_contact)
        self.assertIn('contact.setTag("contact-" + keys[i])', show_contact)
        keys = set(json.loads((ROOT / 'app/src/main/assets/public/contact-links.json').read_text()))
        self.assertEqual(keys, {'website', 'form', 'email', 'telegram', 'instagram', 'x'})

if __name__ == '__main__':
    unittest.main()
