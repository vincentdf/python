#!/usr/bin/python
# coding=utf-8

"""
利用ellipse 和 rectangle 画图。。　
"""

from Tkinter import *

root=Tk()
canvas=Canvas(root,width=600,height=400,bg="yellow")
canvas.pack()
x0=40
y0=40
x1=100
y1=100
for i in range(10):
    canvas.create_oval(300+x1,300-y1,200+x0,300+y0,width=1)
    canvas.create_rectangle(x0,y0,x1,y1,width=1)
    x0-=2
    y0-= 2
    x1 += 5
    y1 += 5
mainloop()
