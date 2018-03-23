#!/usr/bin/python
# coding=utf-8

""""
题目：输入一行字符，分别统计出其中英文字母，空格，数字和其它字符的个数。
程序分析：利用而语句，条件为输入的字符不为'\ n'。
"""

a=raw_input("输入一段话")
sa=0
space=0
mun=0
oth=0

if a.isalpha():
    sa+=1
elif a.isspace():
    space+=1
elif a.isnumeric():
    mun+=1
else:
    oth+=1
print ("英文%d个，空格%d个，数字%d个，其他%d个"%sa,space,mun,oth)

