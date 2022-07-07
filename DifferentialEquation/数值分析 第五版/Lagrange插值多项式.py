import numpy as np
import sympy
import matplotlib.pyplot as plt

def Lagrnage_Interpolation(x, y):
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)

    n = len(x)
    t = sympy.Symbol('t')
    polynomial = 0.0

    for i in range(n):
        basis_func = y[i]
        for j in range(i):
            basis_func *= (t -x[j])/(x[i] -x[j])
        for j in range(i+1, n):
            basis_func *= (t -x[j])/(x[i] -x[j])
        polynomial += basis_func

    return polynomial

def cal_interp_0(polynomial, x0):

    x0 = np.array(x0, dtype=np.float64)
    n = len(x0)
    y0 = np.zeros(n)
    t = polynomial.free_symbols.pop()  # 获取插值多项式的自由变量
    for k in range(n):
        y0[k] = polynomial.evalf(subs={t: x0[k]})
    return y0

if __name__ == '__main__':
    x = [0.32, 0.34, 0.36]
    # y = [0.314567, 0.33487, 0.352274]
    y = [np.sin(each) for each in x]
    x0 = [0.3367]

    polynomial = Lagrnage_Interpolation(x, y)
    y0 = cal_interp_0(polynomial, x0)

    print('插值多项式结果：', y0)
    print('准确结果：', np.sin(x0))

    theta = np.arange(0.2, 0.5, 0.01)
    plt.plot(x, y, 'ro')
    plt.plot(theta, np.sin(theta), 'b-')
    plt.plot(x0, y0, 'g*')
    plt.show()