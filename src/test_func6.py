import unittest
from func6 import matrix_sum, matrix_max_elem, matrix_min_elem


class TestFunc(unittest.TestCase):
    mx = [[1, 1, 1],
          [2, 2, 2],
          [3, 3, 3]
          ]

    def test_matrix_sum(self):
        result = matrix_sum(TestFunc.mx)
        self.assertEqual(result, 18)

    def test_matrix_max_elem(self):
        result = matrix_max_elem(TestFunc.mx)
        self.assertEqual(result, 3)

    def test_matrix_min_elem(self):
        result = matrix_min_elem(TestFunc.mx)
        self.assertEqual(result, 1)
