#! /usr/bin/python
# coding=utf-8
"""
字符串排序。
"""

if __name__=="__main__":
    list=[]
    for i in range(3):
        l=raw_input("input string:\n")
        list.append(l)
    print list
    list.sort()
    print list
    for i in range(3):
        print list[i],