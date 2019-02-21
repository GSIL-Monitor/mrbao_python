# -*- coding: UTF-8 -*-
#多进程------多线程
from multiprocessing import process
import threading

def threading_(func,thread_name,*value):
    '''封装线程'''

    thread_=threading.Thread(target=func,args=value,name=thread_name)