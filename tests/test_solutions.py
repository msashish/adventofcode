from common_tools import CommonTools
import unittest
from day1_2019 import Day1Puzzle


class TestConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.mass_list = CommonTools().get_input_data('day1_2019')

    def test_day1(self):
        print("testing day1_2019 puzzle")
        self.assertEqual(Day1Puzzle().calculate_fuel(self.mass_list), 3369286)
