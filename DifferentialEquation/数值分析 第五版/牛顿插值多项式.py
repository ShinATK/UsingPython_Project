import numpy as np
import sympy
import matplotlib.pyplot as plt

def Newton_Interpolation(x, y):
    x= np.array(x, dtype=np.float64)
    y= np.array(y, dtype=np.float64)
    n = len(x)
    
    # 均差计算
    mean_differ = np.zeros(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            y[i] *= 1/(x[i] - x[j])
        mean_differ[i] += y[i]
    sum = mean_differ.sum()
    return sum

if __name__ == '__main__':

    x = [0.40, 0.55, 0.65, 0.80, 0.90, 1.05]
    y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
    n = len(x)
    mean_differ = [None for _ in x]
    for each in range(n):
        mean_differ[each] = Newton_Interpolation(x[:each+1], y[:each+1])

    print(mean_differ)