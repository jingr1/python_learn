#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading, multiprocessing

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def run_thread():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)


# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def change_it_times(n):
    for i in range(100000):
        change_it(n)

lock = threading.Lock()
def change_it_withlock(n):
    for i in range(100000):
         # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

def run_2_thread():
    t1 = threading.Thread(target=change_it_withlock, args=(5,))
    t2 = threading.Thread(target=change_it_withlock, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance) # not always 0


#Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦
def dead_loop():
    x = 0
    while True:
        x = x ^ 1

def run_dead_loop():
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=dead_loop)
        t.start()
if __name__ == '__main__':
    #run_thread()
    #run_2_thread()
    run_dead_loop()