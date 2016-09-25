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
        self.stringList = ['cat','apple','orange','bananan']
        self.emptyList = []
        self.elementInList = 90
        self.elementNotInList = 17
        self.string = 'orange'

    def test_linear_search_correct_result(self):
        self.assertEqual(3, linear_search.search(self.inputList, self.elementInList))

    def test_linear_search_incorrect_result(self):
        self.assertEqual(False, linear_search.search(self.inputList, self.elementNotInList))

    def test_linear_search_emptyList_result(self):
        self.assertEqual(False, linear_search.search(self.emptyList, self.elementInList))

    def test_linear_search_stringKey_IntegerList_result(self):
        self.assertEqual(False, linear_search.search(self.inputList, self.string))

    def test_linear_search_stringType_result(self):
        self.assertEqual(2, linear_search.search(self.stringList, self.string))

if __name__ == "__main__":
    unittest.main()