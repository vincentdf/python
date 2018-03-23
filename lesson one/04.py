#!/usr/bin/python
# coding=utf-8

"""题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天："""



months=(0,31,59,90,120,151,181,212,242,273,303,334)
monthone = [1,3,5,7,8,10,12]
monthtwo = [4,6,9,11]
monththree = 2
leap=0
year = int(raw_input("年\n"))
month = int(raw_input("月\n"))
day = int(raw_input("日\n"))

if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    leap = 1

#判断 闰平年

if month in monthone and day < 32:
    sum = months[month-1]+day
elif month in monthtwo and day <32 :
    sum = months[month-1]+day
elif month ==2 and day<30 and leap==1 :
    sum =months[month-1]+day
elif month == 2 and day<29 and leap!=1:
    sum =months[month-1]+day
else:
    print "输入日期有误"
#大月天数在32天以内，小月天数在31天以内，闰2月天数在30天以内，平2月天数在29天以内。其他为日期错误。

if month>2 and leap==1:
    sum+=1
#闰年 大于2月大日期加1

print sum
