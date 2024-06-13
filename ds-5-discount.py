"""
write a python program that asks the user for their age and gender, and prints amessage indicates
whether they are elegible for a discount. Females under the age of 25 and males under the age of
22 are eligible for a discount.
"""

def discount() :
    try : 
        age = int(input("Enter your age :\n"))
        gender = input("Enter your gender male or female :\n")
    except ValueError as err : print(err)
    else :
        if gender == "male" or gender == "female" :
            if gender == "male" and age < 22 :
                print("Eligible for discount")
            elif gender == "female" and age < 25 :
                print("Eligible for discount")
            else :
                print("Not eligible for discount.")
        else :
            print("Please enter only male or female")
discount()