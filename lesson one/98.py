#! /usr/bin/python
# coding=utf-8
"""
从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
"""
if __name__=="__main__":
    fp= open("test.txt","w")
    string=raw_input("input string\n")
    string=string.upper()
    fp.write(string)
    fp= open ("test.txt","r")
    print fp.read()
    fp.close()