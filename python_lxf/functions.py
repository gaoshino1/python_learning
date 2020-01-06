#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from powtest import my_power
import math

# 调用函数
# print(max(2, 1, 3, -5))

# print(float('12.34'))
# print(str(123))
# print(int('234'))
# print(bool(1))
# print(bool(''))

# a = abs
# print(a(-2))

# list = (255, 1000)
# for n in list:
#     print(hex(n))  # hex()返回的就是字符串


# 定义函数
# 没有retuen语句时返回的是None，reuturn None简写return
# def my_power(x, y):
#     return x ** y;

# print(pow(2, 3))
# print(my_power(2, 3))

# def nop():
#     pass  # pass语句什么都不做，可以用来作为占位符

# age = 20
# if age >= 10:
#     pass  # 如果这里缺少了pass，则会报错

# pow('1', 2)  # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# my_power('1', 2)

# print(isinstance('1', (int, float)))

# def move(x, y, step, angle = 0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# r = move(100, 100, 60, math.pi / 6)
# print(r)  # 其实返回的是一个tuple

## 练习：定义一个函数quadratic(a, b, c),接受3个参数，返回一元二次方程ax^2 + bx + c = 0的两个解
# def quadratic(a, b, c):
#     if b ** 2 - 4 * a * c >= 0:
#         x1 = ((-b) + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#         x2 = ((-b) - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
#     else:
#         return "无解"
#     return x1, x2

# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')

### 实现手动输入
# a, b, c = map(int, input('input a, b, c(使用空格分开):\n').split(' '))  # map(function, iterable, ...)  将输入的字符转为int


# 函数的参数
# def power(x):
#     return x ** x

# print(power(2))

# def power(x, n):
#     s = 1
#     while n > 0:
#         s = s * x
#         n -= 1
#     return s

# print(power(2, 3))

## 默认参数
### 必选参数必须在前，默认参数在后。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面，变化小的参数就可以作为默认参数
# def power(x, n = 2):
#     s = 1
#     while n > 0:
#         s = s * x
#         n -= 1
#     return s

# print(power(10))

# def enroll(name, gender):
#     print('name:', name)
#     print('gender:', gender)

# print(enroll('Sarah', 'F'))

# def enroll(name, gender, age = 6, city = 'Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# print(enroll('Sarah', 'F'))
# print(enroll('Bob', 'M', 23))
# print(enroll('Adam', 'F', city='Tianjin'))

## 默认参数的坑
# def add_end(L=[]):
#     L.append('END')
#     return L

# print(add_end([1, 2, 3]))  # [1, 2, 3, 'END']
# print(add_end(['x', 'y', 'z']))  # ['x', 'y', 'z', 'END']

# print(add_end())  # ['END']
# print(add_end())  # ['END', 'END']
### 个人的理解就是第一次调用时使用了默认参数，变量L指向的了['END']，到第二次执行的时候L不是指向的空列表了

# 牢记默认参数必须指向不变对象
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# print(add_end())
# print(add_end())

# 可变参数
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum += n ** 2
#     return sum

# print(calc([1, 2, 3]))
# print(calc((1, 3, 5, 7)))  # 使用普通函数需要构建List或Tuple

## 在函数内部，参数numbers接收到的是一个tuple
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum += n * n
#     return sum

# print(calc(1, 2, 3))
# print(calc())

# nums = [4, 5, 6]
# print(calc(*nums))  # *nums表示把nums这个list的所有元素作为可变参数传进去

# 关键字参数
## 关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

# print(person('Micheal', 20))
# print(person('Bob', 23, city='Beijing', address='Shandong'))

# extra = {'city': 'Beijing', 'job': 'Engineer'}
# print(person('Adam', 22, city=extra['city'], job=extra['job'])) 
# print(person('Hasenburg', 46, **extra))  # kw获得的dict是extra的一份拷贝，对kw的修改不会影响到函数外的extra

# 命名关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)

# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job关键字参数
## 命名关键字需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)

# person('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)

# # person('Jack', 24, 'Beijing', 'Engineer')  # TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
# person('Jack', 24, city='Beijing', job='Engineer')  # Jack 24 () Beijing Engineer

# 命名关键字参数可以有缺省值，从而简化调用：
# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)

# person('Jack', 24, job='Engineer')

# def person(name, age, city, job):
#     # 缺少*，city和job被视为位置参数
#     pass

# 参数组合
## 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# f1(1, 2)
# f1(1, 2, c=3)
# f1(1, 2, 3, 'a', 'b')
# f1(1, 2, 3, 'a', 'b', x=99)
# f2(1, 2, d=99, ext=None)

# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)
# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f2(*args, **kw)

# 练习
# def product(*args):
#     result = 1
#     if len(args) == 0:
#         raise TypeError("没有传如参数")
#     else:
#         for n in args:
#             result *= n
#     return result

# # 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


# 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)

# print(fact(5))
# ## 使用递归函数需要注意防止栈溢出
# print(fact(1000))

## 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以把循环看成是一种特殊的尾递归函数也是可以的
## 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式，这样，编译器或解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈桢，不会出现栈溢出的情况
# def fact(n):
#     return fact_iter(n, 1)

# def fac_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)

## 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出
## 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也一样，所以即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出

# 练习  汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')