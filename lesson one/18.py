#!/usr/bin/pyton
# coding=utf-8

"""
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
"""
Tn=0
Sn=[]
a=int(raw_input("a="))
n=int(raw_input("n="))
for i in range(n):
    Tn=Tn+a
    a=a*10
    print Tn
    Sn.append(Tn)

num=reduce(lambda x,y:x+y,Sn)
print num