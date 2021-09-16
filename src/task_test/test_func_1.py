import unittest
from func import calc_sum, calc_div, calc_diff, calc_mult


class TestFunc(unittest.TestCase):

    def test_sum(self):
        result = calc_sum(1, 2)
        self.assertEqual(result, 3, "Should be 3")

    def test_diff(self):
        result = calc_diff(5, 2)
        self.assertEqual(result, 3, "Should be 3")

    def test_mult(self):
        result = calc_mult(3, 2)
        self.assertEqual(result, 6, "Should be 6")

    def test_div(self):
        result = calc_div(6, 2)
        self.assertEqual(result, 3, "Should be 3")


if __name__ == '__main__':
    unittest.main()
