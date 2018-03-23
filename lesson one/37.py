#!/usr/bin/python
# coding=utf-8
"""
对x个数进行排序。
"""
"""import random
a=int(raw_input("请输入最小值"))
b=int(raw_input("请输入最大值"))
x=int(raw_input("对___个数进行排序\n"))
j=0
l=[]
for i in range(a,b+1):
    j+=1
    l.append(i)
if j<x:
    print "\n排序个数大于区间内的数字,请重新输入"
print sorted(random.sample(l,x))

"""  #自定义随机数中的x个数进行排序

#对输入对数字进行排序
l=[]
x=int(raw_input("需要对几个数字进行排序"))
for i in range(x):
    n=int(raw_input("输入第%d个数字"%(i+1)))
    l.append(n)
l.sort()
for i in range(x):
    if i ==0 or i==x-1:
        print l[i],
    else:
        print ">",l[i],



