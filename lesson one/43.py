#!/usr/bin/python
# coding=utf-8

"""模仿静态变量(static)另一案例。"""

class num:
    nnum=1
    def inc(self):
        self.nnum+=1
        print"nnum=%d"%self.nnum

if __name__ =="__main__":
    nnum=2
    inst =num()
    for i in range(3):
        nnum+=1
        print "The num =%d"%nnum
        inst.inc()