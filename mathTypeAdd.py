# -*- encoding: utf-8 -*-
"""
@File : mathTypeAdd.py
@Time : 2020/1/11 12:42
@Author : Linleil
"""
result = False
put_in = input('like \'5 * 7\'')
num1, tp, num2 = put_in.split()
num1 = int(num1)
num2 = int(num2)
if tp == '+':
    result = num1 + num2
elif tp == '-':
    result = num1 - num2
elif tp == '*':
    result = num1 * num2
elif tp == '/':
    result = num1 / num2
elif tp == '%':
    result = num1 % num2
else:
    print('wrong input')

if result:
    print(result)
