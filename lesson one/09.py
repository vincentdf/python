#!/usr/bin/python
# coding=utf-8

"""
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数。
程序源代码：
"""
import time #导入time模块
dic={1:"Asasd",2:"Bas",3:"Cdasd"} #定义字典
for key,value in dict.items(dic):#dict.items(dic) 遍历并返回字典的键和值
    print key,value
    time.sleep(1) #暂停1秒
