#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os
from multiprocessing import Pool
import time, random
#子进程要执行的函数
def run_proc(name):
    print ('Run child process %s (%s)...'% (name, os.getpid()))

def Create_Child_Proc():
    print ('Parent process %s.'% os.getpid())
    p = Process(target = run_proc, args = ('test',))
    print ('Child process will start.')
    p.start()
    p.join()  #等待子进程结束后再继续往下运行
    print ('Child process end.')

def long_time_task(name):
    print('Run task %s (%s)...'% (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print ('Task %s runs %0.2f seconds.'% (name, (end - start)))

def Creat_Pool_proc():
    print('Parent process %s.'% os.getpid())
    p = Pool(4) #默认为CPU的内核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print ('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')


import subprocess

def run_subprocess():
    print ('$ nslookup www.python.org ')
    r = subprocess.call(['nslookup','www.python.org'])
    print ('Exit code:',r)

    print ('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    output, err =p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...'% value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read %s'% os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.'% value)
        pass

def proc_communication():
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read, args = (q,))
    pw.start()
    pr.start()
    pw.join()  # 等待pw结束.
    pr.terminate()    # pr进程里是死循环，无法等待其结束，只能强行终止.


def main():
    #Create_Child_Proc()
    #Creat_Pool_proc()
    #run_subprocess()
    proc_communication()
if __name__ == '__main__':
    main()