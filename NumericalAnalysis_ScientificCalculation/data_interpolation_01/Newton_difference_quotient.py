import numpy as np
from data_interpolation_01.utils import interp_utils
import sympy
import pandas as pd


class NewtonDifferenceQuotient:
    """
    牛顿差商（均差）插值算法
    增加插值点时，可以避免重复计算
    """
    def __init__(self, x, y):
        """
        牛顿差商插值必要参数的初始化，及各健壮性的检测
        :param x:已知数据的x坐标点
        :param y:已知数据的y坐标点
        """

        # 将数据类型进行数据转换
        self.x = np.asarray(x, dtype=float)
        self.y = np.asarray(y, dtype=float)

        if len(self.x) > 1 and len(self.x) == len(self.y):
            self.n = len(self.x) #已知离散数据点的个数
        else:
            raise ValueError("插值数据（x，y）维度不匹配！")

        self.polynomial = None  # 最终的插值多项式，符号表示
        self.poly_coefficient = None # 最终插值多项式的系数向量，幂次从高到低
        self.coefficient_order = None # 对应多项式系数的阶次
        self.y0 = None # 所插值点的值，单个值或向量
        self.diff_quot = None # 存储离散数据点的差商

    def diff_quotient(self):
        """
        计算牛顿差商（均差）
        """
        diff_quot = np.zeros((self.n, self.n)) # 存储差商
        diff_quot[:, 0] = self.y # 差商表中第一列的值，存储y值
        for j in range(1, self.n): # 按列计算
            for i in range(j, self.n): # 起始位置为差商表的对角线
                diff_quot[i, j] = (diff_quot[i, j-1] - diff_quot[i-1, j-1]) / (self.x[i] - self.x[i-j])


        self.diff_quot = pd.DataFrame(diff_quot)
        return diff_quot

    def fit_interp(self):
        """
        核心算法：生成插值多项式
        """

        # 数值运算，符号运算
        t = sympy.Symbol("t") # 定义符号变量
        self.polynomial = 0.0 # 插值多项式实例化
        for i in range(self.n):
            # 针对每个数据点，构造插值基函数
            basis_fun = self.y[i] # 插值基函数
            for j in range(i):
                basis_fun *= (t-self.x[j])/(self.x[i]-self.x[j])

            for j in range(i+1, self.n):
                basis_fun *= (t-self.x[j])/(self.x[i]-self.x[j])

            self.polynomial += basis_fun # 插值多项式相加

        # 插值多项式特征
        self.polynomial = sympy.expand(self.polynomial) # 多项式展开
        polynomial = sympy.Poly(self.polynomial, t) # 根据多项式构造多项式对象
        self.poly_coefficient = polynomial.coeffs() # 获取多项式的系数
        self.coefficient_order = polynomial.monoms() # 多项式系数对应的阶次

        # print(self.polynomial)

    def cal_interp_x0(self,x0):
        """
        计算所给定的插值点的数值，即插值
        :param x0：所求插值的x坐标
        """
        self.y0 = interp_utils.cal_interp_x0(self.polynomial, x0)
        return self.y0

    def plt_interpolation(self, x0=None, y0=None):
        """
        可视化插值图像与所求的插值点
        """
        params = (self.polynomial, self.x, self.y, "Lagrange", x0, y0)
        interp_utils.plt_interpolation(params)