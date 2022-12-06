#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse

# argparse定义四个步骤
# 导入argparse包 ——import argparse
# 创建一个命令行解析器对象 ——创建 ArgumentParser() 对象
# 给解析器添加命令行参数 ——调用add_argument() 方法添加参数
# 解析命令行的参数 ——使用 parse_args() 解析添加的参数

# name or flags: 普通参数或flag参数选项参数的名称或标签，例如 epochs 或者 -e, --epochs。
#                Flag参数不需要指定参数值，只需要带有参数名即可。
# action: 命令行遇到flags参数时的动作。有两个常见的动作，store_true：设定flag参数为true；
#         store_false：设定flag参数为False。注意：如果直接运行程序，默认不读取该变量，
#         要使用必须要进行传参，例如：python try.py --epochs
# nargs: 应该读取的命令行参数个数，可以是具体的数字，或者是?号，当不指定值时对于
#        Positional argument 使用 default，对于 Optional argument 使用 const；
#        或者是 * 号，表示 0 或多个参数；或者是 + 号表示 1 或多个参数。
# default: 不指定参数时该参数的默认值。
# type: 命令行参数应该被转换成的数据类型。
# required: 是否为必选参数或可选参数。
# help: 参数的帮助信息。
# metavar： 在 usage 说明中的参数名称，对于必选参数，默认就是参数名称，对于可选参数默认是全大写的参数名称。
# dest： 解析后的参数名称，默认情况下，对于可选参数选取最长的名称，中划线转换为下划线.
# choices： 参数可允许的值的一个容器。
# const： action 和 nargs 所需要的常量值。
# store_const：表示赋值为const；
# append：将遇到的值存储成列表，也就是如果参数重复则会保存多个值;
# append_const：将参数规范中定义的一个值保存到一个列表；
# count：存储遇到的次数；此外，也可以继承 argparse.Action 自定义参数解析；

# argparse 会生成帮助和使用信息提示，并在提供无效参数时发出错误。


# 1. 定义命令行解析器对象
parser = argparse.ArgumentParser(description='Demo of argparse')

# 2. 添加命令行参数
parser.add_argument("first_number", help="first number to be added", type=int)
parser.add_argument("second_number", help="second number to be added", type=int)
parser.add_argument('-e', type=int, default=30, help="help info of -e")
parser.add_argument('--batch', type=int, default=4)
parser.add_argument('-t', '--test', type=int, default=5, help="help info of test")
parser.add_argument('-a', action='store_true', default=False, help='action test')

# 3. 从命令行中结构化解析参数
args = parser.parse_args()
print(args)
epochs = args.e
batch = args.batch
test = args.test
print()
print('show {}  {}  {}'.format(epochs, batch, test))
