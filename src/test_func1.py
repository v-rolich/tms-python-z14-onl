import unittest
from func1 import calc_sum, calc_diff, calc_mult, calc_div


class TestFunc(unittest.TestCase):

    def test_calc_sum(self):
        result = calc_sum(2, 3)
        self.assertEqual(result, 5)

    def test_calc_diff(self):
        result = calc_diff(5, 2)
        self.assertEqual(result, 3)

    def test_calc_mult(self):
        result = calc_mult(5, 2)
        self.assertEqual(result, 10)

    def test_calc_div(self):
        result = calc_div(6, 6)
        self.assertEqual(result, 1)
