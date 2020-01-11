#!/usr/bin/env python3

names = ['A', 'B', 'C']
print("Have a dinner with", end=' ')
for n in names:
    print(n, end=' ')

refuse = 'B'
print("\nBecause of something urgent, " + refuse + ' cannot come to dinner')
print("But we invited D")
names.remove('B')
names.append('D')

print("Have a dinner with", end=' ')
for n in names:
    print(n, end=' ')