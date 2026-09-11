'''
------

Exception handling:-

Definition:-
---> This is the way handling errors
---> we can write any number exception for one code written at try block

try:
    print(6/0)
except:
    print('Not Divisible by zero')


four components:-


----> 1.Try:-

Definition:- The try block where we can write code which may contain errors
--- syntax:-
try:
    code lines

    
-----> 2.except
----
Definition:- This will handle errors that are raised at try block

--- syntax:-
except ErrorName:
    print("ErrorName")

Example:-

try:
    print(5/0)
    print(num)
except ZeroDivisionError:
    print('Not Divisible by zero')
except NameError:
    print('Name Error')

-----> 3.else
Definition:_ The Else block will only executes, if no error at try block

try:
    print("Hello")
except ZeroDivisionError:
    print('Not Divisible by zero')
except NameError:
    print('Name Error')
else:
    print('HELLO')


----> 4.finally
Definition:- This block will execute regardless with the error at try block

Example:-

try:
    print("Hello")
except ZeroDivisionError:
    print('Not Divisible by zero')
except NameError:
    print('Name Error')
else:
    print('HELLO')
finally:
    print('End')



----> File handling:-
----
The file handler is a object which is used to create, update, read, and delete...

modes:-
--
r
with open('NEW_FILE.txt','r') as file:
    print(file.read())

w
with open('NEW_FILE.txt','w') as file:
    file.write('This is sharon, I am your student')
a
with open('NEW_FILE.txt','a') as file:
    file.write('This is sharon, I am your student')

x




-------
'''
with open('python_file.txt','x') as file:
    file.write('This is sharon, I am your student')
