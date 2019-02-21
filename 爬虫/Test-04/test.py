# -*- coding: utf-8 -*-
import os,time
from multiprocessing import Process,Pool
'''from multiprocessing import Process
base_dir=os.path.dirname(__file__)
file_dir=base_dir+'/123.txt'
f=open(file_dir,'rb')
result=f.read()
print(result)
print(file_dir)
f.close()
with open(file_dir,'wb')as a:
    a.write(b'1222222')
a.close()
print(os.getcwd())
print(os.listdir())
print(os.path.basename(__file__))
'''
'''def run_fun(name):
    print('run child process %s ....' % name)
if __name__=='__main__':
    print('parent process %s.' % os.getpid())
    p=Pool(4)
    for i in range(1,5):
        p=Process(target=run_fun,args=('123',))
        print('child process will start')
        p.start()
        p.join()
        print('child process end')
def run(name):
    print('Task %s (pid=%s) is Running....' %(name,os.getpid()))
    time.sleep(3)
    print('Task %s end' % name)
if __name__=='__main__':
    print('Current process %s'% os.getpid())
    p=Pool(processes=3)
    for i in range(5):
        p=Process(target=run,args=(i,))
    print('Wating for all subprocesses done...')
    p.start()
    p.join()
    
'''



