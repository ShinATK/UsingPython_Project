import numpy as np
import matplotlib.pyplot as plt
import sympy

class AitkenStepwiseInterpolationWithEpsilon:
    """
        Aitken逐步插值法：
            基本思想是，k+1次多项式可以由两个k次插值多项式通过线性插值得到
            带精度要求，未必逐步推导至最后一个多项式，达到精度要求即可停止递推
        """

    def __init__(self, x, y, eps=1e-3):
        """
        :param x:已知数据的x坐标点
        :param y:已知数据的y坐标点
        """

        # 将数据类型进行数据转换
        self.x = np.asarray(x, dtype=float)
        self.y = np.asarray(y, dtype=float)

        if len(self.x) > 1 and len(self.x) == len(self.y):
            self.n = len(self.x)  # 已知离散数据点的个数
        else:
            raise ValueError("插值数据（x，y）维度不匹配！")

        self.eps = eps # 插值点的精度要求
        self.y0 = None  # 所插值点的值，单个值或向量
        self.recurrence_num = [] # 存储每个插值点的递推次数

    def fit_interp(self, x0):
        """
        核心算法：根据给定插值点x0，并根据精度要求，逐步递推
        """

        # 数值运算，符号运算
        x0 = np.asarray(x0, dtype=float)
        y_0 = np.zeros(len(x0)) # 用于存储对应x0的插值
        self.recurrence_num = []

        for k in range(len(x0)): # 针对每一个所求的插值点，逐个计算
            val_next = np.zeros(self.n)  # 用于存储下一列递推多项式的值
            val_before = np.copy(self.y)  # 用于存储上一列递推多项式的值
            tol, i = 1, 0  # 初始精度要求
            for i in range(self.n - 1):
                for j in range(i + 1, self.n):
                    val_next[j] = (val_before[j] * (x0[k] - self.x[i])
                                   - val_before[i] * (x0[k] - self.x[j]))\
                                  /(self.x[j] - self.x[i])
                tol = np.abs(val_before[i+1]-val_next[i+1]) # 精度更新
                val_before[i+1:] = val_next[i+1:]  # 多项式递推，下一列赋值给上一列
                if tol <= self.eps: #满足精度要求，不再进行递推，跳出i循环
                    break
            y_0[k] = val_next[i+1] # 满足精度要求的值
            self.recurrence_num.append(i+1)
        self.y0 = y_0 # 计算完毕，赋值给类属性变量，供用户调用
        return y_0

    def plt_interpolation(self, x0, y0):
        """
        可视化插值图像与所求的插值点
        """
        plt.figure(figsize=(8, 6))
        plt.plot(self.x, self.y, "ro", label="Interpolation base points")

        xi = np.linspace(min(self.x), max(self.x), 100)  # 模拟100个值
        yi = self.fit_interp(xi)
        avg_rec = np.round(np.mean(self.recurrence_num), 2)
        plt.plot(xi, yi, "b--", label="Interpolation polynomial")
        if x0 is not None and y0 is not None:
            plt.plot(x0, y0, "g*", label="Interpolation point values")

        plt.legend()
        plt.xlabel("x", fontdict={"fontsize": 12})
        plt.ylabel("y", fontdict={"fontsize": 12})

        plt.title("Aitken interp avg_recurrence times is %.1f with eps=%.1e"
                  %(avg_rec, self.eps), fontdict={"fontsize": 13})
        plt.grid(ls=":")
        plt.show()