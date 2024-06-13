"""
write a python program that takes a list of numbers and returns the sum of all the even numbers 
in the list.
"""

def addEven() :
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    allSum = 0
    for num in nums :
        if num % 2 == 0 :
            allSum = allSum + num
    print(allSum)
addEven()