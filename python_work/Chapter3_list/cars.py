#!/usr/bin/env python3

cars = ['bmw', 'audi', 'toyota', 'subaru']
# sort()永久性排序
## 正向排序
cars.sort()
print(cars)
## 反向排序
cars.sort(reverse=True)
print(cars)

# sorted()临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse-sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again:")
print(cars)

# 永久性反转列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print("\n\n" + str(cars))