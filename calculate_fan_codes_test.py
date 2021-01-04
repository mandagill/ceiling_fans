import unittest

from calculate_fan_codes import CodeCalculator


class CodeCalculatorTest(unittest.TestCase):
    def test_adjacent_fans_use_different_codes(self):
        calc = CodeCalculator(fans=2, floors=1)
        codes = calc.calculate_floor()
        code1 = codes[0]
        code2 = codes[1]
        self.assertNotEqual(code1, code2)

    def test_codes_have_correct_format(self):

        calc = CodeCalculator(fans=1, floors=1)
        code_array = calc.calculate_floor()

        self.assertIsInstance(code_array, list)

    def test_consecutive_codes_are_different(self):
        calc = CodeCalculator(fans=2, floors=1)
        code_array = calc.calculate_floor()

        code1 = code_array[0]
        code2 = code_array[1]

        self.assertNotEqual(code1, code2)

    def test_calculate_floor_3_fans(self):
        """should return an array of arrays"""

        calc = CodeCalculator(fans=6, floors=1)
        code_array = calc.calculate_floor()
        print(code_array)

        self.assertIsInstance(code_array[0], list)
        self.assertIsInstance(code_array[1], list)

    def test_correct_number_of_codes_returned(self):
        """should return an array of 6 fan codes"""

        calc = CodeCalculator(fans=6, floors=1)
        code_array = calc.calculate_floor()

        self.assertEqual(len(code_array), 6)

    def test_calculate_building(self):
        """should return a dictionary of nested arrays"""
        pass


if __name__ == '__main__':
    unittest.main()
