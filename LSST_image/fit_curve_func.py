from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

# 建立衰减曲线
def decay_func(t, a, b):
    return np.exp(-a*t+b)

pulses5 = np.loadtxt('./decay_data/5pulses.txt')[:,1]
pulses10 = np.loadtxt('./decay_data/10pulses.txt')[:,1]
pulses25 = np.loadtxt('./decay_data/25pulses.txt')[:,1]
pulses50 = np.loadtxt('./decay_data/50pulses.txt')[:,1]
pulses75 = np.loadtxt('./decay_data/75pulses.txt')[:,1]
pulses100 = np.loadtxt('./decay_data/100pulses.txt')[:,1]

data = [pulses5, pulses10, pulses25, pulses50, pulses75, pulses100]
name_list = ['pulses5', 'pulses10', 'pulses25', 'pulses50', 'pulses75', 'pulses100']
i = 0

for each in data:
    decay_data = abs(each/min(each))
    dt = 4/len(decay_data)
    t = np.arange(0, 4, dt)

    name = name_list[i]

    popt, pcov = curve_fit(decay_func, t, decay_data, maxfev=100000)
    a,b = popt[0:2]
    spvals=decay_func(t,a,b)
    plt.plot(t, decay_data, '*')
    plt.plot(t, spvals, 'r')
    plt.legend()
    plt.title(name+' a=%.2f, b=%.2f'%(a,b))
    plt.show()
    i = i+1

