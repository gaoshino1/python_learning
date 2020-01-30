#!/usr/bin/env python3

from functools import reduce

# 高阶函数 high-order function
## 变量可以指向函数
# f = abs
# f(-10)
## 函数名也是变量
# abs = 10
# abs(-10)  # TypeError: 'int' object is not callable
## 传入参数
# def add(x, y, f):
#     return f(x) + f(y)

# print( add(5, -6, abs) )

## map/reduce
## map()函数接受两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# def f(x):
#     return x * x

# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(list(r))

# print( list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) )

## reduce() 把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
## reduc(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# def fn(x, y):
    # return x + y

# def fn(x, y):
#     return x * 10 + y

# def char2sum(s):
#     digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
#     return digits[s]

# print( reduce(fn, [1, 3, 5, 7, 9]) )
# print(reduce(fn, map(char2sum, '13579')))

# DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2sum(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2sum, s))

# print(str2int('12345'))

## 使用lamda函数进一步简化
# DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
# def char2sum(s):
#     return DIGITS[s]

# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2sum, s))

# print(str2int('1248'))

## 练习：把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
# def normalize(name):
#     return name.title()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

## 练习：Python提供的sum()函数可以接受一个list并求和，编写一个函数，可以接受一个list并利用reduce()求积
# def prod(L):
#     def product(x, y):
#         return x * y
#     return reduce(product, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

## 练习：利用map和reduce编写一个str2float函数，把字符串'123,456'转换成浮点数123.456
# def str2float(s):
#     def str2int(s):  # 也可以不定义，使用内置的int()函数
#         digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
#         return digits[s]
#     def str2integer(x, y):
#         return x * 10 + y
#     def str2decimal(x, y):
#         return x / 10 + y
#     str1, str2 = s.split('.')
#     return reduce(str2integer, map(str2int, str1)) + reduce(str2decimal, map(str2int, str2[::-1])) / 10

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

## filter
## 内建的filter()函数用于过滤序列，接收一个函数和一个序列，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# def is_odd(n):
#     return n % 2 == 1

# print( list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])) )

# def not_empty(s):
#     return s and s.strip()

# print( list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])) )

## 埃氏筛法取素数
# def _odd_iter():
#     n = 1
#     while True:
#         n += 2
#         yield n

# def _not_divisible(n):
#     return lambda x: x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter()  # 初始序列
#     while True:
#         n = next(it)  # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it)  # 构造新序列

# for x in primes():
#     print(x)

## 练习：回数是指从左向右读和从右向左读都是一样的数，利用filter()筛选出回数
def is_palindrome(n):
    

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')