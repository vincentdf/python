#!/usr/bin/python
# coding=utf-8

"""
画椭圆
"""

from Tkinter import *
root=Tk()
canvas=Canvas(width=300,height=400,bg="green")
canvas.create_oval(100,100,200,200,width=1,fill="red")
canvas.pack()
mainloop()
