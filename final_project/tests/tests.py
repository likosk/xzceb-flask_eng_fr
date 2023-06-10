import unittest
from translator import english_to_french, french_to_english

def test_englist_to_french_translation(self):
    self.assertEqual(english_to_french("hello"), "bonjour")
    self.assertEqual(english_to_french("world"), "monde")
self.assertNotEqual(english_to_french('hello'), 'hello')

def test_french_to_english_translation(self):
    self.assertEqual(french_to_english("bonjour"), "hello")
    self.assertEqual(french_to_english("monde"), "world")
self.assertNotEqual(french_to_english('bonjour'), 'bonjour')

if __name__ == '__main__':
    unittest.main()