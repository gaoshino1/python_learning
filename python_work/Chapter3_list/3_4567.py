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

print("\nHey guys, there is a bigger table, we can invite more friends.")
names.insert(0, 'E')
names.insert(len(names) // 2, 'F')
names.append('G')
print("Have a dinner with", end=' ')
for n in names:
    print(n, end=' ')

print("\nIt's a broken table, now we can only invite two friends")
while len(names) > 2:
    name = names.pop()
    print("Sorry, " + name + ", maybe next time.")

for n in names:
    print("Hey " + n + ", come to the party.")

del names[0]
del names[0]
print(names)