import numpy as np
import matplotlib.pyplot as plt

# 舍入误差为阶乘倍数递增
def forward(n):
    if n == 0 :
        return 1-1/np.e
    else:
        return 1-n*forward(n-1)

# ！！稳定算法！！
# 舍入误差为阶乘倒数倍数递减
def backward(n, N):
    if n == N:
        return 0.5*(1/np.e + 1)/(N+1)
    else:
        return (1-backward(n+1, N))/(n+1)

if __name__ == '__main__':

    N = 20

    I_backward = []
    for i in range(N + 1):
        I_backward.append(backward(i, N))
    plt.plot(I_backward, 'b-', label='backward')

    I_forward = []
    for i in range(N+1):
        I_forward.append(forward(i))
    plt.plot(I_forward, 'r--', label='forward')



    plt.show()