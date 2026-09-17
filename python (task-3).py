1.
# practice
print("----------- Grade Checker -----------")

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks enteredd")

elif marks >= 90:
    print("Grade: A")
    print("Remark: Outstanding!")

elif marks >= 80:
    print("Grade: B")
    print("Remark: Excellent!")

elif marks >= 70:
    print("Grade: C")
    print("Remark: Good")

elif marks >= 60:
    print("Grade:D")
    print("Remark: better, needs improvement")

elif marks >= 50:
    print("Grade: E")
    print("Remark: Poor, needs serious improvement")

else:
    print("Grade: F")
    print("Remark: Failed, needs to reappear")

2.
#Even-Odd Checker (with Twist)
num = int(input("Enter a number:"))
if num == 0:
    print("Zero is neither even nor odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even Number")
elif num < 0 and num % 2 != 0:
    print("Negative Odd Number")
elif num > 0 and num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

3.
#Season Identifier
month = int(input("Enter a month number (1-12):"))
if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
else:
    print("Invalid month entered")








































