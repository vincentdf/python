#! /usr/bin/python
# coding=utf-8

n=int(raw_input("要输入几个数\n"))
m=int(raw_input("要移动几位数\n"))
l=[]
for i in range(1,n+1):
    a=raw_input("请输入第%d位数"%i)
    l.append(a)
print "原数列是：",l
for j in range (m):
    l.insert(0,l.pop())

print "移动后的数列是：",l,