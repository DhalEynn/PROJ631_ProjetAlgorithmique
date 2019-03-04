# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 08:40:51 2019

@author: Admin
"""

file = open(path, "r")
lines = file.readlines()
file.close()
print(lines[0], lines[1], lines[2])
temp = []
for i in range (len(lines)):
    if (lines[i] == '\n'):
        temp.append(i)
for i in temp:
    lines.pop(i)
print(lines[0], lines[1], lines[2])