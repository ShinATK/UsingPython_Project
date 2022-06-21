import numpy as np # 数值运算，尤其是向量化的运算方式
import sympy # 符号运算库
from data_interpolation_01.utils import interp_utils

class Lagrange_Interpolation:
    """
    拉格朗日插值
    """

    def __init__(self, x, y):
        """
        拉格朗日必要参数的初始化，及各健壮性的检测
        :param x:
        :param y:
        """
        self.x = np.array(x, dtype=np.float64)
        self.y = np.array(y, dtype=np.float64) # 类型转换， 数据结构采用array
        if len(self.x) > 1 and len(self.x) == len(self.y):
            self.n = len(self.x) # 已知离散数据点个数
        else:
            raise ValueError("插值数据（x，y）维度不匹配")

        self.polynomial = None # 最终的插值多项式，符号表示
        self.poly_coefficient = None # 最终插值多项式的系数向量，幂次从高到低
        self.coefficient_order = None # 对应多项式系数的幂次
        self.y0 = None # 所求插值点的数值（单个点或向量）

    def fit_interp(self):
        """
        核心算法：生成拉格朗日插值多项式
        :return:
        """
        # 数值运算，符号运算
        t = sympy.Symbol('t') # 定义符号变量
        self.polynomial = 0.0 # 插值多项式实例化
        for i in range(self.n):
            # 针对每个数据点，构造插值基函数
            basis_fun = self.y[i] # 插值基函数
            for j in range(i):
                basis_fun *= (t - self.x[j])/(self.x[i] - self.x[j])
            for j in range(i+1, self.n):
                basis_fun *= (t - self.x[j])/(self.x[i] - self.x[j])
            self.polynomial += basis_fun # 插值多项式累加
        # self.polynomial = sympy.simplify(self.polynomial) # 对多项式进行简化
        self.polynomial = sympy.expand(self.polynomial) # 多项式展开
        polynomial = sympy.Poly(self.polynomial, t) # 根据多项式对象
        self.poly_coefficient = polynomial.coeffs() # 获取多项式系数
        self.coefficient_order = polynomial.monoms() # 多项式对应对阶次
        # print(self.polynomial)

    def cal_interp_x0(self, x0):
        self.y0 = interp_utils.cal_interp_x0(self.polynomial, x0)
        return self.y0

    def plt_interpolation(self, x0=None, y0=None):
        """
        :param x0:
        :param y0:
        :return:
        """
        params = (self.polynomial, self.x, self.y, "Lagrange", x0, y0)
        interp_utils.plt_interpolation(params)