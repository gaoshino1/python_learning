#!/usr/bin/env python3

cities = ['London', 'Tokyo', "LA", "Paris", "艾欧泽亚"]
print("The original list:")
print(cities)

print("\nThe sorted list:")
print(sorted(cities))

print("\nThe original list again:")
print(cities)

print("\nThe revese-sorted list:")
print(sorted(cities, reverse=True))

print("\nThe original list is:")
print(cities)

print("\nThe reverse list:")
cities.reverse()
print(cities) 

print("\nThe reverse-reverse list:")
cities.reverse()
print(cities)

print("\nThe sort list:")
cities.sort()
print(cities)

print("\nThe reverse-sort list:")
cities.sort(reverse=True)
print(cities)