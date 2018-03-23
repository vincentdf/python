#!/usr/bin.python
# coding=utf-8

"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""
f1 = 1
f2 = 1
f3=[1,1]
month=int(raw_input("查看第____月兔子数量\n"))
for i in range(1,month):
#    print '%12ld %12ld' % (f1,f2),
    f1=f1+f2
    f3.append(f1)
    f2=f1+f2
    f3.append(f2)
#    if i%3==0:
#       print
print f3[month-1]
