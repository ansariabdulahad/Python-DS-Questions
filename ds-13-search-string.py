"""
write a program that takes a list of strings and returns a new list with only the string contains
the letter input by user.
"""

def charSearch():
    strings = ['ahad', 'noor', 'samad', 'wahid']
    char = input("Enter your letter: \n")
    result = []

    for string in strings :
        if char in string :
            result.append(string)
    print("Search result is :",result)
charSearch()