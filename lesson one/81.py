#!/usr/bin/python
# coding=utf-8
"""
809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
"""
if __name__=="__main__":
    for i in range(10,100):
        if 809*i==800*i+9*i and len(str(809*i))==4 and len(str(8*i))==2 and len(str(9*i))==3:
            print "??=%d"%i
            print "809*??=809*%d=%d"%(i,(809*i))