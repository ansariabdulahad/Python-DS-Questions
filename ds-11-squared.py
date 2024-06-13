"""
write a pyhton program that takes a list of numbers and returns a new list with numbers squared.
"""

def squared() :
    nums = [2, 3, 4, 5, 6, 7, 8, 9]
    squared = []

    for num in nums :
        squared.append(num**2)
    print(f"sqaure list {squared} of this list {nums}")
squared()