import unittest
from func3 import Math


class TestFunc(unittest.TestCase):
    inst_2 = Math(9, 10)

    def test_init(self):
        self.assertIsInstance(TestFunc.inst_2, Math)

    def test_calc_sum(self):
        result = TestFunc.inst_2.calc_sum()
        self.assertEqual(result, 19)

    def test_calc_diff(self):
        result = TestFunc.inst_2.calc_diff()
        self.assertEqual(result, -1)

    def test_calc_mult(self):
        result = TestFunc.inst_2.calc_mult()
        self.assertEqual(result, 90)

    def test_calc_div(self):
        result = TestFunc.inst_2.calc_div()
        self.assertEqual(result, 0.9)
