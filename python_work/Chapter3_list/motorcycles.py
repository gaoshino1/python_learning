#!/usr/bin/env python3

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 添加元素
## 末尾添加元素
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

## 插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 删除元素
## 使用del语句删除元素，无返回值
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

## 使用pop()方法删除末尾元素，有返回值
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owns = motorcycles.pop()
print("The last motorcycle I owner was a " + last_owns.title() + ".")

## 弹出任何位置的元素，有返回值
first_owned = motorcycles.pop(0)
print("The first motorcycle I owner was a " + first_owned.title() + ".")

## 根据值删除元素remove(),只删除第一个指定的值，如果一个值多次出现考虑使用循环remove()
motorcycles = ['honda', 'suzuki', 'ducati', 'yamaha']
motorcycles.remove('suzuki')
print(removed_motorcycle)