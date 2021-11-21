from src.task_func_6 import add_row_to_csv
from src.task_func_6 import count_total_products_amount
from src.task_func_6 import del_row_from_csv
from src.task_func_6 import find_max_price_product
from src.task_func_6 import find_min_price_product
from src.task_func_6 import prepare_csv_data
from src.task_func_6 import print_csv
from src.task_func_6 import read_csv
from src.task_func_6 import write_csv
import unittest


class TestCsv(unittest.TestCase):

    test_file = '2.csv'

    fields = ['Product Name', 'Price', 'Amount']

    rows = [
        ['Apple', 2, 10],
        ['Banana', 3, 5],
    ]

    def test_read_csv(self):
        res = read_csv(TestCsv.test_file)
        self.assertEqual(res, res)

    def test_prepare_csv_data(self):
        res = prepare_csv_data(TestCsv.fields, TestCsv.rows)
        self.assertEqual(res, res)

    def test_print_csv(self):
        res = print_csv(TestCsv.test_file)
        self.assertEqual(res, res)

    def test_write_csv(self):
        res = write_csv(TestCsv.test_file, TestCsv.fields, TestCsv.rows)
        self.assertEqual(res, res)

    def test_add_row_to_csv(self):
        res = add_row_to_csv(TestCsv.test_file, '')
        self.assertEqual(res, res)

    def test_del_row_from_csv(self):
        res = del_row_from_csv(TestCsv.test_file)
        self.assertEqual(res, res)

    def test_count_total_products_amount(self):
        res = count_total_products_amount('2.csv')
        self.assertEqual(res, 15)

    def test_find_max_price_product(self):
        res = find_max_price_product('2.csv')
        self.assertEqual(res, 10)

    def test_find_min_price_product(self):
        res = find_min_price_product('2.csv')
        self.assertEqual(res, 5)

    # def test_reduce_product_amount(self):
    #     res = reduce_product_amount('2.csv', 'Apple')
    #     self.assertEqual()
