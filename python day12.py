'''
day 12(27/08/26)

LOOPING STATEMENTS:-

for loop:-
---> for loop is used to interate over a squence or iterable datatypes.
eg:-
nums = [12,3,5,78]
for num in nums:
    print(num)
    
print(num)=num define this variable at run to store values from itrable datatypes.

else in for:-
---> unlike if-else,else block in for statement is executed after completed of all iterations.
 eg:-nums = 'python'
for num in nums:
    print(num)
else:
    print('For ended')
    
---> control statements.
Break:- it is used to stop iteration based on the given condition.
nums = [1,2,3,4,5,6]
eg:-
for num in nums:
    print(num)
    if num == 3:
        break
        print(num)
        
--> based on if statement checking whether a number is odd or even.
eg:-val_ =[1,2,3,4,5,6,7,8,9]
for j in val_:
    if j %2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')
        
------->continue
 the continue is keyword used to skip the current iteration based on the condition
eg:-nums =[1,2,3,4,5,6,7,,8,9]
for num in nums:
    if num ==6:
        continue
        print(num)
   
pass:-
--> a pass is called as space nolder, that is used after statements like(if,for,else)not to raise any error.
eg:-
for j in range(1,11):
    if j == 15:
        print(j)
    else:
        pass

assert:-
--> assert is a keyword used to check the condition, incase the condition is false,it will raise the error(Assertion error).
eg:-
age =15
assert age >= 18 'not eligible to vote'
print('your eligible to vote')
   
---> while loop:-

eg:-
num = 1
while num < 5:
    print(num)
    num += 1








'''









