#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-19 14:53:57
# @Author  : jingray (lionel_jing@163.com)
# @Link    : http://www.jianshu.com/u/01fb0364467d
# @Version : $Id$

import os

class Student(object):
    name = 'Student' #类属性

    def __init__(self, name, score):
        self.__name = name #实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__score = score #实例属性

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score
        else:
            raise ValueError('bad score')

class myclass:
	def __init__(self):
		print "new object"
		self.name ="myclass"
	def setname(self,name):
		self.name = name
	def printname(self):
		print self.name
class MyNewClass(myclass):
	def setage(self,age):
		self.age = age
	def printage(self):
		print self.age
		
a=MyNewClass()
print a.name
a.setname("Apple")
a.printname()
a.setage(18)
a.printage()

jingray = Student('jingri','100')
