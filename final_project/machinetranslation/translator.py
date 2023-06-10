import json
import os
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    translate english to french
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

#print(english_to_french("hello"))

def french_to_english(french_text):
    """
    translate french to english
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text

#print(french_to_english("bonjour"))