'''
day 18(3/9/26)
Lambda function:
-->lambda function is small anonymous function. 
--> lambda can take n number arguments, but only with one expression.
--> the function is defined by using lambda keyword.
syntax:- lambda arguments : expression
eg:-
add_ = lambda a,b,c : a+b+c
print(add_(10,20,9))

eg 2:- by using lambda function  check whether number is even or odd?
even = lambda num : num % 2 ==0
print(even(10))

eg 3:-by using lambda function  check the greater number?
great_ = lambda a,b: a if a>b else b
print(great_(90,20))

eg 4:- by using lambda function find cube number?
cube = lambda x: x**3
print(cube(5))

FILTER():-
filter() function will perform only on selected elements of iterables.
syntaX:- filter(lambda arguments: expression,iterables)
eg:-
nums = [1,2,3,4,5,6]
data_ = filter(lambda a: a%2==0,nums)
print(tuple(data_))

eg:-
nums = [1,2,3,4,5,6]
data_ = filter(lambda a: a>2,nums)
print(tuple(data_))

MAP():-
map() function will perform on all elements of a iterable.
syntax:-  map(lambda arguments: expression, iterable)
eg:-
nums = [1,2,3,4,5,6]
get_ = map(lambda a: a+6,nums)
print(list(get_))

Reduce():-
--> the reduce() function repearedly applies a function to the elements and reduces them to one final value.
--> it is available in the functool module.
syntax:-  reduce(lambda arguments: expression, iterable)
eg 1:-
from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,nums)
print (data_)

eg 2:-
from functools import reduce
num = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,range(1,10))
print (data_)
















'''

from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,nums)
print (data_)









