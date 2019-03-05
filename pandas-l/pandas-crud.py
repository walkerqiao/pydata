#!/usr/bin/env python
# coding=utf-8
# reference from https://www.jianshu.com/p/ac563d84e006

import numpy as np
import pandas as pd

# 1、DataFrame的创建方式

# 1.1 通过二维数组创建
arr = [['张伊曼', 100], ['张诗诗', 90], ['张巧玲', 80]]
df0 = pd.DataFrame(arr)

print("df0=====================")
print(df0)

print("df0.index=====================")
print(df0.index)

print("df0.columns=====================")
print(df0.columns)

print("df0.dtypes=====================")
print(df0.dtypes)

print("df0.values=====================")
print(df0.values)

print("更换index、columns的值===========================")
df0 = pd.DataFrame(arr,index=['第一行','第二行','第三行'],columns=['name','分数'])
#df0.index = ['第一行', '第二行', '第三行']  #等同于以这种方式更改index的值
print(df0)

# 1.2 通过字典创建
dict0 = {
    'android': [90, 80, 60],
    'java': [99, 78, 89],
    'python': [98, 82, 85],
    'c': 80
}
df1 = pd.DataFrame(dict0)
print("df1===========================")
print(df1)


# 3、DataFrame的值的获取
dict0 = {
    'android': [90, 80, 60],
    'java': [99, 78, 89],
    'python': [98, 82, 85],
    'c': 80
}
df0 = pd.DataFrame(dict0)
df0.index = ['张伊曼', '张诗诗', '张巧玲']
print("df0===========================")
print(df0)

# print(df0['张伊曼']['android'])  #注意：先行后列获取会报错

print("单个的值的获取===========================")
print(df0['android']['张伊曼'])    #通过这种方式获取单个的值

print("一行值的获取===========================")
print(df0.ix[0])

print("多行值的获取===========================")
print(df0.ix[:2])

print("任意多行值的获取===========================")
print(df0.ix[:2, :2])

print("一列值的获取===========================")
print(df0['android'])

# 4、 修改值  新增列 新增行
dict0 = {
    'android': [90, 80, 60],
    'java': [99, 78, 89],
    'python': [98, 82, 85],
    'c': 80
}
df0 = pd.DataFrame(dict0)
df0.index = ['张伊曼', '张诗诗', '张巧玲']
print("df0===========================")
print(df0)

print("修改单个值===========================")
df0['android']['张伊曼'] = 100
print(df0)

print("修改一列值===========================")
df0['android'] = [100, 100, 100]
print(df0)

print("新增列===========================")
df0['c++'] = np.nan
print(df0)

print("新增行===========================")
df0.ix['思思'] = np.nan
print(df0)
