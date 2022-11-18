# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 01:29:01 2022

@author: gbson
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

term = [1]
def cal_term(term_):
    count = 3
    a, b, c = 1, 1, 2
    while (len(term_)<5000):
        temp = b + c
        a, b, c = b, c, b + c
        count += 1
        if len(str(temp)) > len(term_):
            term_.append(count)

cal_term(term)
t = int(input())
for _ in range(t):
    n = int(input().strip())
    print(term[n - 1])
