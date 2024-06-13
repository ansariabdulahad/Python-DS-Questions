# write a python program to calculate the BMI (Body Mass Index)

def bmi() :
    try : 
        height = float(input("Enter your Height in meter: \n"))
        weight = float(input("Enter your Weight in kilogram: \n"))
    except ValueError as err : raise(err)
    else :
        bmi = weight / (height * height)

        if bmi < 18.5 : print("Under Weight")
        elif bmi < 24.9 : print("Normal Weight")
        elif bmi < 36.5 : print("Over Weight")
        else : print("Obese Weight")
bmi()