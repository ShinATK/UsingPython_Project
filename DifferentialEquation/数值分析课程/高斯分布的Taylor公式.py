import numpy as np
import matplotlib.pyplot as plt

def factorial(n):
    return np.math.factorial(n)

def origin_function(x):
    return np.exp(-x**2)

def origin_Taylor(x, n=10):

    origin_taylor = 0.0
    for i in range(n+1):
        origin_taylor = origin_taylor+ (-1)**i * x**(2*i) / factorial(i)

    return origin_taylor

if __name__ == '__main__':

    x = np.arange(-1, 1, 0.01)
    y_origin = origin_function(x)
    y_taylor = origin_Taylor(x)

    plt.plot(x, y_origin, label='origin function')
    plt.plot(x, y_taylor, ls='--', label='origin taylor')
    plt.legend()
    plt.show()