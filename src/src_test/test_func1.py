import unittest
from src.task_func_1 import calc_diff
from src.task_func_1 import calc_div
from src.task_func_1 import calc_mult
from src.task_func_1 import calc_sum


class TestFunc(unittest.TestCase):

    def test_calc_sum(self):
        result = calc_sum(3, 3)
        self.assertEqual(result, 6)

    def test_calc_diff(self):
        result = calc_diff(6, 2)
        self.assertEqual(result, 3)

    def test_calc_mult(self):
        result = calc_mult(5, 2)
        self.assertEqual(result, 10)

    def test_calc_div(self):
        result = calc_div(6, 6)
        self.assertEqual(result, 1)
