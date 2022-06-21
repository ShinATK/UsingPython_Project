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
d_dielec = 1e-7
d_semi = 2e-8
e = 1.6e-19

Vg= -20

V_0 = 0
V_d = Vg
# V_d = Vg*eps_dielec/eps_semi

V_dot_0 = 0
V_dot_d = (Vg-V_0)*eps_dielec/(eps_semi*d_dielec)
# V_dot_d = V_d/d_dielec

delta_y = -0.001

def Femi_Distribution(E):
    return 1/(1+np.exp((E-Ef)/kT))

def Gaussion(E, sigma, V):
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

def get_V_double_dot(V_original):
    return (-1/(eps*eps_semi))*(integrate.quad(Intergrate_GaussFemi, -np.inf, np.inf, args=V_original)[0])


def V(y):
    V = V_d
    V_dot = V_dot_d
    V_list = []
    for thick in np.arange(y/1e-9, 0, delta_y):
        V_double_dot = get_V_double_dot(V)
        V_dot += V_double_dot * delta_y*1e-9
        V += V_dot * delta_y*1e-9
        V_list.append(V)
    return V_list

def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace('{', '').replace('}', '')
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

if __name__ == '__main__':

    y = np.arange(d_semi/1e-9, 0, delta_y)
    V_list = V(d_semi)
    # text_save('V_list.txt', V)
    # print(V[0])
    # print(V[-1])

    n_list = Charge_Distribution(V_list)
    plt.figure(1, figsize=(8, 6))
    plt.title("n(y)")
    plt.plot(y, n_list)
    plt.show()
    plt.figure(2, figsize=(8, 6))
    plt.title("V(y)")
    plt.plot(y, V_list)
    plt.show()
