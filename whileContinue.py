# -*- encoding: utf-8 -*-
"""
@File : whileContinue.py
@Time : 2020/1/11 20:11
@Author : Linleil
"""
tick = 0
while tick < 5:
    tick = tick+1
    if tick == 3:
        continue
    print('tick is', tick)
