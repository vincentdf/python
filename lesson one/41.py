#!/usr/bin/python
# coding=utf-8

def varfunc():
    sum=0
    print "sum=%d"%sum
    sum+=1
if __name__=="__main__":
    for i in range (3):
        varfunc()

class static:
    staticvar=5
    def varfunc(self):
        self.staticvar+=1
        print self.staticvar
print static.staticvar
a=static()
for i in range(3):
    a.varfunc()