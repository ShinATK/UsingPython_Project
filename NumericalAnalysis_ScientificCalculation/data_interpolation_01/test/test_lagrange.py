from data_interpolation_01.lagrange_interpolation import Lagrange_Interpolation
import numpy as np

if __name__ == '__main__':
    # x = np.linspace(0, 2 * np.pi, 10, endpoint=True)
    # y = np.sin(x)

    # interpolation base points
    x = []
    y = [] # 或使用原始方程计算数据基本点
    # interpolation point
    x0 = np.array([np.pi/2, 2.158, 3.58, 4.784])

    lag_interp = Lagrange_Interpolation(x=x, y=y)
    lag_interp.fit_interp()
    print("拉格朗日多项式如下：")
    print(lag_interp.polynomial)
    print("拉格朗日多项式系数向量和对应阶次：")
    print(lag_interp.poly_coefficient)
    print(lag_interp.coefficient_order)
    # 计算插值
    y0 = lag_interp.cal_interp_x0(x0)
    print("所求插值点的值：", y0)
    # print("\n精确值是：", np.sin(x0))

    lag_interp.plt_interpolation(x0, y0)
