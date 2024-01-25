import matplotlib.pyplot as plt
import numpy as np
 
plt.rcParams['font.sans-serif']=['SimHei']     #显示中文
plt.rcParams['axes.unicode_minus']=False       #正常显示负号
 
def radar_map(data, label, cls):
    # 设置雷达图的角度，用于平分切开一个圆面
    n = len(label)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
 
    # 将折线图形进行封闭操作
    angle = np.concatenate((angles, [angles[0]]))
    data = np.concatenate((data, data[:, None, 0]), axis=1)
    label = np.concatenate((label, [label[0]]))
 
    # 绘图
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, polar=True)  # 参数polar, 以极坐标的形式绘制图形
 
    # 画线
    for i in range(len(data)):
        ax.plot(angle, data[i], 'o-', linewidth=2, label=cls[i])
        # ax.fill(angle, data[i], alpha=0.7)  # 填充底色
 
    ax.set_thetagrids(angle * 180 / np.pi, label)  # 添加属性标签
    ax.set_ylim(0, 100)  # 设置极轴的区间范围
    ax.set_theta_zero_location('N')  # 设置极坐标的起点（即0°）在正北方向，即相当于坐标轴逆时针旋转90°
    # ax.spines['polar'].set_visible(False)  # 不显示极坐标最外圈的圆
    # ax.set_yticks([])  # 不显示坐标间隔
    plt.grid(True, c='gray', linestyle='--')  # 设置网格线样式
    plt.title('示例', fontsize=12)  # 添加标题
    plt.legend(loc='lower right', bbox_to_anchor=(0.0, 0.0))  # 设置图例的位置，在画布外
    plt.show()
 
if __name__ == '__main__':
    # 要展示的指标
    label = np.array(['AA', 'OA', 'kappa', "PA", "UA"])
 
    # 每个数据的名字
    cls = np.array(['A_1', 'A_2', 'A_3', "A_4", "A_5"])
 
    # 数据
    data = np.array([[92.3, 95.1, 90.2, 65.2, 75.1],
                     [50.3, 65.2, 80.4, 90.2, 77.6],
                     [45.2, 55.3, 86.2, 45.2, 88.3],
                     [85.2, 65.3, 98.2, 47.2, 58.6],
                     [88.5, 95.3, 65.2, 84.5, 78.6]])
 
    # 绘制雷达图
    radar_map(data, label, cls)
