"""
Write a program that takes three numbers and checks if they form pythagorean triples. If they do,
print "This number for a pythagorean triples" if not print "This number do not form a pythagorean 
triples" 
"""

def triples() :
    try : 
        a = int(input("Enter number one : \n"))
        b = int(input("Enter number two : \n"))
        c = int(input("Enter number three : \n"))
    except ValueError as err : raise(err)
    else :
        if (a**2) + (b**2) == (c**2) : print("This number for a pythagorean triples")
        else : print("This number is not for a pythagorean triples")
triples()