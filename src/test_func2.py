import unittest
from func2 import validate_args


class TestFunc(unittest.TestCase):

    def test_validate_args(self):
        with self.assertRaises(ValueError):
            validate_args('8', '9')
