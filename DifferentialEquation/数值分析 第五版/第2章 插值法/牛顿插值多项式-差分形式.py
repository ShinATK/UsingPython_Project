# 向前差分，向后差分，中心差分

import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

def Newton_Difference(x, y):
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    t = sy.Symbol('t')

    polynomial = 0

    n = len(y)

    # 储存各阶差分
    newton_difference = dict()

    for i in range(0, n):
        if i == 0:
            newton_difference[f'{i}'] = y # 零阶差分即为原函数数值
        else:
            newton_difference[f'{i}'] = [None for _ in range(n-i)] # 声明各阶差分列表长度
            newton_difference[f'{i}'] = \
                [newton_difference[f'{i-1}'][j+1]-newton_difference[f'{i-1}'][j] for j in range(n-i)]

    result = [1 for _ in y]
    # 牛顿前插公式
    for i in range(n):
        result[i] *= np.math.factorial(i)
        for j in range(i):
            result[i] *= (t - j)
        polynomial += result[i] * newton_difference[f"{i}"][0]

    return polynomial

def cal_interp_0(polynomial, x0):

    x0 = np.array(x0, dtype=np.float64)
    n = len(x0)
    y0 = np.zeros(n)

    # 获取插值多项式的自由变量
    t = polynomial.free_symbols.pop()
    for k in range(n):
        y0[k] = polynomial.evalf(subs={t: x0[k]})
    return y0

if __name__ == '__main__':

    h = 0.1
    k = [0, 1, 2, 3, 4, 5]

    x = [each*h for each in k]
    y = [np.cos(each) for each in x]
    #
    # theta = np.arange(0, 0.25*np.pi, 0.001)
    #
    # plt.plot(theta, np.cos(theta))
    # plt.scatter(x, y, marker='*', c='red')
    # plt.show()

    polynomial = Newton_Difference(x, y)
    print(polynomial)

    x0 = 0.033
    t = (x0-x[0])/h
    y0 = cal_interp_0(polynomial, [t])
    print(y0)
    print(np.cos(x0))