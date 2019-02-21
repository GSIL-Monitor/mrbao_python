# -*- coding: utf-8 -*-
import os
import asyncio
import threading
import time

'''
print(os.getcwd())

filelist=os.listdir(os.getcwd())
print(filelist)

for filename in filelist:
    filepath = os.path.join(os.getcwd(), filename)
    print(filepath)
    '''


def consumer(x):
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        # r='200 OK'


def product(c):
    next(c)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


# c=consumer()

# product(c)
def addlist(alist):
    for i in alist:
        yield i + 1


def foo():
    print("starting...")
    r = ''
    while True:
        res = yield r
        print("你传的消息我收到了是%s:" % res)
        r = "宝宝"


def fcc(f):
    f.send(None)
    n = 0
    while n < 10:
        n = n + 1
        print("我正在做第%s" % n)
        r = f.send(n)
        print("好的%s知道你在做第%s" % (r, n))

    f.close()


c = foo()
print(next(c))
fcc(c)


@asyncio.coroutine  # 方法一
def hello():
    print("Hello World! (%s)" % threading.currentThread())
    yield from asyncio.sleep(1)
    print("Hello Again (%s)" % threading.currentThread())


now = lambda: time.time()


async def do_some_work(x):  # 方法二
    print("wating:%s" % x)
    #await asyncio.sleep(x)  # await使用asyncio.sleep函数来模拟IO操作，携程的目的也是让这些IO操作异步化
    return "Done after{}s".format(x)


def callback(future):
    print("callback:%s" % future.result())


start = now()
coroutine1 = do_some_work(1)  # 创建携程对象
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

# task=loop.create_task(coroutine)创建任务
task=asyncio.ensure_future(coroutine1)
print(task)
tasks = [asyncio.ensure_future(coroutine1),
         asyncio.ensure_future(coroutine2),
         asyncio.ensure_future(coroutine3)]
'''
当task（也就是coroutine）执行完成的时候，就会调回调函数，并通过参数future获取携程执行的结果
'''
task.add_done_callback(callback)#添加回调函数
print(task)
loop = asyncio.get_event_loop() # 创建事件循环
loop.run_until_complete(task)  # 将携程放入事件循环中
# asyncio.wait(tasks) 也可以使用 asyncio.gather(*tasks) ,前者接受一个task列表，后者接收一堆task
#for task in tasks:
    #print("Task ret:{}".format(task.result()))
# print("task ret:{}".format(task.result()))
print("Time:%s" % (now() - start))
