from src.task_func_4 import validate_author
from src.task_func_4 import validate_pages
from src.task_func_4 import validate_price
from src.task_func_4 import validate_year
import unittest


class TestFunc(unittest.TestCase):

    def test_validate_author(self):
        with self.assertRaises(TypeError):
            validate_author(1)
        with self.assertRaises(ValueError):
            validate_author('')

    def test_validate_pages(self):
        with self.assertRaises(TypeError):
            validate_pages('a')
        with self.assertRaises(ValueError):
            validate_pages(0)

    def test_validate_price(self):
        with self.assertRaises(TypeError):
            validate_price('1')
        with self.assertRaises(ValueError):
            validate_price(-1)

    def test_validate_year(self):
        with self.assertRaises(TypeError):
            validate_year('1')
        with self.assertRaises(ValueError):
            validate_year(2222)
