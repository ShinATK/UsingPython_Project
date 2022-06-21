import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

T = 300
kT = 0.025852 # T=300K, kT=0.025852eV

E0 = -5.0 # 单位：eV
Ef = -4.28 # 单位：eV

Nt = 1e27
# sigma = 0.5 # 单位：eV

eps = 8.85e-12
eps_dielec = 3.5
eps_semi = 3.0

d_dielec = 100e-9
d_semi = 20e-9

e = 1.6e-19

def Femi_Distribution(E):
    return 1/(1+np.exp((E-Ef)/kT))

def Gaussion(E, sigma, V=0):
    a = Nt/(sigma*np.sqrt(2*np.pi))
    x = -(E+V-E0)**2/(2*sigma**2)
    return a*np.exp(x)

def Intergrate_GaussFemi(E, V):
    return Femi_Distribution(E)*Gaussion(E, 0.5, V=V)

def Charge_Distribution(V_list):
    n_list = []
    for V in V_list:
        n = integrate.quad(Intergrate_GaussFemi, -np.inf, np.inf, args=V)[0]
        n_list.append(n)
    return n_list

# print(Charge_Distribution())

# E = np.arange(-10, 10, 0.01)
# plt.subplot()
# plt.plot(E, Gaussion(E, 0.05))
# plt.plot(E, Gaussion(E, 0.5))
# plt.plot(E, Gaussion(E, 5))
# plt.show()

V_list = np.arange(-20, 0, 0.01)
plt.subplot()
plt.plot(V_list, Charge_Distribution(V_list))
plt.show()
