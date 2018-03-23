#! /usr/bin/python
# coding=utf-8
"""
输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
"""

if __name__ == "__main__":

    while 1:
        n = int(raw_input("请输入不为5的奇数：\n"))
        i = 1
        k = 9
        while n%2==1 and n%5!=0:
            if k%n==0 :
                print "%d个9可以被%d整除"%(len(str(k)),n),"\n",k,"/",n,"=",k/n
                exit()
            else:
                i=i*10
                k=9*i+k