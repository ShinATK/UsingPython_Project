import numpy as np
from data_interpolation_01.lagrange_interpolation import LagrangeInterpolation
import matplotlib.pyplot as plt

def fun(x):
    """
    Runge函数
    """
    return 1/(1+x**2)

if __name__ == "__main__":

    plt.figure(figsize=(8,6))
    for n in range(3, 12, 2):
        x = np.linspace(-5, 5, n, endpoint=True)
        y = fun(x) # 向量化运算方式，不需要循环

        lag_interp = LagrangeInterpolation(x, y)
        lag_interp.fit_interp() # 生成拉格朗日插值多项式

        xi = np.linspace(-5, 5, 100, endpoint=True)
        yi = lag_interp.cal_interp_x0(xi) # 拉格朗日插值多项式求解插值点

        plt.plot(xi, yi, lw=0.7, label='n=%d'%(n-1))

    plt.plot(xi, fun(xi), "k-", label=r"$\frac{1}{1+x^{2}}\qquad$")
    plt.xlabel("x", fontdict={"fontsize": 12})
    plt.ylabel("y", fontdict={"fontsize": 12})
    plt.title('Runge phenomenon of lagrange interpolation of different orders', fontdict={'fontsize':14})
    plt.legend()
    plt.show()