#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   trim.py
@Time    :   2020/11/04 20:54:33
@Author  :   HenryWu 
@Version :   1.0
@Contact :   21910069@zju.edu.cn
'''
# Start typing your code from here

###切片的教程作业
###利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法


def trim(s):
    while s[:1] == " ":
        s = s[1:]

    while s[-1:] == " ":
        s = s[:-1]

    return s


###迭代（c语言的遍历数组）
def findMinAndMax(L):
    if L == []:
        return (None, None)
    max = L[0]
    min = L[0]
    for value in L[1:]:
        if value > max:
            max = value

        if value < min:
            min = value
    return (min, max)

###使用内建的isinstance函数可以判断一个变量是不是字符串
###请修改列表生成式，通过添加if语句保证列表生成式能正确地执行
###作用是取字符串，转换成小写
def List_Comprehensions():
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [ch.lower() for ch in L1 if isinstance(ch,str)]
    return L2


def main():
    # 测试:
    L2=List_Comprehensions()
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
        print('测试通过!')
    else:
        print('测试失败!')


if __name__ == '__main__':
    main()