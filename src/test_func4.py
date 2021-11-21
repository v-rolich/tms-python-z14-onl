import unittest
from func4 import validate_pages, validate_price, validate_year, validate_author


class TestFunc(unittest.TestCase):

    def test_validate_pages(self):
        with self.assertRaises(TypeError):
            validate_pages('1')
        with self.assertRaises(ValueError):
            validate_pages(0)

    def test_validate_price(self):
        with self.assertRaises(TypeError):
            validate_price('1')
        with self.assertRaises(ValueError):
            validate_price(-100)

    def test_validate_year(self):
        with self.assertRaises(TypeError):
            validate_year('1')
        with self.assertRaises(ValueError):
            validate_year(2050)

    def test_validate_author(self):
        with self.assertRaises(TypeError):
            validate_author(9379992)
        with self.assertRaises(ValueError):
            validate_author('')
