#!/usr/bin/python
# coding=utf-8
"""
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
"""

a=raw_input("输入第一个字母(大写)")
if a=="S":
    b=raw_input("请输入第二个字母")
    if b=="a":
        print "Saturday "
    elif b=="u":
        print "Sunday"
    else:
        print "请输入正确字母"
elif a=="T":
    b=raw_input("请输入第二个字母")
    if b=="u":
        print "Tuesday "
    elif b=="h":
        print "Thursday"
    else:
        print "请输入正确字母"
elif a=="M":
    print "Monday"
elif a=="W":
    print "Wednesday"
elif a=="F":
    print "Friday"
else:
    print "请输入正确字母"