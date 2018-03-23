#! usr/bin/python
# coding=utf-8
import urllib.request
"""x=input("please input url")
y=input("please input filename")
filename=urllib.request.urlretrieve(x,y)
urllib.request.urlcleamup()"""
file=urllib.request.urlopen("http://www.baidu.com")
print (file.info())
data=file.read(),m
dataline=file.readlines()
##print (data)
print(dataline)
fhandle=open("1.html","wb")
fhandle.write(data)
fhandle.close()