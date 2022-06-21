from data_interpolation_01.aitken_stepwise_interp_eps import AitkenStepwiseInterpolationWithEpsilon
import numpy as np


if __name__ == "__main__":

    # x = np.linspace(0, 2*np.pi, 10, endpoint=True) # endpoint为True表示包含最后一个点
    #     # y = np.sin(x)
    #     # x0 = np.array([np.pi/2, 2.158, 3.58, 4.784])

    x = np.array([-0.35, -0.2, 0, 0.35, 0.35, 0.45])
    y = np.array([3, 6, 9, 12, 15, 18])
    x0 = np.array([-0.5, 0, 0.5])

    # y = np.loadtxt('Vg(-40 4).txt')
    # x = np.arange(-40, 5, 0.5)
    # x0 = np.array([7, 8, 9])

    asi_interp = AitkenStepwiseInterpolationWithEpsilon(x, y)
    y0 = asi_interp.fit_interp(x0)

    print("Aitken带精度要求，所求插值点的值：", y0)
    print("每个点递推次数为：", asi_interp.recurrence_num)
    asi_interp.plt_interpolation(x0, y0)

