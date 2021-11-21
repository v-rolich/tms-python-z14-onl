import unittest
from math1 import Math


class TestFunc(unittest.TestCase):

    def test_sum(self):
        n = Math(6, 3)
        result = n.calc_sum()
        self.assertEqual(result, 9, "Should be 3")

    def test_diff(self):
        n = Math(6, 3)
        result = n.calc_diff()
        self.assertEqual(result, 3, "Should be 3")

    def test_mult(self):
        n = Math(6, 3)
        result = n.calc_mult()
        self.assertEqual(result, 18, "Should be 6")

    def test_div(self):
        n = Math(6, 3)
        result = n.calc_div()
        self.assertEqual(result, 2, "Should be 3")


if __name__ == '__main__':
    unittest.main()
