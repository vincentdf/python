#!/usr/bin/python
# coding=utf-8

"""
创建一个列表
"""

if __name__=="__main__":
    lis=[]
    for i in range (5):
        l=int (raw_input("please input list`s number:"))
        lis.append(l)
    lis.reverse()
    print lis