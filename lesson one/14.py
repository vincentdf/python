#!/usr/bin/python
# coding=utf-8
"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""

n=int(raw_input("输入一个正整数\n"))
print "%d ="%n,
if n<=0 or not isinstance(n,int):
    print "请输入一个正整数"
    exit(0)  #判断是否是正整数，如果不是。跳出程序  exit(0)
elif n in [1,2]:
    print n  #如果你n=1，直接输出n
while n not in [1,2]:
    for i in xrange(2,n+1):
        if n%i==0:  #是否为最小素数
            n=n/i   #如果是最小素数那么，n等于商
            if n==1:
                print i  #当n=i 时候直接输出n
            else:
                print "{} *".format(i),
            break  #跳出for循环，重新开始第一步