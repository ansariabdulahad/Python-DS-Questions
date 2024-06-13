"""
write a python program that takes a list of strings and return the longest string in the list.
"""

def longString() :
    strings = ['ahad', 'ahad ansari', 'samad', 'noor ansasri', 'wasiuddin umari']
    longestStr = strings[0]

    for str in strings :
        if len(str) > len(longestStr) :
            longestStr = str
    print("Longest string is ", longestStr)
longString()