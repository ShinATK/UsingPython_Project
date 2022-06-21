import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.optimize import curve_fit

# N = np.zeros((20, 30))+10
# A = np.zeros((10, 20))+10

# print(A)

# 建立衰减曲线
def decay_func(t, a):
    return np.exp(-a*t)

pulses5 = np.loadtxt('./decay_data/5pulses.txt')[:,1]
pulses10 = np.loadtxt('./decay_data/10pulses.txt')[:,1]
pulses25 = np.loadtxt('./decay_data/25pulses.txt')[:,1]
pulses50 = np.loadtxt('./decay_data/50pulses.txt')[:,1]
pulses75 = np.loadtxt('./decay_data/75pulses.txt')[:,1]
pulses100 = np.loadtxt('./decay_data/100pulses.txt')[:,1]

max_I = abs(min(pulses100))
data = [pulses5, pulses10, pulses25, pulses50, pulses75, pulses100]
name_list = ['pulses5', 'pulses10', 'pulses25', 'pulses50', 'pulses75', 'pulses100']
I = [min(pulses5)/max_I, min(pulses10)/max_I, min(pulses25)/max_I, min(pulses50)/max_I, min(pulses75)/max_I,min(pulses100)/max_I]

Nmatrix = {'pulses5':np.zeros((10,10))-I[0],
           'pulses10':np.zeros((10,10))-I[1],
           'pulses25':np.zeros((10, 10))-I[2],
           'pulses50':np.zeros((10,10))-I[3],
           'pulses75':np.zeros((10,10))-I[4],
           'pulses100':np.zeros((10,10))-I[5]}

for i in range(0, 6):
    for each_t in range(0, 5):
        decay_data = abs(data[i]/max_I)
        dt = 4/len(decay_data)
        t = np.arange(0, 4, dt)
        name = name_list[i]

        popt, pcov = curve_fit(decay_func, t, decay_data, maxfev=100000)
        a = popt[0]

        show_matrix = Nmatrix[name]*decay_func(each_t, a)

        fig, ax = plt.subplots()
        ax.contourf(show_matrix, vmin=0, vmax=1, cmap=cm.Blues)
        plt.axis('off')
        plt.savefig(f'./20220304output_png 单个矩阵/{name_list[i]}/{name_list[i]} {each_t}s.png', dpi=720)
        plt.show()
        np.savetxt(f'./20220304output_png 单个矩阵/{name_list[i]}/{name_list[i]}  {each_t}s.txt', show_matrix)