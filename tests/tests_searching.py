"""
Tests for Searching
"""

import unittest

from algorithms.searching import (
    linear_search,
    binary_search
)


class TestLinearSearch(unittest.TestCase):
    """
    Tests Linear search with a Integer or String Lists
    """
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


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.inputList = [2,65,12,90,123,76,71]
        self.low = 0
        self.high = len(self.inputList)-1
        self.elementInList = 65
        self.elementNotInList = 87
        self.emptyList = []

    def test_binary_search_correct_result(self):
        self.assertEqual(1, binary_search.iterative_search(self.inputList,self.elementInList))
        self.assertEqual(1, binary_search.recursive_search(self.inputList,self.low,self.high,self.elementInList))

    def test_binary_search_incorrect_result(self):
        self.assertEqual(False, binary_search.iterative_search(self.inputList,self.elementNotInList))
        self.assertEqual(False, binary_search.recursive_search(self.inputList,self.low,self.high,self.elementNotInList))

    def test_binary_search_emptyList_result(self):
        self.assertEqual(False, binary_search.iterative_search(self.emptyList,self.elementInList))
        self.assertEqual(False, binary_search.recursive_search(self.emptyList,self.low,len(self.emptyList)-1,self.elementInList))

if __name__ == "__main__":
    unittest.main()