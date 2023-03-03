from whiteboard5 import *
import unittest

class ReformatTest(unittest.TestCase):

    def test_one(self):
        self.assertEqual(add_digits(48), 3)
        self.assertEqual(add_digits(59), 5)
    
    def test_two(self):
        self.assertEqual(add_digits(16), 7)
        self.assertEqual(add_digits(314), 8)

    def test_three(self):
        self.assertEqual(add_digits(29), 2)
        self.assertEqual(add_digits(999), 9)

unittest.main()