"""
write a program that takes in a string and check it contains lower case, upper case or both.
"""

"""def case():
    capital = False
    small = False
    try : string = input("Enter your string: \n")
    except : print("invalid input !")
    else :
        for char in string :
            if char.isupper() : capital = True
            else : small = True
    
        if capital and small : print("String contains both lower and upper case characters")
        else :
            if capital : print("String contains only upper case characters")
            else : print("String contains only lower case characters")
case()"""

def case() :
    string = input("Enter your string: \n")
    capital = any(char.isupper() for char in string)
    small = any(char.islower() for char in string)
    if capital and small : print("String contains both lower and upper case characters")
    else :
        if capital : print("String contains only upper case characters")
        else : print("String contains only lower case characters")
case()