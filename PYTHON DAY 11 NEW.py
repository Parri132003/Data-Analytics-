'''
day 11(26/08/26)

Elif:-
->elif statement is used to check more possible outcomes or more conditions
 eg1:-   a=90
    b=780
    c=670
if a>b and a>c: # 90>780 and90>670
    print(a)
elif b>a and b>c: # 780>90and 780>670
        print(b)
else:
     print (c)
     
eg2:-num=7
     num_2=3
user_opt= int(input('Enter\n1.add\n2.sub\n3.mul\n4.pow:')
if user_opt==1:
print(num1+num_2)
elif user_pot==2:
print(num-num_2)
elif user_opt==3:
print(num-num_2)
elif user_opt==3:
    print(num*num_2)
else user_pot==4:
    print(num**num_2)


Nested if:-
-> if inside an if statement is called nested if


Example:-
app_details ={'pin':1234}

import random
user_pass =int(input("ENTER your app password:"))
otp = random.randint(1000,9999)
if user_pass == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = int(input("ENTER 4 digit otp:"))
    
    if user_otp == otp:
        print('welcome to the app')
    else:
        print('incorrect otp')
else:
     print('password is incorrect')

eg:-
a= int(input("Enter a number:"))
if a % 2 ==0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

-----> GRADING SYSTEM:-
marks_ = int(input("Enter your marks:"))
if marks_>=90:
    print('A+')
elif marks_>=80:
    print('A')
elif marks_>=70:
    print('B+')
elif marks_>=60:
    print('b')
elif marks_>=50:
    print('c+')
elif marks_>=40:
    print('c')
else:
    print('fail')

'''
