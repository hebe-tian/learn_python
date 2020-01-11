# -*- encoding: utf-8 -*-
"""
@File : continueAndBreak.py
@Time : 2020/1/11 20:21
@Author : Linleil
"""
i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print('odd:', i)
    i += 1

