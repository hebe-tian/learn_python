# -*- encoding: utf-8 -*-
"""
@File : whileBreak.py
@Time : 2020/1/11 20:13
@Author : Linleil
"""
name = ''
while True:
    print('please type your name:')
    name = input()
    if name == 'your name':
        break
print('thank you')
