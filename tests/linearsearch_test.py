"""
Author: Mohammed Fahad Kaleem
"""

import unittest

from algorithms.searching import (
    linear_search
)


class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.inputList = [2,65,12,90,123,76,71]
        self.elementInList = 90
        self.elementNotInList = 17

    def test_linear_search_correct_result(self):
        self.assertEqual(True, linear_search.search(self.inputList, self.elementInList))


    def test_linear_search_incorrect_result(self):
        self.assertEqual(False, linear_search.search(self.inputList, self.elementNotInList))

if __name__ == "__main__":
    unittest.main()