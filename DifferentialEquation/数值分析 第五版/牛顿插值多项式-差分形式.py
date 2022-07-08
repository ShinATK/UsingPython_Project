import numpy as np
import sympy
import matplotlib.pyplot as plt

def Mean_Differ(x, y):
    x= np.array(x, dtype=np.float64)
    y= np.array(y, dtype=np.float64)
    n = len(x)

    # 均差计算
    mean_differ = np.zeros(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            y[i] *= 1/(x[i] - x[j])
        mean_differ[i] += y[i]
    sum = mean_differ.sum()

    return sum

def Newton_Interpolation(x, y, mean_differ, k):
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    n = len(x)
    t = sympy. Symbol('t')
    result = mean_differ

    # 牛顿插值迭代公式
    for i in range(n):
        for j in range(i):
            result[i] *= (t - x[j])
    Polynomial = 0.0
    # 各阶差分储存在列表result中
    for each in result[:k]:
        Polynomial += each

    return Polynomial

def cal_interp_0(polynomial, x0):

    x0 = np.array(x0, dtype=np.float64)
    y0 = np.zeros(n)

    # 获取插值多项式的自由变量
    t = polynomial.free_symbols.pop()
    for k in range(n):
        y0[k] = polynomial.evalf(subs={t: x0[k]})
    return y0

if __name__ == '__main__':

    x = [0.40, 0.55, 0.65, 0.80, 0.90, 1.05]
    y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
    n = len(x)
    mean_differ = [None for _ in x]
    for each in range(n):
        mean_differ[each] = Mean_Differ(x[:each+1], y[:each+1])
    print(mean_differ)


    x0 = [0.596]
    polynomial = Newton_Interpolation(x, y, mean_differ, k=4)
    result = cal_interp_0(polynomial, x0)
    print(result)
    print(sympy.factor(mean_differ)) # 分解因式