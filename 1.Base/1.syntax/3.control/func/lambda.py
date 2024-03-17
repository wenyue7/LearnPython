#!/bin/python3
#########################################################################
# File Name: lambda.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sun Mar 17 13:40:37 2024
#########################################################################

# lambda 函数特点：
#   lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
#   lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。
# lambda 语法格式：
#   lambda arguments: expression
#   其中:
#   lambda是 Python 的关键字，用于定义 lambda 函数。
#   arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
#   expression 是一个表达式，用于计算并返回函数的结果。


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


# lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上
# 执行操作。例如：
numbers = [1, 2, 3, 4, 5]
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次
# function 函数返回值的新列表。
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]


# 使用 lambda 函数与 filter() 一起，筛选偶数：
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]
