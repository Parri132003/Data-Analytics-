'''
TASK-2

#User can enter height in centimeters,feets --> metres
#cal BMI
#make all user validations for height --> cms,feets
 '''     


weight = int(input("Enter the weight in kgs: "))
height = float(input("Enter the height: "))
unit = input("Enter the height unit (cms/feet): ")
name = input("Enter the name: ")

if weight > 0 and height > 0:
    
    if unit == "cms":
        height = height / 100

    elif unit == "feet":
        height = height * 0.3048

    else:
        print("Enter only cms or feet")

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print(f"BMI of {name} is {bmi} and you are Underweight --> Eat well")

    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"BMI of {name} is {bmi} and you are Healthy --> Keep consistent")

    elif bmi >= 25 and bmi <= 29.9:
        print(f"BMI of {name} is {bmi} and you are Overweight --> Start Exercising")

    elif bmi >= 30:
        print(f"{name} is in Obese Category and BMI is {bmi}")

else:
    print("Do enter only +ve values greater than 0")
