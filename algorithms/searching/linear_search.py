"""
    Linear Search Algorithm
    -----------------------
    Compare each element in the input list until the 'key' is found

    Time Complexity: O(n) where n is the number of elements in the input list

    More details about Linear Search on https://en.wikipedia.org/wiki/Linear_search
"""
__author__ = 'Mohammed Fahad Kaleem'

def search(inputList, key):
    """
    Takes a list and searches if 'key' is in the list
    :param inputList: A list with elements
    :param key: Element that needs to be searched for
    :return: Returns position if the 'key' is found
             Returns False if the 'key' is not found
    """
    position = 0
    while position < len(inputList):
        if inputList[position] == key:
            return position
        position += 1
    return False
