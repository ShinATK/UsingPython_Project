from data_interpolation_01.lagrange_interpolation import LagrangeInterpolation
import numpy as np


if __name__ == "__main__":

    # 拉格朗日插值法测试
    # x = np.linspace(0, 2*np.pi, 10, endpoint=True) # endpoint为True表示包含最后一个点
    # y = np.sin(x)
    #
    # x0 = np.array([np.pi/2, 2.158, 3.58, 4.784])
    #
    # print(x)
    # print(y)

    # 例2：在一天24小时内，从零点开始间隔2小时测得的环境温度数据分别为12，9，9，10，24，28，27，25，20，18，15，13。推测中午13时的温度
    # x = np.linspace(0, 24, 13, endpoint=True)
    # y = np.array([12,9,9,10,18,24,28,27,25,20,18,15,13])
    # x0 = np.array([1, 10.5, 13, 18.7, 22.3])
    # 边界处的拟合度不高，阶次越高也不一定准确度越高
    # 龙格现象 龙格函数：f(x)=1/(1+x**2)

    # 阈值电压为X，打印次数为Y
    # x = np.array([-0.35, -0.2, 0, 0.2, 0.35, 0.45])
    # y = np.array([1, 2, 3, 4, 5, 6])
    # x0 = np.array([0, 0.5])

    # # 打印次数为X，阈值电压为Y
    # y = np.array([-0.35, -0.2, 0, 0.2, 0.35, 0.45])
    # x = np.array([1, 2, 3, 4, 5, 6])
    # x0 = np.array([7, 8, 9])

    y = np.loadtxt('Qs_calculate_0.1s.txt')[1:]
    y_refine = y/1e14
    x = np.loadtxt('ET_calculate_0.1s.txt')[1:]
    x0 = np.arange(0.8, 1.3, 0.1)

    lag_interp = LagrangeInterpolation(x, y_refine)
    lag_interp.fit_interp()

    # print("拉格朗日多项式：")
    # print(lag_interp.polynomial)
    # print("拉格朗日多项式系数向量和对应阶次：")
    # print(lag_interp.poly_coefficient)
    # print(lag_interp.coefficient_order)

    y0 = lag_interp.cal_interp_x0(x0)
    print("所求插值点的值：", y0)
    lag_interp.plt_interpolation(x0, y0)

