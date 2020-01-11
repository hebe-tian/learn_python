# -*- encoding: utf-8 -*-
"""
@File : moneyConverter.py
@Time : 2020/1/11 11:50
@Author : Linleil
"""
# ￥ = $ *6.74
dollar = input('how many dollar\n')
dol = int(dollar)
rmb = dol * 6.74
# '{}'.format()
print('RMB：{}'.format(rmb))
