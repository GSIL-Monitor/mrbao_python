# -*- coding: utf-8 -*-
'''
必选参数-默认参数-可变参数-关键字参数
'''
def test(name,age,**kwargs):
    print("name:",name,"age:",age,"other:",kwargs)
test('bob',23)
test('ok',22,city='shanghai')
def keBian(name,*age):
    print("name:",name,"other:",age)
keBian('ok',123)
keBian('123',345,23,2,34,4,4,4,4,5,6,6,5,4)

def canShu(name,*age,**kwargs):
    print("name:",name,"age:",age,"kwargs:",kwargs)
canShu('22',1,11111,234454462,24442,2221)
canShu('hello',23,34,22,name1='world')
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
def func(a,b,c=1,*args,**kwargs):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kwargs)
func(1,2)
args=(1,2,3,4)
kwargs={'d':5}
func(*args,**kwargs)
'''
要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''