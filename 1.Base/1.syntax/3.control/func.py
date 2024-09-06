#!/usr/bin/env python
#########################################################################
# File Name: func.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Fri  6 Sep 18:00:17 2024
#########################################################################

# 全局变量示例
global_var = "这是一个全局变量"

def print_function_documentation(func):
    """打印函数的文档字符串"""
    print(func.__doc__)

def my_function(x, y):
    """
    这个函数接受两个参数x和y，并返回它们的和。

    参数:
    x (int): 第一个加数
    y (int): 第二个加数

    返回:
    int: x和y的和
    """
    # 局部变量示例
    local_var = x + y
    return local_var

def use_global_and_local_variables():
    """
    这个函数展示了全局变量和局部变量的使用。
    它修改了一个全局变量，并定义了一个局部变量。
    """
    global global_var  # 声明要修改全局变量
    global_var = "全局变量已被修改"
    local_var = "这是一个局部变量"
    print(f"全局变量: {global_var}")
    print(f"局部变量: {local_var}")

def example_with_lambda():
    """
    这个函数展示了lambda表达式的使用。
    Lambda表达式用于创建匿名函数对象。
    """
    # lambda表达式，接受两个参数并返回它们的和
    add = lambda x, y: x + y
    print(f"使用lambda表达式: {add(5, 3)}")

    # 另一个lambda表达式，将列表中的每个元素乘以2
    numbers = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"列表元素乘以2: {doubled}")

def main():
    # 打印函数文档
    print_function_documentation(my_function)

    # 调用函数并打印返回值
    result = my_function(5, 3)
    print(f"my_function的返回值: {result}")

    # 展示全局变量和局部变量的使用
    use_global_and_local_variables()

    # 展示lambda表达式的使用
    example_with_lambda()

if __name__ == "__main__":
    main()
