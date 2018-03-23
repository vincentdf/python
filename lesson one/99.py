#! /usr/bin/python
# coding=utf-8
"""
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
"""
if __name__=="__main__":
    pf=open("test1.txt","w")
    pf.write("efg")
    pf.close()
    pf = open("test2.txt","w")
    pf.write("abcd")
    pf.close()


    pf=open("test1.txt")
    a=pf.read()
    pf.close()
    pf=open("test2.txt")
    b=pf.read()
    pf.close()
    l=list(a+b)
    l.sort()
    pf=open("test3.txt","w")
    l2="".join(l)
    l2=l2.upper()
    pf.write(l2)
    pf=open("test3.txt","r")
    print pf.read()
    pf.close()