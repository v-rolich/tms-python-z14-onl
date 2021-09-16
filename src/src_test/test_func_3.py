import unittest
from src.task_func_3 import Math


class TestFunc(unittest.TestCase):

    args = Math(2, 2)

    def test_init(self):
        self.assertIsInstance(TestFunc.args, Math)

    def test_calc_sum(self):
        result = TestFunc.args.calc_sum()
        self.assertEqual(result, 4)

    def test_calc_diff(self):
        result = TestFunc.args.calc_diff()
        self.assertEqual(result, 0)

    def test_calc_mult(self):
        result = TestFunc.args.calc_mult()
        self.assertEqual(result, 4)

    def test_calc_div(self):
        result = TestFunc.args.calc_div()
        self.assertEqual(result, 1)
