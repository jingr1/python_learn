#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'kz9hxb'
'''
常用第三方库还有：
MySQL的驱动：mysql-connector-python
用于科学计算的NumPy库：numpy
用于生成文本的模板工具Jinja2
处理图像的工具库： Pillow
'''
import sys
from PIL import Image

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
        
im = Image.open('test.png')
print(im.format,im.size,im.mode)
im.thumbnail((200,100))
im.save('test_thumb.jpg','JPEG')
im = Image.open('test_thumb.jpg')
print(im.format,im.size,im.mode)

if __name__=='__main__':
    test()