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
        print(code_array)

        code1 = code_array[0]
        code2 = code_array[1]

        self.assertNotEqual(code1, code2)

    def test_calculate_floor(self):
        """should return an array of arrays"""
        pass

    def test_calculate_building(self):
        """should return a dictionary of nested arrays"""
        pass


if __name__ == '__main__':
    unittest.main()
