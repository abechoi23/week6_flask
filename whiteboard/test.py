from whiteboard import *
# change sumString to python file name, you can change * to function name
import unittest

class SecondIndexTest(unittest.TestCase):

    def test_one(self):
        result1 = second_index('Hello world!!!','l')
        self.assertEqual(result1, 3)
    
    def test_casing(self):
        result1 = second_index('HelLo world!!!','l')
        self.assertEqual(result1, 3)

    def test_two(self):
        result = second_index('', 'q')
        self.assertEqual(result,-1)

unittest.main()