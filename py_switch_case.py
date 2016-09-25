#!/usr/bin/python3
# coding: utf-8
# task from stepic
d = {'plus': lambda a, b: a + b,
     'minus': lambda a, b: a - b,
     'multiply': lambda a, b: a * b,
     'divide': lambda a, b: a // b}
x, y, z = input().split()
print(d[y](int(x), int(z)))
