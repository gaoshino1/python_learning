#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据类型和变量
 
# print('\\\t\\')
# print(r'\\\t\\')
# print('''First
# Second
# Third''')
# print(r'''\\\t
# \n''')

# print(10 / 3)
# print(10 // 3)
# print(10 % 3)


# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# 字符串和编码

# # ord()获取字符的整数表示，chr()函数把编码转换为对应的字符
# print("‘中’的整数表示为：", ord('中'))
# print("20013对应的字符为：", chr(20013))
# # 使用十六进制表示
# print('\u4e2d\u6587')


# # 由于Python的字符串是str类型，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes，bytes的每个字符只占用一个字节
# x = b'ABC'

# # 以Unicode表示的str通过encode()方法可以编码为指定的bytes，在bytes中，无法显示为ASCII字符的字节，用\x##显示
# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))  # 会报错，编码不支持

# # 如果从网络或磁盘上读取了字节流，那么读到的数据就是bytes，需要用decode()方法变为str
# print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# # 如果bytes中包含无法解码的字节，decode()方法会报错，如果只有一小部分无效的字节，可以传入errors = 'ignore'忽略错误的字节
# print(b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8'))  # 报错
# print(b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8', errors='ignore'))


# # len()计算str的字符个数，计算bytes的字节数
# print(len('ABC'))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# print(len('中文'.encode('utf-8')))

# 格式化

# print('Hello, %s' % 'world')
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
# print('growth rate: %d %%' % 7)

# print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
r = (85 - 72) / 72 * 100
print('小明的成绩从72到85，成绩提升了: %2.1f%%' % r)
print('小明的成绩从72到85，成绩提升了: {0:2.1f}%'.format(r))

# 使用List和tuple
## List
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print("长度:", len(classmates))
print(classmates[0], classmates[1], classmates[-1])
# print(classmates[3])  # IndexError: list index out of range
# print(classmates[-4])  # IndexError: list index out of range
# list是一个可变的有序表
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')  # 在指定索引位插入
print(classmates)
# pop()删除末尾元素
classmates.pop()
print(classmates)
# pop(index) 删除指定位置的元素
classmates.pop(1)
print(classmates)
# 直接替换
classmates[1] = 'Sarah'
print(classmates)

s = ['Python', 'Java', ['asp', 'php'], 'scheme']
print("长度:", len(s))


## Tuple  有序列表，一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 初始化空tuple
t = ()
# 初始化一个元素的tuple，必须要带逗号，否则被当成数字1，因为规定这种情况下是按小括号计算的
t = (1,)
# 虽说不能修改，但是！ 看下面   tuple中的一个元素是list，看似是tuple的元素变了其实变的是list的元素
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])


# 条件判断
age = 20
if age >= 18:
    print('adult')
elif age >= 14:
    print('teenager')
else:
    print('you are just a kid')
# 只要是非零数值、非空字符串、非空list等，就判断为true，否则为false

# input
birth = input('birth: ')
birth = int(birth)
if birth < 2000:  # TypeError: '<' not supported between instances of 'str' and 'int'
    print('90后')
else:
    print('00后')