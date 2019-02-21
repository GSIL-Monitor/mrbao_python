from functools import wraps
# 回调函数
def double(x):
    return x * 2


def quad(x):
    return x * 4


# 中间函数
def middle(k, func):
    return 1 + func(k)


def main():
    k = 1
    i = middle(k, double)
    print(i)
    l = middle(k, quad)
    print(l)

def simple(a):
    print('-->start:a= {}',format(a))
    b=yield a
    print('-->received:b={}',format(b))
    c=yield a+b
    print('-->received:c={}',format(c))

def coroutine(func):
    @wraps(func)
    def wrap(*args,**kwargs):
        gen=func(*args,**kwargs)
        next(gen)
        return gen
    return wrap

@coroutine
def averager():
    total=0.0
    count=0
    average=None
    while True:
        tern= yield average
        print('tern',format(tern))
        total+=tern
        count+=1
        average=total/count
        print(average)
a=averager()
a.send(10)

