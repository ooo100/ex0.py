x = 'wow'
print(x)

a = b = c = 1
print(a, b, c)

d = reversed('green') #??not working??
print(d)

e = '123'
print(type(e))

names = ['Noo', 'Yess', 'Ann', 'Po', 'Na']
print (names[0])
print (names[-1])

name = ['Noo', 'Yess', 'Ann', 'Po', 'Na']
name.append('Woo')
print (name)

name = ['Noo', 'Yess', 'Ann', 'Po', 'Na']
name.insert(1, 'Aoo')
print (name)

f = [1,1,1,1,2,3] #?????
x= f.count(1)
print(f.count(1)) 

f = [1,1,1,1,2,3] 
f.reverse()
print(f) 

f = [1,1,1,1,2,3] #?????
f[::-1]
print(f) 

age = input('Your age? ')
print(age)

import datetime
today = datetime.datetime.now()
print(str(today))
print(repr(today)) #........

dic = {'name' : "Ann" , 'age' : 10}
print (dic)
print (dic['name'])
print (dic.values())
print (dic.keys())

def wow():       #?????
    """woowo"""
print(wow)

from datetime import datetime, timedelta
now = datetime.now()
then = datetime (2020, 8, 24)
delta = now - then
print (delta.days)
print (delta.seconds)

import datetime
today = datetime.date.today()
print ('Today:' ,today)

from enum import Enum
class Color(Enum):
    red = 1
    yellow = 2
    blue = 3
print (Color(2))
print (Color['blue'])

g = {1,2,2,3,3}
h = {3,3,4,4,5}
s = g.intersection(h)
print(s)

i, j, k, l, n = 2,1,3,4,5 #?????
import operator
operator.div(i, j)
print (operator)

m, o = 2,3  #pow??????
(m ** o)
pow (m, o)
print (pow)
import math    #???
math.pow(m,o)
print (m,o)

import math  #.......
import cmath
math.log(4)
cmath.log(4)













