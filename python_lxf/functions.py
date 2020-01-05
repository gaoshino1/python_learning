#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from powtest import my_power
import math

# 调用函数
print(max(2, 1, 3, -5))

print(float('12.34'))
print(str(123))
print(int('234'))
print(bool(1))
print(bool(''))

a = abs
print(a(-2))

list = (255, 1000)
for n in list:
    print(hex(n))  # hex()返回的就是字符串


# 定义函数
# 没有retuen语句时返回的是None，reuturn None简写return
# def my_power(x, y):
#     return x ** y;

print(pow(2, 3))
print(my_power(2, 3))

def nop():
    pass  # pass语句什么都不做，可以用来作为占位符

age = 20
if age >= 10:
    pass  # 如果这里缺少了pass，则会报错

# pow('1', 2)  # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# my_power('1', 2)

# print(isinstance('1', (int, float)))

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)  # 其实返回的是一个tuple

## 练习：定义一个函数quadratic(a, b, c),接受3个参数，返回一元二次方程ax^2 + bx + c = 0的两个解
def quadratic(a, b, c):
    if b ** 2 - 4 * a * c >= 0:
        x1 = ((-b) + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = ((-b) - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    else:
        return "无解"
    return x1, x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

### 实现手动输入
a, b, c = map(int, input('input a, b, c(使用空格分开):\n').split(' '))  # map(function, iterable, ...)  将输入的字符转为int