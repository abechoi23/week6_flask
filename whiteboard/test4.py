from whiteboard4 import *
import unittest


class PalindromeNumberTest(unittest.TestCase):

    def test_one(self):
        self.assertFalse(is_palindrome(10))
        self.assertFalse(is_palindrome(-101))
        self.assertTrue(is_palindrome(101))

    def test_two(self):
        self.assertTrue(is_palindrome(99))
        self.assertFalse(is_palindrome(12))

    def test_three(self):
        self.assertFalse(is_palindrome(-1))
        self.assertTrue(is_palindrome(1))


unittest.main()
