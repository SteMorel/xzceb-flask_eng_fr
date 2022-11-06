import unittest

import english_to_french,french_to_english 

class TestEnglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("null"),"Null")
    def test2(self): 
        self.assertEqual(english_to_french("Today"),"Aujourd'hui")
    def test3(self): 
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test4(self): 
        self.assertNotEqual(english_to_french("No"),"No")
        
class TestFrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("null"),"Null")
    def test2(self): 
        self.assertEqual(french_to_english("Aujourd'hui"),"Today")
    def test3(self): 
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    def test4(self): 
        self.assertEqual(french_to_english("Non"),"No")

unittest.main()