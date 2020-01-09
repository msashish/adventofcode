from common_tools import CommonTools
import sys


class Day1Puzzle:

    @staticmethod
    def calculate_fuel(masses):
        fuel = 0
        for mass in masses:
            mass_fuel = mass.strip('\n').strip('')
            fuel += int(mass_fuel)//3 - 2
        return fuel


if __name__ == '__main__':
    mass_list = CommonTools().get_input_data(sys.modules['__main__'].__file__)
    total_fuel = Day1Puzzle().calculate_fuel(mass_list)
    print("Total fuel required is: " + str(total_fuel))

