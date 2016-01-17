#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object): 
    def __init__(self,name,score):
        self.name = name     #public
        self.__score = score #private
        
    def print_score(self):
        print('%s: %s' % (self.name,self.__score))
        
    def get_score(self):
        return self.__score
        
    def set_score(self,score):
        if score<0 or score>100:
            raise ValueError('score must between 0~100!')
        self.__score = score
         
    def get_grade(self):
        if self.__score >=90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'
        
bart = Student('Bart Simpson',60) #instance1
lisa = Student('Lisa Simpson',92) #instance1
#print (bart.name,bart.__score) #wrong code
print(bart.name,bart.get_score())
bart.print_score()
print(bart.get_grade())
print('lisa.name=', lisa.name)


#subclass

class Animal(object):
    #__slots__ = ('name','color') #不容许定义和修改其他属性，对子类无效
    age = 5 #class attribute
    def __init__(self,name):
        self.name = name
        #self.age = 5 #object attribute
    def run(self):
        print('%s is running...'%(self.name))
    def run_twice(self):
        self.run()
        self.run()
class FlyableMixin(object):
    def fly(self):
        print('Flying')
        
class Dog(Animal):
    def run(self):
        print ('Dog is running quickly...')
    pass

class Cat(Animal):
    def __len__(self):
        return 100
    pass
    
class Bat(Animal,FlyableMixin): #multiple inheritance
    pass
   
dog = Dog('dog')
cat = Cat('cat')
dog.run()
dog.run_twice()
cat.run()
cat.run_twice()
print('the length of cat is:',len(cat))

print('dog is animal?',isinstance(dog, Animal))

print('\'a\' is a str?', isinstance('a',str))
#print('\'a\' has followed attribute and method:\n',dir('a'))
#print('instance dog has followed attribute and method:\n',dir(dog))
#print('instance cat has followed attribute and method:\n',dir(cat))

print('hasattr(dog, \'name\') =', hasattr(dog, 'name'))
print('hasattr(dog, \'age\') =', hasattr(dog, 'age')) # 有属性'age'吗？
setattr(dog, 'age', 3) # 设置一个属性'age'
print('hasattr(dog, \'age\') =', hasattr(dog, 'age')) # 有属性'age'吗？
print('getattr(dog, \'age\') =', getattr(dog, 'age')) # 获取属性'age'
print('dog.age =', dog.age) # 获取属性'age'

fish = Animal('fish') 
print(fish.age) #class attribute 5
fish.age = 3 #set instance attribute
print(fish.age) #instance attribute 3
print(Animal.age)
del fish.age #delete instance attribute
print(fish.age) #class attribute 5

# @property
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999

