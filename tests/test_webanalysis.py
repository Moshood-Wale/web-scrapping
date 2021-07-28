# Modules imported

import unittest

from unittest.case import TestCase

from webanalysis import WebAnalysis



class TestWebAnalysis(unittest.TestCase):
    
    def word_count(self):
        result = WebAnalysis.word_count("software")
        self.assertEqual(result)

    
    def word_count(self):
        result = WebAnalysis.word_count("Events")
        self.assertEqual(result)
    

if __name__=='__main__':
    unittest.main() 