import unittest
from funcs import *


class TestFunc2(unittest.TestCase):
    matrix = [[0, 10, 8],
              [5, 5, 6],
              [0, 7, 0]
              ]

    def test_matrix_max_elem(self):
        result = matrix_max_elem(TestFunc2.matrix)
        self.assertEqual(result, 10)

    def test_matrix_min_elem(self):
        result = matrix_min_elem(TestFunc2.matrix)
        self.assertEqual(result, 0)

    def test_matrix_sum(self):
        result = matrix_sum(TestFunc2.matrix)
        self.assertEqual(result, 41)


if __name__ == '__main__':
    unittest.main()
