#! /usr/bin/python
# coding=utf-8

"""求0—7所能组成的奇数个数。
解析：
一位数的时候，有1，3，5，7。共4个
二位数的时候，十位上的7个数，共7x4个奇数。
三位数的时候，百位上有7个数，十位上有8个数，共7x8x4个奇数
四位数的时候，千位上有7个数，百位和十位上各有8个数，共7x8x8x4个奇数。
。。。。。
"""

if __name__=="__main__":
    sum=4
    s=0
    for i in range (1,9):
        if i >2:
            sum *=8
        elif i==2:
            sum*=7
        s=s+sum

    print s