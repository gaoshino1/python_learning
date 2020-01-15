#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n += 2
# print(L)

# L = list(range(1, 100, 2))
# print(L)

# 切片
# L = ['Micheal', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[:3])  # 同L[0:3]
# print(L[1:3])

# L = list(range(100))
# print(L[:10])
# print(L[-10:])
# print(L[:-10])
# print(L[:10:2]) # 每两个取一个
# print(L[::5])  # 所有数每5个取一个
# print(L[:])
# ## tuple的结果仍然是tuple
# T = (1, 2, 3)
# print(T[-1:])
# ## 字符串的操作结果仍是字符串
# str = 'ABCDEFG'
# print(str[:2])

# ## 作业
# def trim(s):
#     while len(s) > 0 and s[:1] == " ":
#         s = s[1:]
#     while len(s) > 0 and s[-1:] == " ":
#         s = s[:-2]
#     return s

# ## 作业测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')


# 迭代
d = {'a':1, 'b':2, 'c':3}
print(d)