#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   basic.py
@Time    :   2020/11/03 21:16:17
@Author  :   HenryWu 
@Version :   1.0
@Contact :   21910069@zju.edu.cn
'''
# Start typing your code from here


import math

def quadratic(a, b, c):
    s1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    s2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    return s1,s2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
