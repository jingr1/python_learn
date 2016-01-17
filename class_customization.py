#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#__str__

class Student(object):
    def __init__(self,name):
        self.name =name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
    
    def __getattr__(self,attr):
        if attr == 'age':
            return 99
        raise ArithmeticError('\'Student\' object has no attribute \'%s\''% attr)
    def __call__(self):
        print('my name is %s.'% self.name)
        
print(Student('Jerry'))
s = Student('Jerry')
print(s)
print('s.age=',s.age)
#print('s.score=',s.score)
#__iter__  class can be used to "for...in" for iteration
s()

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
        
for n in Fib():
    print(n)
    
#__getitem__   class support indexing
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
        
f = Fib()
f2 = Fib2()
print('f2[10]=',f2[10])
#'Fib' object does not support indexing
#print(f[10])


#__getattr__
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
    
print(Chain().status.user.timeline.list)


#enumerate
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique

@unique #check the duplicate value
class Weekday(Enum):  #self define enumerate
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
for name, member in Weekday.__members__.items():
    print(name, '=>', member ,',', member.value)
        