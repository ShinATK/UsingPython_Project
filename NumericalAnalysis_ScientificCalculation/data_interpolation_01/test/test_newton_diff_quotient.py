
from data_interpolation_01.Newton_difference_quotient import NewtonDifferenceQuotient
import numpy as np


if __name__ == "__main__":

    x = np.linspace(0, 2*np.pi, 10, endpoint=True)
    y = np.sin(x)
    x0 = np.array([np.pi/2, 2.158, 3.58, 4.784])

    ndq = NewtonDifferenceQuotient(x=x, y=y)
    ndq.diff_quotient()
    print("牛顿差商插值差商表：")
    print(ndq.diff_quot)

