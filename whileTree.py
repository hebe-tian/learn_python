# -*- encoding: utf-8 -*-
"""
@File : whileTree.py
@Time : 2020/1/11 23:20
@Author : Linleil
"""
high = int(input('high for tree:'))
spaces = high - 1
hashes = 1
while high != 0:
    # 打印空格和'#'，结尾设置为''
    for i in range(spaces):
        print(' ', end='')
    for i in range(hashes):
        print('#', end='')
    print()
    spaces = spaces - 1
    hashes = hashes + 2
    high = high - 1
