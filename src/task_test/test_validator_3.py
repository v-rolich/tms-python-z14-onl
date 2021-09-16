import unittest
from validators import *


class TestFunc(unittest.TestCase):

    def test_pages(self):
        with self.assertRaises(TypeError):
            validate_pages("2")
        with self.assertRaises(ValueError):
            validate_pages(-1)

    def test_year(self):
        with self.assertRaises(TypeError):
            validate_year("2")
        with self.assertRaises(ValueError):
            validate_year(5000)

    def test_author(self):
        with self.assertRaises(TypeError):
            validate_author(5)
        with self.assertRaises(ValueError):
            validate_author("")

    def test_price(self):
        with self.assertRaises(TypeError):
            validate_price("5")
        with self.assertRaises(ValueError):
            validate_price(-10)


if __name__ == '__main__':
    unittest.main()
