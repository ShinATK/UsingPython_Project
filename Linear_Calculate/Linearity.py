import matplotlib.pyplot as plt
import numpy as np

def Linear_Func(x):
    return 1-x

def test_Func1(x):
    return 1-x**2
def test_Func2(x):
    return 1-x**3

def error_Func(x_list, Function_Name):
    Q=0
    for each in x_list:
        Q+=abs(Linear_Func(each)-Function_Name(each))
    return Q*100/len(x_list)

if __name__ == '__main__':

    x = np.arange(0, 1, 0.01)
    # print(x)

    Q1 = error_Func(x, test_Func1)
    Q2 = error_Func(x, test_Func2)

    plt.plot(x, Linear_Func(x), '-', label=f'Linear_Func')
    plt.plot(x, test_Func1(x), '.', label=f'test_Func1 error={Q1}%')
    plt.plot(x, test_Func2(x), '.', label=f'test_Func2 error={Q2}%')
    plt.legend()
    plt.show()