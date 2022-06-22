from data_interpolation_01.aitken_stepwise_interpolation import AitkenStepwise_Interpolation
import numpy as np

if __name__ == '__main__':
    x = np.linspace(0, 2 * np.pi, 10, endpoint=True)
    y = np.sin(x)

    # # interpolation base points
    # x = np.linspace(0, 24, 13, endpoint=True)
    # y = np.array([12, 9, 9, 10, 18, 24, 28, 27, 25, 20, 18, 15, 13]) # 或使用原始方程计算数据基本点

    # interpolation point
    x0 = np.array([np.pi/2, 2.158, 3.58, 4.784])
    # x0 = np.array([1, 10.5, 13, 18.7, 22.3])

    asi_interp = AitkenStepwise_Interpolation(x=x, y=y)
    asi_interp.fit_interp()
    print("Aitken多项式如下：")
    print(asi_interp.polynomial)
    print("Aitken多项式系数向量和对应阶次：")
    print(asi_interp.poly_coefficient)
    print(asi_interp.coefficient_order)
    # 计算插值
    y0 = asi_interp.cal_interp_x0(x0)
    print("所求插值点的值：", y0)
    print("\n精确值是：", np.sin(x0))

    asi_interp.plt_interpolation(x0, y0)
