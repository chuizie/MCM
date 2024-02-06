#library
import numpy as np
import matplotlib.pyplot as plt

height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
    # x：柱子在x轴上的坐标。浮点数或类数组结构。注意x可以为字符串数组！
    # height：柱子的高度，即y轴上的坐标。浮点数或类数组结构。
    # width：柱子的宽度。浮点数或类数组结构。默认值为0.8。
    # bottom：柱子的基准高度。浮点数或类数组结构。默认值为0。
    # align：柱子在x轴上的对齐方式。字符串，取值范围为{'center', 'edge'}，默认为'center'。
        #'center'：x位于柱子的中心位置。
        #'edge'：x位于柱子的左侧。如果想让x位于柱子右侧，需要同时设置负width 以及align='edge'。

    #外观参数
        #color：柱子的填充色。颜色值或颜色值序列。
        #edgecolor：柱子边缘的颜色。颜色值或颜色值序列。
        #linewidth：柱子边缘宽度。浮点数或类数组。如果为0，不绘制柱子边缘。
        #tick_label：柱子的刻度标签。字符串或字符串列表。默认值为None（使用默认数值标签）。
        #**kwargs：Rectangle属性。通过关键字参数进一步设置柱子属性。
        #hatch：柱子填充符号。字符串，取值范围为 {'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}，符号可以组合，例如/+，多个重复符号，增加密度。


# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()


#example
    # plt.figure(figsize=(13,9))
    # plt.rcParams['font.family']='SimHei'

    # plt.subplot(231)
    # x=['a','b','c']
    # hight=[1,3,2]
    # plt.bar(x,hight)
    # plt.title('默认样式')
    # plt.subplot(232)
    # x=['a','b','c']
    # hight=[1,3,2]
    # plt.bar(x,hight,color='r',edgecolor='g',linewidth=2)
    # plt.title('自定义柱子颜色、边框颜色、线宽')
    # plt.subplot(233)
    # x=['a','b','c']
    # hight=[1,3,2]
    # plt.bar(x,hight,tick_label=[1,2,3])
    # plt.title('设置刻度标签')
    # plt.subplot(234)
    # x=['a','b','c']
    # hight=[1,3,2]
    # plt.bar(x,hight,hatch='/')
    # plt.title('设置柱子填充符号')
    # plt.subplot(235)
    # x=['a','b','c']
    # hight=[1,3,2]
    # plt.bar(x,hight,hatch='//')
    # plt.title('重复填充符号')
    # plt.subplot(236)
    # x=['a','b','c']
    # hight=[1,3,2]
    # plt.bar(x,hight,hatch='/+')
    # plt.title('组合填充符号')
    # plt.show()
