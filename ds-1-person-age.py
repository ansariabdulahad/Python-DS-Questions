""" 
write a python program that takes in a person's age and check if they are child (12), 
teenager (13-19), young adult (20-39), middle-aged adult (40-59) or senior (60+).
print an appropriate message for each age group 
"""

# Tried using without oops concept
"""
def personAge() :
    try: age = int(input("Enter your age: \n"))
    except : print("Invalid input !")
    else: 
        if age > 0 and age <= 12 : print("You are a child")
        elif age > 13 and age <= 19 : print("You are a teenage")
        elif age > 20 and age <= 39 : print("You are a young adult")
        elif age > 40 and age <= 59 : print("You are a middle age")
        else : print("You are a senior")
personAge()
"""

# Try using oops concept

class Main :
    def __init__(self) :
        try: age = int(input("Enter your age: \n"))
        except : print("Invalid input !")
        else: 
            if age > 0 and age <= 12 : print("You are a child")
            elif age > 13 and age <= 19 : print("You are a teenage")
            elif age > 20 and age <= 39 : print("You are a young adult")
            elif age > 40 and age <= 59 : print("You are a middle age.")
            else : print("You are a senior")
Main()