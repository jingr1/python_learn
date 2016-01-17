#!C:\python35\python.exe
#!/usr/bin/env python3  #linux system 
# -*- coding:utf-8 -*-  # for chinese character

from myabs import my_abs
import math
'''
def __sum__(n):
    if n>=0:
        return(n*n+1)
    else:
        pass
s=0
for n in range(101):
    s= __sum__(n)+s
    print('__sum__(', n, ')=', __sum__(n),' s =', s)
print(s)
'''

print('my_abs(-100) = ',my_abs(-100))
print('sqrt(2)= ', math.sqrt(2))


#x^n, x^2 as defalt
def power(x, n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
    
print('5^3 =',power(5,3))
print('5^2 =',power(5))
print('5^2 =',power(5,2))


def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
    
    
# variable argument
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum
    
print ('calc(1,2,3,4)=',calc(1,2,3,4),'calc(1,2,3) =',calc(1,2,3))

# keyword argument
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
    
    
# 汉诺塔的移动
'''
编写move(n,a,b,c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
然后打印出把所有盘子从A借助B移动到C的方法 
'''   
def mov(n,a,b,c):
    if 1==n:
        print(a,'-->',c)    #如果只有一个盘子，直接从A动到C
    else:
        mov(n-1,a,c,b)    #step1：将前n-1个盘子从A移动到B
        mov(1,a,b,c)      #step2：将最底下的第n号盘子从A移动到C
        mov(n-1,b,a,c)    #step3：将B上的n-1个盘子移动到C
        
mov(3,'A','B','C')
'''
#递归过程分解，n>3时同理：        
mov(3,A,B,C)    #调用函数
    mov(2,A,C,B)        #step1：将前n-1个盘子从A移动到B
        mov(1,A,B,C)    #打印A-->C
        mov(1,A,C,B)    #打印A-->B
        mov(1,C,A,B)    #打印C-->B

                        #step2：将最底下的第n号盘子从A移动到C
    mov(1,A,B,C)        #打印A-->C

    mov(2,B,A,C)        #step3：将B上的n-1个盘子移动到C
        mov(1,B,C,A)     #打印B-->A
        mov(1,B,A,C)     #打印B-->C
        mov(1,A,B,C)     #打印A-->C
'''

# high-order function
def add(x,y,f):
    return f(x)+f(y)
    
print ('abs(-5)+abs(6)=',add(-5,6,abs))

#map
print([x*x for x in range(1,10)])

def f(x):
    return x*x

r = map(f,[a for a in range(1,10)])
print(r)
print(list(r))

print(list(map(str,[1,2,3,4,5])))

def normalize(name):
    def fn(s):
        return s[0].upper()+s[1:].lower()
    return (map(fn,name))
L = ['adaM','JIM','lISA']    
print(list(normalize(L)))

#reduce
from functools import reduce

def char2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))
print (char2int('13579'))

def prod(L):
    def product(x,y):
        return x*y
    return reduce(product,L)
    
L2 = [1,2,3,4,5]
print(prod(L2))

def str2float(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    s1,s2 = s.split('.')
    return reduce(fn,map(char2num,s1))+reduce(fn,map(char2num,s2))/pow(10,len(s2))
    
print(str2float('123.456'))

#filter
#用 filter 求素数
def primes():
    yield 2
    def _odd_iter():
        n = 1
        while True:
            n = n+2
            yield n
    def _not_divisible(n):
        return lambda x:x%n>0 #匿名函数
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n<100:
        print(n)
    else:
        break
        
        
#回数
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(list(filter(is_palindrome, range(1,10000))))

#sorted

Lstr = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(Lstr))
print(sorted(Lstr,key=str.lower))
print(sorted(Lstr,key=str.lower,reverse=True))    
    
Ldict = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(L):
    return L[0]
def by_score(L):
    return L[1]
print (sorted(Ldict,key = by_name))
print (sorted(Ldict,key = by_score,reverse=True))


#decorator
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
    
@log('begin call')
def now():
    print('2015-3-25')

now()

#Partial function
    
print ('int(\'10010\')=' , int('10010'))

int2 = functools.partial(int,base=2)
print ('int2(\'10010\')=' , int2('10010'))

    
   


    