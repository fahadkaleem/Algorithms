"""
    Binary Search
    -------------
    Takes a list of integers and compares it with the 'key'
    Time Complexity: O(log n) where n is the number of elements
    More details about Binary Search on https://en.wikipedia.org/wiki/Binary_search_algorithm
"""
import random
__author__ = "Mohammed Fahad Kaleem"

def iterative_search(inputList,key):
    """
    Iterative approach for Binary Search, Checks if the 'key' is in the inputList
    :param inputList: A list with elements
    :param key: An element that needs to be found in the list
    :return: Returns index if the 'key' is found
             Returns 'False' if the 'key' is not found
    """
    low = 0
    high = len(inputList)-1
    while low <= high:
        mid = low + (high-low)//2
        if key>inputList[mid]:
            low = mid+1
        elif key<inputList[mid]:
            high = mid-1
        else:
            return mid
    return False

def recursive_search(inputList,low,high,key):
    if len(inputList) == 0:
        return False
    if high>=low:
        mid = low + (high-low)//2
        if key>inputList[mid]:
            return recursive_search(inputList,mid+1,high,key)
        elif key<inputList[mid]:
            return recursive_search(inputList,low,mid-1,key)
        else:
            return mid
    else:
        return False
