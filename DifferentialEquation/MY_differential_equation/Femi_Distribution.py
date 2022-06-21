import numpy as np
import matplotlib.pyplot as plt

kT = 0.025852 # T=300K, kT=0.025852eV

E0 = -5.0 # 单位：eV
Ef = -4.28 # 单位：eV

def Femi_Distribution(E):
    return 1/(1+np.exp((E-Ef)/kT))

t = np.arange(-100, 100, 0.1)
ax = plt.subplot()
# plt.plot(t, 1/(1+np.exp(-4*t)), color='black')
# plt.plot(t, 1/(1+np.exp(-3*t)), color='green')
# plt.plot(t, 1/(1+np.exp(-2*t)), color='yellow')
# plt.plot(t, 1/(1+np.exp(-t)), color='blue')
# plt.plot(t, 1/(1+np.exp(-0.5*t)), color='red')
plt.plot(t, 1/(1+np.exp(0*t)))
plt.plot(t, 1/(1+np.exp(0.5*t)), color='red')
plt.plot(t, 1/(1+np.exp(t)), color='blue')
plt.plot(t, 1/(1+np.exp(2*t)), color='yellow')
plt.plot(t, 1/(1+np.exp(3*t)), color='green')
plt.plot(t, 1/(1+np.exp(4*t)), color='black')
plt.show()