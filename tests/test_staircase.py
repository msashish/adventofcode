import unittest
from staircase import StairCase


class TestStairCase(unittest.TestCase):

    def test_recursive_simple(self):
        s = StairCase()
        self.assertEqual(s.simple_recursive(1, [1, 2]), 1)
        self.assertEqual(s.simple_recursive(1, [2]), 0)
        self.assertEqual(s.simple_recursive(2, [2]), 1)
        self.assertEqual(s.simple_recursive(2, [1, 2]), 2)
        self.assertEqual(s.simple_recursive(3, [1, 2]), 3)
        self.assertEqual(s.simple_recursive(4, [1, 2]), 5)

    def test_recursive_large(self):
        s = StairCase()
        self.assertEqual(s.simple_recursive(5, [1, 3, 5]), 5)
        self.assertEqual(s.simple_recursive(5, [3, 5]), 1)

    def test_dp_bottom_up(self):
        s = StairCase()
        self.assertEqual(s.find_using_dp(1, [1, 2]), 1)
        self.assertEqual(s.find_using_dp(1, [2]), 0)
        self.assertEqual(s.find_using_dp(2, [2]), 1)
        self.assertEqual(s.find_using_dp(2, [1, 2]), 2)
        self.assertEqual(s.find_using_dp(3, [1, 2]), 3)
        self.assertEqual(s.find_using_dp(4, [1, 2]), 5)
        self.assertEqual(s.find_using_dp(5, [1, 3, 5]), 5)
        self.assertEqual(s.find_using_dp(5, [3, 5]), 1)
