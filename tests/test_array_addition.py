import unittest
import sys
from array_addition import ArrayAddition


class TestArrayAddition(unittest.TestCase):

    def setUp(self) -> None:
        self.array1 = [5, 6, 7, 8]
        self.array2 = [9, 9, 9, 9]
        self.array3 = [9, 9, 9, 9, 9, 9, 9]
        self.aa = ArrayAddition()

    def test_correct_array_addition(self):
        print('running correct_array_addition')
        self.assertNotEqual(self.aa.get_output_array(self.array1), [5])
        self.assertEqual(self.aa.get_output_array(self.array1), [5, 6, 7, 9])

    def test_carry_over_addition(self):
        self.assertEqual(self.aa.get_output_array(self.array2), [1, 0, 0, 0, 0])
        self.assertEqual(self.aa.get_output_array(self.array3), [1, 0, 0, 0, 0, 0, 0, 0])
