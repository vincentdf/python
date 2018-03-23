#! /usr/bin/python
# coding=utf-8

"""进制之间的转化"""

if __name__=="__main__":
    n=raw_input("请输入一个八进制")
    print("输入的数据是%s"%n)
    print("转化成二进制是：%s"%bin(int(n,8)))
    print("转化成十进制是：%s"%int(n,8))
    print("转化成十六进制是%s"%hex(int(n,8)))