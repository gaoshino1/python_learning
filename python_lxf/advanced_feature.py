#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable


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
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, '=', v)

for ch in 'ABC':
    print(ch)

## 使用collections模块的Iterable类型判断一个对象是否是可迭代对象
print( isinstance('abc', Iterable) )
print( isinstance([1, 2, 3], Iterable) )
print( isinstance(123, Iterable) )

## python内置的enumerate函数可以把一个list变成索引-元素对，实现类似Java中的下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, '=', value)

## for循环里同时引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

## 练习
def findMinAndMax(L):
    min = 0
    max = 0
    if len(L) == 0:
        min = None
        max = None
    elif len(L) == 1:
        min = L[0]
        max = L[0]
    else:
        min = L[0]
        max = L[0]
        for value in L:
            if value < min:
                min = value
            elif value > max:
                max = value
    return (min, max)
## 练习测试
if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')