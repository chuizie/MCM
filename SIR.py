import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定义 Kermack-McKendrick 模型的微分方程
def kermack_mckendrick(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# 定义模型参数
beta = 0.3  # 传染率
gamma = 0.1  # 康复率

# 定义初始条件
S0 = 0.9
I0 = 0.1
R0 = 0.0
initial_conditions = [S0, I0, R0]

# 定义时间范围
t = np.linspace(0, 200, 200)

# 解微分方程
solution = odeint(kermack_mckendrick, initial_conditions, t, args=(beta, gamma))

# 绘制图形
plt.plot(t, solution[:, 0], label='易感者(S)')
plt.plot(t, solution[:, 1], label='感染者(I)')
plt.plot(t, solution[:, 2], label='康复者(R)')
plt.xlabel('时间')
plt.ylabel('比例')
plt.legend()
plt.show()
