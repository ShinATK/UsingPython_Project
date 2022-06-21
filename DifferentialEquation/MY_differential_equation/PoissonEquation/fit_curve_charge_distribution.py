import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Charge_Distribution(y, a, b, c, d):

    CD = a + b*np.exp(c*y+d)

    return CD


y = np.loadtxt('cd_y.txt')/1e-3

# init
cd_init = np.loadtxt('cd init linear.txt')[:, 1]/1e19

# vg-5
cd_vg5 = np.loadtxt('cd vg-5 linear.txt')[:, 1]/1e19

# vg-20
cd_vg20 = np.loadtxt('cd vg-20 linear.txt')[:, 1]/1e19

# print(y)
# print('\n')
# print(cd_init)
# print(cd_vg5)
# print(cd_vg20)

params = {'a':0, 'b':0, 'c':0, 'd':0}

def curve_fit_cd(y, cd, name):
    err_stdev = 0.02
    cd_noise = err_stdev * np.random.normal(size=cd.size)
    cd_data = cd + cd_noise
    popt, pcov = curve_fit(Charge_Distribution, y, cd_data, maxfev=1000)#训练函数
    params['a']= popt[0]
    params['b']= popt[1]
    params['c']= popt[2]
    params['d']= popt[3]
    cd_vals=Charge_Distribution(y, params['a'], params['b'], params['c'], params['d'])
    plt.plot(y, cd, '*',label='original values')
    plt.plot(y, cd_vals, 'r',label='curve_fit values')
    plt.xlabel('y axis')
    plt.ylabel('CD axis')
    plt.legend(loc=4)
    plt.title(f'{name} curve fit')
    # plt.savefig(save_path, dpi=720)
    plt.show()
    return 0

curve_fit_cd(y, cd_vg5, 'cd_vg-5')
print(f'cd_vg-5 a={params["a"]}, b={params["b"]}, c={params["c"]}, d={params["d"]}')

curve_fit_cd(y, cd_vg20, 'cd_vg-20')
print(f'cd_vg-20 a={params["a"]}, b={params["b"]}, c={params["c"]}, d={params["d"]}')
