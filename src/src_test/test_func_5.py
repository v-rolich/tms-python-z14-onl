from src.task_func_5 import matrix_max_elem
from src.task_func_5 import matrix_min_elem
from src.task_func_5 import matrix_sum
import unittest


class TestFunc(unittest.TestCase):

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]
              ]

    def test_max_elem(self):
        res = matrix_max_elem(TestFunc.matrix)
        self.assertEqual(res, 9)

    def test_min_elem(self):
        res = matrix_min_elem(TestFunc.matrix)
        self.assertEqual(res, 1)

    def test_matrix_sum(self):
        res = matrix_sum(TestFunc.matrix)
        self.assertEqual(res, 45)
