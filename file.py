#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filepath = 'E:\python\\read.txt'
def dir_formater(dir_):
    return dir_.replace("\\", "/").replace("//", "/")
'''
try:
    f = open(dir_formater(filepath), 'r')
    print(f.read())
finally:
    if f:
        f.close()
'''
def readfile():
    with open(dir_formater(filepath),'r',encoding='gbk', errors='ignore') as f:
        #print(f.read())
        for line in f.readlines():
            print(line.strip())#删掉行尾的空白'\n'
def writefile():
    with open(dir_formater(filepath),'w') as f:
        f.write('hello everyone!')

from io import StringIO
def stingiowe():
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print(f.getvalue())

def stringiord():
    f = StringIO('hello\n world!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


from io import BytesIO
def bytesiowe():
    f = BytesIO()
    f.write('牧云'.encode('utf-8'))
    print(f.getvalue())


def bytesiord():
    f = BytesIO('人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8'))
    print(f.read())



from datetime import datetime
import os
def ospath():
    pwd = os.path.abspath('.')

    print('      Size     Last Modified  Name')
    print('------------------------------------------------------------')

    for f in os.listdir(pwd):
        fsize = os.path.getsize(f)
        mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        flag = '/' if os.path.isdir(f) else ''
        print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
    print([x for x in os.listdir('.') if os.path.isdir(x)])
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
def main():
    ospath()

if __name__ == '__main__':
    main()