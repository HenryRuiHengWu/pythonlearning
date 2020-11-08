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

from functools import reduce

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
    L2 = [ch.lower() for ch in L1 if isinstance(ch, str)]
    return L2


###杨氏三角
###把每一行看做一个list，试写一个generator，不断输出下一行的list
###生成器
'''
# 期待输出:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
    # [1, 6, 15, 20, 15, 6, 1]
    # [1, 7, 21, 35, 35, 21, 7, 1]
    # [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    if results == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
                   [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1],
                   [1, 7, 21, 35, 35, 21, 7, 1],
                   [1, 8, 28, 56, 70, 56, 28, 8, 1],
                   [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]:
        print('测试通过!')
    else:
        print('测试失败!')
        
'''


def triangles():
    l = [1]
    while True:
        yield l
        l = [0] + l + [0]
        l = [l[i] + l[i + 1] for i in range(len(l) - 1)]


###利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
###map()函数的练习
'''
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
###
'''


def normalize(name):
    return name[0].upper() + name[1:].lower()


###Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
###reduce()函数的练习
'''
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

'''


def prod(L):
    def Multiply(x, y):
        return x * y

    return reduce(Multiply, L)


###利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
###map和reduce的练习
'''
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

'''


def str2float(s):
    pass


###回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
###主要考filter
def is_palindrome(n):
    pass


def main():
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')


if __name__ == '__main__':
    main()