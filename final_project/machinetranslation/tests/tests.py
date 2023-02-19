import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase): 
    def test_french_to_english(self): 
        english_text1 = french_to_english('0')['translations'][0]['translation']
        self.assertEqual(english_text1, '0') #Test for null input for
        self.assertNotEqual(english_text1, '1') #Test for != null input for
        english_text2 = french_to_english('Bonjour')['translations'][0]['translation']
        self.assertEqual(english_text2, 'Hello')  #Test for =
        self.assertNotEqual(english_text2, 'Hi')  #Test for !=
    def test_english_to_french(self):
        french_text1 = english_to_french('0')['translations'][0]['translation']
        self.assertEqual(french_text1, '0') #Test for null inpu$
        self.assertNotEqual(french_text1, '1') #Test for != null inpu$
        french_text1  = english_to_french('Hello')['translations'][0]['translation']
        self.assertEqual(french_text1 , 'Bonjour')  #Test fo =
        self.assertNotEqual(french_text1 , 'Bon')  #Test fo !=
     
if __name__ == '__main__':
     unittest.main()