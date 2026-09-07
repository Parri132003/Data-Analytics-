'''
Day 21(7/09/26)
BUILT- IN FUNCTIONS:
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))
print(math.cos(5))

import  random
print(random.randint(100000,999999))
print(random.randrange(1,100))
color =['red','pink','blue','orange','yellow']
print(random.choice(color))
random.shuffle(color)
print(color)

import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor())

import collections
data_ =['banana','apple','banana','orange','orange']
print(collections.Counter(data_))
all_ = collections.Counter(data_)
print(all_.most_common())

from collections import defaultdict
data_ = defaultdict(list)
data_['python']. append('madhi')
data_['python'].append('mani')
data_['java'].append('sweety')
print(data_)

from datetime import datetime
today = datetime.today()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)

from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m,-%y'))
print(now.strftime('%H:%M:%S'))
print(now.strftime('%a'))


***example program:***
import random
attep_ =3
num = random.randrange(1,100)
print(num)
while attep_ >0:
    game_ = int(input('Enter a number between 1 and 100:'))
    if game_ == num:
        print(" your guess is correct")
        break
    else:
        attep_ -= 1
if attep_ == 3:
    print('price money is 500')
elif attep_ ==2:
    print('price money is 200')
elif attep_ ==1:
    print('print money is 100')
else:
    print('better luck next time')
-----------------------------------------------
# itertools:
import itertools
a = itertools.count(45)
print(next(a))
print(next(a))

b = itertools.repeat('python',6)
for j in b:
    print(j)
c = itertools.cycle(['python','java','c'])
for j in c:
    print(j)
--------------------------------------------------
import itertools
n = itertools.chain([1,2,3],[4,5,6])
print(list(n))

'''

import itertools
n = itertools.chain([1,2,3],[4,5,6])
print(list(n))











































