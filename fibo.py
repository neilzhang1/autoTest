# @Time : 2022/6/2 23:44 
# encoding: utf-8
# @Author : Neil
# @File : fibo.py 
# @Software: PyCharm

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result