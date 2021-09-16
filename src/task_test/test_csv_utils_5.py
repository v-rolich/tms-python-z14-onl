import unittest
from csv_utils import *


class Testcsv(unittest.TestCase):

    def test_csv(self):
        result = read_csv("text.cvc")
        self.assertTupleEqual(result, (['1', '2', '3'], [['1', '4', '5']]))


if __name__ == '__main__':
    unittest.main()
