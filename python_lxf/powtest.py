#!/usr/bin/env python3

def my_power(x, y):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(y, (int, float)):
        raise TypeError('bad operand type')
    return x ** y;