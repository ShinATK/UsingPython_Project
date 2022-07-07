import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

T = 300
kT = 0.025852 # T=300K, kT=0.025852eV

E0 = -5.0 # 单位：eV
Ef = -4.28 # 单位：eV

Nt = 1e25
sigma = 0.1 # 单位：eV

eps = 8.85e-12
eps_dielec = 3.5
eps_semi = 3.0

d_dielec = 100e-9
d_semi = 20e-9

e0 = 1.6e-19

# 聚集电子用E-Ef，空穴则为Ef-E
def Femi_Distribution(E):
    return 1/(1+np.exp((Ef-E)/kT))

def Gaussion(E, sigma, V=0):
    a = Nt/(sigma*np.sqrt(2*np.pi))
    x = -(E+V-E0)**2/(2*sigma**2)
    return a*np.exp(x)

def Intergrate_GaussFemi(E, V, sigma):
    return Femi_Distribution(E)*Gaussion(E, sigma, V=V)

def Charge_Distribution(V_list, sigma):
    n_list = []
    for V in V_list:
        n = integrate.quad(Intergrate_GaussFemi, -np.inf, np.inf, args=(V, sigma))[0]
        n_list.append(n)
    return n_list

# print(Charge_Distribution())

# E = np.arange(-10, 10, 0.01)
# plt.subplot()
# plt.plot(E, Gaussion(E, 0.05))
# plt.plot(E, Gaussion(E, 0.5))
# plt.plot(E, Gaussion(E, 5))
# plt.show()

<<<<<<< Updated upstream
# 积分后，电荷浓度图像
# V_list = np.arange(-2, 0, 0.01)
# # V_list = [0]
# CD_list = dict()
# for each in np.arange(50, 200, 50):
#     CD_list[each] = Charge_Distribution(V_list, each)
#     plt.plot(V_list, CD_list[each], label=f'sigma={each} meV')
# plt.legend()
# plt.show()

# 积分前，原函数随能级分布图
Vg = 0
plt.figure(figsize=(8, 6))
for each in [0.1, 0.01, 0.001]:
    E = np.arange(-5, -4.2, each)
    femi_func = Femi_Distribution(E)
    gauss_func = Gaussion(E, sigma, Vg)
    origin_func = Intergrate_GaussFemi(E, Vg, sigma)
    # plt.plot(E, gauss_func, label=f'gauss_func dE = {each} eV')
    # plt.plot(E, femi_func, label=f'femi_func dE = {each} eV')
    plt.plot(E, origin_func, label=f'GaussFemi dE = {each} eV')
=======
V_list = np.arange(-20, 0, 0.01)
# V_list = [0]
CD_list = dict()
for each in np.arange(50, 200, 50):
    CD_list[each] = Charge_Distribution(V_list, each)
    plt.plot(V_list, CD_list[each], label=f'sigma={each} meV')
>>>>>>> Stashed changes
plt.legend()
plt.tight_layout()
plt.show()



