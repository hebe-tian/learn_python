# -*- encoding: utf-8 -*-
"""
@File : sample.py
@Time : 2020/1/12 10:29
@Author : Linleil
"""
# string = input('input')
# string = string.upper()
# listOfWords = string.split()
# for word in listOfWords:
#     print(word[0], end='')

orgin_message = input('input')
secret_message = ''

for char in orgin_message:
    if char == ' ':
        secret_message = secret_message + str(ord(char))
    else:
        secret_message = secret_message + str(ord(char)-23)

print(secret_message)
norm_string = ''

for i in range(0, len(secret_message)-1, 2):
    char_code = secret_message[i] + secret_message[i+1]
    if char_code == '32':
        code = chr(int(char_code))
    else:
        code = chr(int(char_code)+23)
    print(code)
    norm_string = norm_string + code
print(norm_string)
