import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

T = 300
kT = 0.025852 # T=300K
E0 = -5.0
Ef = -4.28
Nt = 1e20
sigma = 0.05
eps = 8.85e-12
eps_dielec = 3.5
eps_semi = 3.0
d_dielec = 100e-9 # 100nm
d_semi = 20e-9 # 20nm
e = 1.6e-19

delta_y = 0.001 # 0.001nm
Vg = -20

def Femi_Distribution(E):
    return 1/(1+np.exp((E-Ef)/kT))

def Gaussion(E, sigma, V):
    a = Nt/(sigma*np.sqrt(2*np.pi))
    x = -(E+V-E0)**2/(2*sigma**2)
    return a*np.exp(x)

def Intergrate_GaussFemi(E, V):
    return Femi_Distribution(E)*Gaussion(E, 0.5, V=V)

V = np.zeros(20000)
y = np.arange(0, 20, delta_y)
for i in range(1, 19999):
    V[i+1] = 2*V[i] - V[i-1] + ((delta_y*1e-9)**2)*(integrate.quad(Intergrate_GaussFemi, -np.inf, np.inf, args=V[i])[0])


plt.figure(figsize=(8, 6))
plt.plot(y, V)
plt.show()

