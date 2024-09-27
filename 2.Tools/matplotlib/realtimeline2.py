#!/usr/bin/env python
#########################################################################
# File Name: realtimeline2.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Thu 26 Sep 21:00:11 2024
#########################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import itertools

# 初始化数据
x_data = []
y_data = {}
lines = {}
tags = []  # 用于存储每条曲线的标签
texts = {}  # 用于存储每条曲线的文本对象

# 创建图形
fig, ax = plt.subplots()

# 初始化函数：清空线条数据
def init():
    for line in lines.values():
        line.set_data([], [])
    return list(lines.values()) + list(texts.values())

# 更新函数：更新每帧数据
def update(frame):
    x_data.append(frame)

    # 动态生成 y 数据并更新每条曲线的数据
    for tag, line in lines.items():
        index = tags.index(tag)  # 每个标签的索引
        if len(y_data[tag]) == 0:
            y_data[tag] = []
        y_data[tag].append(np.sin(frame + (index * np.pi / len(tags))))  # 不同标签有不同相位偏移
        line.set_data(x_data, y_data[tag])

        # 在曲线的右端显示标签
        if len(x_data) > 0:
            texts[tag].set_position((x_data[-1], y_data[tag][-1]))  # 将文本放在线的终点
            texts[tag].set_text(tag)  # 设置标签内容

    # 动态调整 x 轴和 y 轴范围
    ax.set_xlim(min(x_data) - 1, max(x_data) + 1)
    ax.set_ylim(-1.5, 1.5)

    return list(lines.values()) + list(texts.values())

# 动态添加或删除曲线，并给每条曲线分配标签
def adjust_curves(new_tags):
    global tags, lines, y_data, texts

    # 如果有新标签，添加新曲线和对应的文本
    for tag in new_tags:
        if tag not in tags:
            tags.append(tag)
            line, = ax.plot([], [], lw=2)  # 创建新曲线
            lines[tag] = line
            y_data[tag] = []  # 初始化对应标签的y数据
            # 在曲线的最右端创建对应的文本标签
            texts[tag] = ax.text(0, 0, '', fontsize=9, verticalalignment='center')

    # 删除不存在的标签对应的曲线和文本
    for tag in tags[:]:
        if tag not in new_tags:
            # 移除对应的曲线
            lines[tag].remove()  # 从图中移除曲线
            texts[tag].remove()  # 从图中移除文本标签
            del lines[tag]  # 删除该标签对应的曲线对象
            del y_data[tag]  # 删除该标签对应的y数据
            del texts[tag]  # 删除该标签对应的文本对象
            tags.remove(tag)

# 创建一个无限的迭代器
frames = itertools.count(start=0, step=0.1)

# 初始化曲线（初始有两条曲线）
adjust_curves(['curve_1_old', 'curve_2_old'])

# 创建动画
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

# 动态调整曲线数量和标签
adjust_curves(['curve_1', 'curve_2', 'curve_3', 'curve_4'])  # 添加更多曲线

plt.show()
