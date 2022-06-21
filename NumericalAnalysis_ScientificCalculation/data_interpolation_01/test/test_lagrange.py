from data_interpolation_01.lagrange_interpolation import Lagrange_Interpolation

import numpy as np

if __name__ == '__main__':
    x = np.linspace(0, 2 * np.pi, 10, endpoint=True)
    y = np.sin(x)
    # print(x)
    # print(y)

    lag_interp = Lagrange_Interpolation(x=x, y=y)
    lag_interp.fit_interp()

