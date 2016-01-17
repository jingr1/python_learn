#!C:\python35\python.exe
#!/usr/bin/env python3  #linux system 
# -*- coding:utf-8 -*-  # for chinese character
'''
name = input('please enter your name: ' )
print("hello",name)
'''
#景日
#string and encoding
print ('牧云轩')

ascii_A = ord('A')
str_B = chr(66)
bytes_abc = 'abc'.encode('ascii')
utf_jr = '景日'.encode('utf-8')
str_ABC = b'ABC'.decode('ascii')
ch_jr = b'\xe6\x99\xaf\xe6\x97\xa5'.decode('utf-8')
len_jr = len(ch_jr)
print(' ascii_A = %d = 0x%x\n str_B = %s\n bytes_abc = %s\n utf_jr = %s\n str_ABC = %s\n ch_jr = %s\n len_jr = %s' % (ascii_A,ascii_A,str_B,bytes_abc,utf_jr,str_ABC,ch_jr,len_jr) )

print(' pi = %.3f\n growth rate: %d %%' % (3.1415926,70))

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('growth rate = %2.1f%%' % r)

#list

classmates = ['Lucy','Micheal','Tom']
print('classmates = %s \nlen(classmates)= %d \nclassmates[-1] = %s \nclassmates[0] = %s' % (classmates,len(classmates),classmates[-1],classmates[0]))
classmates.append('Bob')
print('classmates.append(Bob) = %s \nlen(classmates)= %d \nclassmates[-1] = %s \nclassmates[0] = %s' % (classmates,len(classmates),classmates[-1],classmates[0]))
classmates.insert(1, 'Jack')
print('classmates.insert(1, Jack) = %s \nlen(classmates)= %d \nclassmates[-1] = %s \nclassmates[0] = %s' % (classmates,len(classmates),classmates[-1],classmates[0]))
classmates.pop(0)
print('classmates.pop(0) = %s \nlen(classmates)= %d \nclassmates[-1] = %s \nclassmates[0] = %s' % (classmates,len(classmates),classmates[-1],classmates[0]))
classmates.pop()
print('classmates.pop() = %s \nlen(classmates)= %d \nclassmates[-1] = %s \nclassmates[0] = %s' % (classmates,len(classmates),classmates[-1],classmates[0]))
classmates[0] = 'Jerry'
print('classmates[0]=jerry = %s \nlen(classmates)= %d \nclassmates[-1] = %s \nclassmates[0] = %s' % (classmates,len(classmates),classmates[-1],classmates[0]))

s = ['python', 'java', ['asp', 'php'], 'scheme','123']
print('s = %s \nlen(s)= %d \ns[2][1] = %s \ns[2] = %s' %(s,len(s),s[2][1],s[2]))

#tuple
classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
# cannot modify tuple:
#classmates[0] = 'Adam'  #error

#dict

#set

#iteration
from collections import Iterable

print(isinstance('abc',Iterable)) #str is iterable?

#list comprehensions
print(list(range(1,11)))
print([x*x for x in range(1,11) if x%2 ==0])
print([m+n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])

d = {'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])
L = ['HEllo']
print([s.lower() for s in L])
print([s.upper() for s in L])
L1 = ['HEllo',18]
print([s.lower() for s in L1 if isinstance(s,str)])

#generator
g= (x*x for x in range(1,11))
print(g)
print([n for n in g])

#fibonacci numbers

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'
print(fib(6))

def fib_g(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'
print(fib_g(6))
print([n for n in fib_g(6)])

#binomial array

def triangles():
    L =[1,]
    while(True):
        yield L
        i = len(L)-1
        while(i):
            L[i] = L[i]+L[i-1]
            i-=1
        L.append(1)
n = 0
for t in triangles():
    print(t)
    n=n+1
    if n ==10:
        break
    


