# -*- encoding: utf-8 -*-
"""
@File : forRange.py
@Time : 2020/1/11 14:16
@Author : Linleil
"""
money = 10000
rate = 0.03
for y in range(10):
    money = money * (1 + rate)
print(format(money, '.2f'))
