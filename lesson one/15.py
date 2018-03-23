#! /usr/bin/python
# coding=utf-8

"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。分组问题。
"""
def A(n):
    if n >= 90:
        grade = "A"
    elif n in range(60,90):
        grade = "B"
    else:
         grade = "C"
    print "同学分配到", grade
    C()

def C():
    x=int(raw_input("是否"))
    if x not in range(0, 2):
        print "请输入正确指令"
        exit(0)
    else:
        n = int(raw_input("分数"))
        A(n)

C()

#用两个函数互相调用实现循环