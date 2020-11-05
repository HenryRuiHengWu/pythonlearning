#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   TowerofHanoi.py
@Time    :   2020/11/04 17:08:31
@Author  :   HenryWu 
@Version :   1.0
@Contact :   21910069@zju.edu.cn
'''
# Start typing your code from here


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


def main():
    move(3, 'A', 'B', 'C')


if __name__ == '__main__':
    main()
