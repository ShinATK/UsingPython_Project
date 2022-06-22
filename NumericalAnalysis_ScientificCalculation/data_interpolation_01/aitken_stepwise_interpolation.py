import numpy as np # 数值运算，尤其是向量化的运算方式
import sympy # 符号运算库
from data_interpolation_01.utils import interp_utils

class AitkenStepwise_Interpolation:
    """
    艾特肯逐步插值：基本思想是k+1次插值多项式，可由两个k次插值多项式通过线性插值得到
    无精度要求，逐步推导最后一个多项式
    """

    def __init__(self, x, y):
        """
        必要参数的初始化，及各健壮性的检测
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
        self.aitken_mat = None

    def fit_interp(self):
        """
        核心算法：生成Aitken插值多项式
        :return:
        """
        # 数值运算，符号运算
        t = sympy.Symbol('t') # 定义符号变量
        self.aitken_mat = sympy.zeros(self.n, self.n + 1)
        self.aitken_mat[:, 0], self.aitken_mat[:, 1] = self.x, self.y
        poly_next = [t for _ in range(self.n)] # 用于存储下一列递推多项式
        poly_before = np.copy(self.y) # 用于存储上一列递推多项式
        for i in range(self.n-1):
            # 针对每个数据点
            for j in range(i+1, self.n):
                poly_next[j] = (poly_before[j] * (t - self.x[i]) - poly_before[i] * (t - self.x[j]))\
                               /(self.x[j] - self.x[i])
            poly_before = poly_next # 多项式的递推，下一列赋值给上一列
            self.aitken_mat[i+1:, i+2] = poly_next[i+1:]

        self.polynomial = poly_next[-1] # Aitken递推完成后的最后一个多项式，即最终结果


        # 插值多项式特征
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
        params = (self.polynomial, self.x, self.y, "Aitken Stepwise", x0, y0)
        interp_utils.plt_interpolation(params)