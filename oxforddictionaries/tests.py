import unittest
from words import OxfordDictionaries

class API_Tester(unittest.TestCase):
    def setUp(self):
        self.oxford = OxfordDictionaries(app_id, app_key)

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
        
        