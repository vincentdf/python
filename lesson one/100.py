#! /usr/bin/python
# coding=utf-8
"""
列表转换为字典。
"""
if __name__=="__main__":
    keys=[1,2,3,4,5,6]
    values=["a","b","c","d","e","f",]
    dic=dict(zip(keys,values))
    print dic