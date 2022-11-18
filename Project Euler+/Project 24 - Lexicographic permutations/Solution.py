# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 01:02:50 2022

@author: gbson
"""
#Idea: Factorial number system
#https://en.wikipedia.org/wiki/Factorial_number_system

# Enter your code here. Read input from STDIN. Print output to STDOUT
def fac_to_remainder(n):
    remainder = [0] * 13
    i = 1
    while (n != 0):
        remainder[13 - i] = n % i
        n = n // i
        i += 1
    return remainder

def solve(n):
    string = list("abcdefghijklm")
    out = ""
    remainder = fac_to_remainder(n - 1)
    for i in remainder:
        out += string.pop(i)
    return out
        
for _ in range(int(input())):
    n = int(input().strip())
    print(solve(n))
