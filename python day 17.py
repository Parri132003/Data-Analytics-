'''
day 17(2/9/26)

SCOPE OF VARIABLES
1. LOCAL VARIABLE:
a variable is define inside the function call it as local variable,
python3.dll
eg:-def display():
    name ='madhu'
    print(name)
display()

2. GLOBAL VARIABLES:
a variable that is define outside the function call
and it can be access anywhere through out program.

eg:- a = 90
def display():
    print(a)
display()
print(a)

eg:- 
a = 90
print(a)
def display():
 global a
 a=10
display()
print(a) 

GLOBAL KEYWORD:
global is keyword used to reaccess new  values to variable
that was already define outside the function call.
eg:-
a = 90
print(a)
def display():
 global a
 a=10
display()
print(a)

PASSING BY VALUE:
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(109)

PASSING BY REFERENCE:
num = 7
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)

RECURSIVE FUNCTION:-
the function call itself until the base condition met....
eg:-
def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(5))


'''



































 
