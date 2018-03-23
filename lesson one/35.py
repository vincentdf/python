#!/usr/bin/python
# coding=utf-8

import random
n=int(raw_input("需要多少以内多随机数"))
while True:
    x=(random.randint(1,n))
    if x==11:
        print "生成11,程序终止"
        break
    else:
        print x