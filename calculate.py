"""
编写一个程序，该程序可以计算出给定数字和运算符的结果。
"""


def cal(a, b, c):
    """
    :param a: 第一个数字
    :param b: 第二个数字
    :param c: 运算符
    :return: 运算结果
    """
    a = float(a)
    b = float(b)
    if c == "+":
        return a + b
    if c == "-":
        return a - b
    if c == "*":
        return a * b
    if c == "/":
        return a / b
