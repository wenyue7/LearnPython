#!/bin/python3
#########################################################################
# File Name: file.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Wed May 31 11:21:31 2023
#########################################################################

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file = open("file.txt", mode='r')


lines = file.readlines()   #把全部数据文件读到一个列表lines中
print("line cnt:%d" % len(lines))
for line in lines:   #把lines中的数据逐行读取出来
    print(line)

# fileObject.seek(offset[, whence])
# offset: 开始的偏移量，也就是代表需要移动偏移的字节数
# whence: 可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
file.seek(1)
for lineidx in range(len(lines)):
    print(file.readline()) # 每次只读一行
