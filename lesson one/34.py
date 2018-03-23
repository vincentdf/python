#!/usr/bin/python
# coding=utf-8
"""
题目：练习函数调用。
"""

def helloworld():
    print "hello world"

def helloworlds():
    for i in range(3):
        helloworld()
if __name__=="__main__":
    helloworlds()