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

import time, functools
from functools import reduce
from enum import Enum, unique

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
    def fn(x, y):
        return x * 10 + y

    n = s.index('.')  #以.为分割
    s1 = list(map(int, s[:n]))
    s2 = list(map(int, s[n + 1:]))
    return reduce(fn, s1) + reduce(fn, s2) / (10**len(s2))


###回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
###主要考filter
'''
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
'''


def is_palindrome(n):
    return str(n) == str(n)[::
                            -1]  #str(n)[::-1]等同于str(n)[-1::-1]，输出结果为str(n)的逆序


###假设我们用一组tuple表示学生名字和成绩：
###L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
###请用sorted()对上述列表分别按名字排序：
###排序函数sorted()
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)
'''


def by_name(t):
    return t[0]


###再按成绩从高到低排序：
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_score)
print(L2)
'''


def by_score(t):
    return -t[1]


###利用闭包返回一个计数器函数，每次调用它返回递增整数：
###返回函数
'''
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
'''


def createCounter():
    num = 0

    def counter():
        nonlocal num
        num = num + 1
        return num

    return counter


###匿名函数
###请用匿名函数改造下面的代码：
'''
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

'''
#L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

###装饰器
###请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
'''
# 测试
f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
    
'''


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        res = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
        return res
    return wrapper
    

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


###类的访问限制
###请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        self.__gender = gender

'''
# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
'''


###类属性和实例属性
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

'''
# 测试:
if Student_2.count != 0:
    print('测试失败!')
else:
    bart = Student_2('Bart')
    if Student_2.count != 1:
        print('测试失败!')
    else:
        lisa = Student_2('Bart')
        if Student_2.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student_2.count)
            print('测试通过!')
'''

class Student_2(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student_2.count = Student_2.count + 1


###面向对象高级编程使用@property
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

'''
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
'''

class Screen(object):
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        
        
    @property
    def resolution(self):
        return self.height * self.width


###枚举类
#把Student的gender属性改造为枚举类型，可以避免使用字符串：

'''
# 测试:
bart = Student_3('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
'''

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student_3(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def main():

    # 测试:
    bart = Student_3('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')


if __name__ == '__main__':
    main()