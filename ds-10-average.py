"""
write a python program that takes a list of numbers and returns average of all the numbers in list.
"""

def average() :
    nums = [23, 12, 34, 56, 6, 334, 56, 13 ,45, 23, 345]
    length = len(nums)
    result = sum(nums) / length
    print("Average of ", nums, "is", format(result, '.2f'))
average()