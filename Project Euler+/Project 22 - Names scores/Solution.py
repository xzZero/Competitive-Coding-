# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:09:26 2022

@author: gbson
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def letter_sum(line):
    sum_ = 0
    for l in line:
        sum_ += ord(l)
    return sum_ - (64 * len(line))

def insert_namelist(names_):
    name_l = {}
    for i in range(len(names_)):
        name_l[names[i]] = letter_sum(names_[i]) * (i + 1)
    return name_l

names = []
name_list = {}
for i in range(int(input())):
    names.append(input().strip().upper())
names.sort()
name_list = insert_namelist(names)

for _ in range(int(input())):
    print(name_list[input().strip().upper()])
