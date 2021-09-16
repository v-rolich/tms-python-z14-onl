from src.task_func_2 import validate_args
import unittest


class TestFunc(unittest.TestCase):

    def test_validate_args(self):
        with self.assertRaises(ValueError):
            validate_args('1', '1')
