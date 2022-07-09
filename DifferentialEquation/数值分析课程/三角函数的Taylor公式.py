import numpy as np
import matplotlib.pyplot as plt

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def sin_Taylor(theta, n=10):
    sin_taylor = 0.0
    for i in range(0, n+1):
        sin_taylor =sin_taylor + (-1)**(i) * theta**(2*i+1)/factorial(2*i+1)
    return sin_taylor

if __name__ == '__main__':

    theta = np.arange(0, 8, 0.1)
    sin_eq = np.sin(theta)
    sin_taylor = sin_Taylor(theta)

    plt.plot(theta, sin_eq, ls='-', c='blue', label= 'sin(x)')
    plt.plot(theta, sin_taylor, ls='--', c='red', label='Taylor_sin(x)')
    plt.legend()
    plt.show()

