import unittest
from translator import english_to_french, french_to_english

class testTranslation(unittest.TestCase):
    def nullCaseEn(self):
        self.assertEqual(english_to_french(''), None)
    
    def translateFr(self):
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')
    
    def nullCaseFr(self):
        self.assertEqual(french_to_english(''), None)
    
    def translateEn(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()