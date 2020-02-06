# -*- encoding: utf-8 -*-
"""
@File : list.py
@Time : 2020/1/12 11:14
@Author : Linleil
"""
import random


# randList = ['string', 1.234, 28]
# print(randList)
#
# oneToTen = list(range(11))
# print(oneToTen)
#
# randList = randList + oneToTen
# print(randList)
# print(randList[0])
# print(len(randList))
#
#
# first3 = randList[0:3]
# print(first3)
#
# print('string' in first3)
#
# print(first3.index('string'))

numList = []
M = 10
for i in range(M):
    numList.append(random.randrange(1, 10))
print(numList)
i = len(numList) - 1
while i > 0:
    j = 0
    while j < i:
        if numList[j] > numList[j+1]:
            numList[j], numList[j+1] = numList[j+1], numList[j]
        j += 1
    for k in numList:
        print(k, end=', ')
    print()
    i -= 1
