import numpy as np
import matplotlib.pyplot as plt

file_name = '2022-7-4 DPPDTT 01'
origin_data = np.loadtxt(f'./Data/{file_name}/断层 {file_name}未作差.txt')
x_data = origin_data[:, 0]
y_data = origin_data[:, 1:]

plt.plot(x_data, y_data)
plt.show()