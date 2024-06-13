"""
write a python program that takes a number from the user and check if number is prime number or not.
"""

def primeNumber() :
    try : num = int(input("Enter a number : \n"))
    except : print("Invalid Input")
    else :
        if num > 1 :
            for index in range(2, num) :
                if num % index == 0 :
                    print(num, "is not Prime Number")
                    break
            else : 
                print(num, "is prime number")
        else :
            print(num, "is not prime number")
primeNumber()