#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable  # 3.9后不再支持
from collections import Iterator
import os


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
# d = {'a':1, 'b':2, 'c':3}
# print(d)
# for key in d:
#     print(key)

# for value in d.values():
#     print(value)

# for k, v in d.items():
#     print(k, '=', v)

# for ch in 'ABC':
#     print(ch)

## 使用collections模块的Iterable类型判断一个对象是否是可迭代对象
# print( isinstance('abc', Iterable) )
# print( isinstance([1, 2, 3], Iterable) )
# print( isinstance(123, Iterable) )

## python内置的enumerate函数可以把一个list变成索引-元素对，实现类似Java中的下标循环
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, '=', value)

## for循环里同时引用两个变量
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)

## 练习
# def findMinAndMax(L):
#     min = max = None
#     if len(L) == 0:
#         pass
#     else:
#         min = max = L[0]
#         for value in L:
#             if value < min:
#                 min = value
#             elif value > max:
#                 max = value
#     return (min, max)
# ## 练习测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!1')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!2')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!3')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!4')
# else:
#     print('测试成功!')


# 列表生成式
# print(list(range(1, 11)))
# ## 生成 [1x1, 2x2, 3x3, ..., 10x10]
# L = []
# for x in range(1, 10):
#     L.append(x * x)
# print(L)

# L1 = [x * x for x in range(1, 10)]
# print(L1)

# L2 = [x * x for x in range(1, 10) if x % 2 == 0]
# print(L2)

# L3 = [m + n for m in 'ABC' for n in 'XYZ']
# print(L3)

# ## 运用os模块，列出当前目录下的所有文件和目录名(包含隐藏文件及目录)
# L4 = [d for d in os.listdir('/home/gaoshi/')]
# print(L4)

# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# print([k + ' = ' + v for k, v in d.items()])

# L5 = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L5])

# ## 练习
# L = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L if isinstance(s, str)]
# ## 测试:
# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

# 生成器
# L = [x * x for x in range(10)]  # 列表生成式
# print(L)  # L是一个列表

# g = (x * x for x in range(10))  # 生成器
# print(g)  # g是一个生成器
# print(next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g))
# for n in g:
#     print(n)

# ## 如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         # print(b)
#         yield b  # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#         a, b = b, a + b
#         n += 1
#     return 'done'

# # print(fib(5))
# f = fib(5)
# print(f)
# # for x in f:
#     # print(x)  # 这样的话拿不到返回的'done'，如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

# while True:
#     try:
#         x = next(f)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator returns value:', e.value)
#         break

# ## generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行。遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o = odd()
# for x in o:
#     print(x)

# ## 练习：杨辉三角形（抄作业）
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]

# ## 测试
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break

# for t in results:
#     print(t)

# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# 迭代器
## 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterable
print( isinstance((x for x in range(10)), Iterator) )
print( isinstance([], Iterator) )
print( isinstance({}, Iterator) )
print( isinstance('abc', Iterator) )

print( isinstance(iter([]), Iterator) )
print( isinstance(iter('abc'), Iterator) )
## 解释：为什么list、dict、str等数据类型不是Iterator
## 
## 因为Python的Iterator对象表示的是一个数据流，
## Iterator对象可以被next()函数调用并不断返回下一个数据，
## 直到没有数据时抛出StopIteration错误。
## 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
## 只能不断通过next()函数实现按需计算下一个数据，
## 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

## 凡是可作用于for循环的对象都是Iterable类型
## 凡是可作用于next()函数的都是Iterator类型，它们表示的是一个惰性绩的序列