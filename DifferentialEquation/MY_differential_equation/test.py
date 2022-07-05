import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

T = 300
kT = 0.025852 # T=300K, kT=0.025852eV

E0 = -5.0 # 单位：eV
Ef = -4.28 # 单位：eV

Nt = 1e25
sigma = 50 # 单位：meV

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
    return Femi_Distribution(E)*Gaussion(E, sigma*1e-3, V=V)

def Charge_Distribution(V_list, sigma):
    n_list = []
    for V in V_list:
        n = integrate.quad(Intergrate_GaussFemi, -np.inf, np.inf, args=(V, sigma))[0]
        n_list.append(n)
    return n_list

M, N = 100, 100
a, b = 1, 1
hx, hy = a / M, b / N
p, q = 1 / hx ** 2, 1 / hy ** 2
r = -2 * (p + q)

U = np.zeros((M - 1, M - 1))
for i in range(M - 1):
    U[i, i] = r
    if i < M - 2: U[i, i + 1] = p
    if i > 0:   U[i, i - 1] = p
V = np.diag([q] * (M - 1))
Zero_mat = np.zeros((M - 1, M - 1))

A_blc = np.empty((N - 1, N - 1), dtype=object)  # 矩阵A的分块形式
for i in range(N - 1):
    for j in range(N - 1):
        if i == j:
            A_blc[i, j] = U
        elif abs(i - j) == 1:
            A_blc[i, j] = V
        else:
            A_blc[i, j] = Zero_mat

A = np.vstack([np.hstack(A_i) for A_i in A_blc])  # 组装得到矩阵A

x_i = np.linspace(0, a, M + 1)
y_i = np.linspace(0, b, N + 1)
F = np.vstack([-2*np.pi**2 * np.sin(np.pi*x_i[1:M].reshape((M-1, 1))) * np.sin(np.pi*j) for j in y_i[1:N]])

u = np.dot(np.linalg.inv(A), F).reshape(M - 1, N - 1)
u_f = np.vstack([np.zeros((1, M + 1)),  # 最后组装边界条件得到全域的解
              np.hstack([np.zeros((N - 1, 1)), u, np.zeros((N - 1, 1))]),
              np.zeros((1, M + 1))])
plt.contourf(u_f)
plt.show()

