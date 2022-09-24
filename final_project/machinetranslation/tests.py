import unittest
from translator import english_to_french, french_to_english

class testTranslationEnToFr(unittest.TestCase):
    def nullCaseEn(self):
        self.assertIsNone(english_to_french(''))
    def translateFrGood(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def translateFrBad(self):
        self.assertNotEqual(english_to_french('Hello'), 'voir')

class testTranslationFrToEn(unittest.TestCase):
    def nullCaseFr(self):
        self.assertIsNone(french_to_english(''))
    def translateEnGood(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def translateEnBad(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Good')

if __name__ == "__main__":
    unittest.main()