"""
Author: Mohammed Fahad Kaleem
"""
def search(inputList, elementToBeFound):
    position = 0
    while position < len(inputList):
        if inputList[position] == elementToBeFound:
            return True
        position += 1
    return False
