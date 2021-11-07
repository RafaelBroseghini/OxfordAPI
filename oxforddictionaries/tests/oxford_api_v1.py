import unittest

from credentials import APPLICATION_ID, APPLICATION_KEY
from oxford_api_v1 import OxfordApiV1


class OxfordApiV1Tests(unittest.TestCase):
    def setUp(self):
        self.oxford = OxfordApiV1(APPLICATION_ID, APPLICATION_KEY)

    def test_synonyms(self):
        self.assertEqual(self.oxford.get_synonyms("play").status_code, 200)

    def test_antonyms(self):
        self.assertEqual(self.oxford.get_antonyms("play").status_code, 200)

    def test_antonyms(self):
        self.assertEqual(self.oxford.translate("play").status_code, 200)

    def test_antonyms(self):
        self.assertEqual(self.oxford.get_info_about_word("play").status_code, 200)

    def test_antonyms(self):
        self.assertEqual(self.oxford.use_in_sentence("play").status_code, 200)


if __name__ == '__main__':
    unittest.main()
