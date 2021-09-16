import unittest
from func_2 import validate_args


class TestFunc2(unittest.TestCase):

    def test_func_2(self):
        result = validate_args(5, 2.5)
        self.assertIsNone(result, "int or float")


if __name__ == '__main__':
    unittest.main()
