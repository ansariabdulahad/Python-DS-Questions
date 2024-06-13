"""
write a python program that takes a string and returns the reverse of the string.
"""

def reverseString() :
    string = input("Enter a string: \n")
    length = len(string) - 1
    reversed = ''
    for index in range(length,-1,-1) :
        reversed = reversed + string[index]
    print("Your String is:", string)
    print("Reversed string is :",reversed)
reverseString()