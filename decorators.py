#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

#"""

def g(*args, **kwargs):
    print("如果打印出来我的认证就是对的啊")
    return 9
def f1(fc):
    def f1s(*args, **kwargs):
        print('Running function:', fc.__name__)
        print('Positional argument:', args)
        print('Keyword argument:', kwargs)
        result = fc(*args, **kwargs)
        print('Result:', result)
        return result
    return f1s

def f2(func):
    def f2s(*args, **kwargs):
        results = func(*args, **kwargs)
        print('Results:', results)
        return results * results
    return f2s


@f2
@f1
def add_ints(a, b):
    return a + b


k = add_ints(3,5)
print(k)
#"""
"""
def outer1(func):
    def inner1(*args,**kwargs):
        print("认证成功！")
        print("%s"% func.__name__)
        result = func(*args,**kwargs)
        print("日志添加成功")
        return result
    return inner1


def outer2(func):
    def inner2(*args,**kwargs):
        result = func(*args, **kwargs)
        print("一条欢迎信息。。。")

        print("%s" % func.__name__)
        print("一条欢送信息。。。")
        return result
    return inner2


@outer1
@outer2
def f1(name,age):

    print("%s 正在连接业务部门1数据接口......"%name)


f1("jack",18)
"""
