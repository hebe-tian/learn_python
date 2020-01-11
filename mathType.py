# -*- encoding: utf-8 -*-
"""
@File : mathType.py
@Time : 2020/1/11 11:58
@Author : Linleil
"""
num1, num2 = input('2 num:').split()
num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
dif = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
print(sum, dif, product, quotient, remainder)
