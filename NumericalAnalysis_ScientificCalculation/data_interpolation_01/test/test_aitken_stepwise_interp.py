from data_interpolation_01.aitken_stepwise_interpolation import AitkenStepwiseInterpolation
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":

    # x = np.linspace(0, 2*np.pi, 10, endpoint=True) # endpoint为True表示包含最后一个点
    # y = 2*np.exp(-x)*np.sin(x)
    # x0 = np.array([np.pi/2, 2.158, 3.58, 4.784])
    y = np.loadtxt('Qs_calculate_0.1s.txt')[1:]
    y_refine = y / 1e14
    x = np.loadtxt('ET_calculate_0.1s.txt')[1:]
    x0 = np.arange(0.8, 1.3, 0.1)

    # plt.plot(x, y_refine)
    # plt.show()

    # asi_interp = AitkenStepwiseInterpolation(x, y_refine)
    # asi_interp.fit_interp()
    #
    # # print("Aitken插值方法：")
    # # print(lag_interp.polynomial)
    # # print("拉格朗日多项式系数向量和对应阶次：")
    # # print(lag_interp.poly_coefficient)
    # # print(lag_interp.coefficient_order)
    #
    # y0 = asi_interp.cal_interp_x0(x0)
    # print("所求插值点的值：", y0)
    # asi_interp.plt_interpolation(x0, y0)

