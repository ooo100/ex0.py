def or_(a,b):
    if a<b:
        return a
    else:
        return b
print(or_(7,6))

x = 9.5
if 8 < x < 10:
    print("x is near 9")

def true_func():
    print("true_func()")
    return True
def false_func():
    print("false_func()")
    return False
true_func() or false_func()

a, b, c, d = 1,2,3,4
print(a ** (b - c))
print(a - b * c / d)

def counter():         #?????
    num=0
    def incrementer():
        nonlocal num
        num += 1
        print(num)
        return num 
    return incrementer
counter()

x ='wow'
def read_x():
    print(x)
read_x()

y = 'nooo'
def change_global_y():
    global y
    y = 'yess'
    print(y)
change_global_y()
print(y)

z = [0, 1 ,2 ,3]
del z[0:2]
print(z)

d = 1                      #?????
def func():
    d = 2
    print(foo)
    print(globals()['d'])
    print(locals()['d'])

n = 5
if n > 10:
    print('big')
elif n < 10:
    print('small')
else:
    print('same')

def printo():
    print('on_no')
0 and printo()
printo()


if True:
    print ('it is true')
else: 
    print('it is false')


o = 'boobaa'
u = 'boobaa'
print(o==u)
print(o is u)

# def hoa ():  #??????
    #if hoa is not None: 
        #print (pass)
    #if hoa is None:
        #print (pass)

class Hoo(object):
    def __init__(self, item):
        self.my_item = item
    def __eq__(self, other):
        return self.my_item == other.my_item
a = Hoo(5)
b = Hoo(5)
print(a == b)
print(a != b)
print(a is b)

i = 0
while i < 10:
    print(i)
    if i == 5:
        print("Break!!!!!!!")
        break
    i += 1

for i in (1, 2, 3, 4, 5):
    print(i)
    if i == 3:
        break

for i in (1, 2, 3, 4, 5 ,6 ,7): #??? 3 ???
    if i == 2 or i == 5:
        continue
    print(i)

for i in range(5):
    print(i)

for index, item in enumerate(['your', 'are', 'a', '??']):
    print(index, '_____', item)

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print('wow')

d = {"a": 1, "b":2, "c":3}
for value in d.values():
    print (value)

from array import *
myarray = array ('i', [1,2,3,4,5])
for i in myarray:
    print(i)

list = [[1,2,3],[4,5,6],[7,8,9]]
print (list[0])
print (list[2])

d = {a:b for a,b in [('key', 'value')]}  #?????
d = dict(key='value')
print (d)

dog = {'name': 'wow', 'color':'gold' , 'special':'tail'} #???order???
cat = {'name': 'Mew', 'color': 'black', 'age':'old'}
from collections import ChainMap
print(dict(ChainMap(dog, cat)))

a = [1,2,3,4,5]
a.append(6)
a.index(3)
a.remove(1)
print(a)

alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [11,12,13]]]
print(alist[0][1][0])







