import numpy as np
import matplotlib.pyplot as plt

def origin_f(x):
    return x**2 +x +1

def de_origin_f(x):
    return 2* x +1

def newton(xk, function_name, function_dot_name, error=1e-5):
    x0_list = [xk] # 储存计算值，观察变化
    fn = function_name
    fn_dot = function_dot_name
    i = 0
    while True:
        yk = fn(xk)
        yk_dot = fn_dot(xk)
        if abs(yk) <= error or i == 50:
            break
        xk_1 = xk - yk / yk_dot
        xk = xk_1
        i += 1
        x0_list.append(xk)

    return x0_list

if __name__ == '__main__':
    xk = np.arange(-100, 100, 10)  # 递推初始值
    for each in xk:
        x0 = newton(each, origin_f, de_origin_f)

        plt.plot(x0)
    plt.show()

    x = np.arange(-10, 10, 1)
    plt.axhline(y=0, ls='--', c='red')
    plt.plot(x, origin_f(x), label='origin_function')
    plt.show()