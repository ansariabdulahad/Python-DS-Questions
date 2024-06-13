"""
write a python program that takes two lists and returns a new list with only the elements
that common in both the list.
"""

def commonList() :
    first = [1, 62, 3, 4, 1, 5, 7, 3, 9]
    second = [1, 62, 33, 43, 1, 5, 12, 3, 10]

    result = list(set(first) & set(second))
    print(result)
commonList()