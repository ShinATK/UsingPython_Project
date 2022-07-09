import numpy as np
import matplotlib.pyplot as plt

h = 0.1
k = [0, 1, 2, 3, 4, 5]

x = [each*h for each in k]
y = [np.cos(each) for each in x]

theta = np.arange(0, 0.25*np.pi, 0.001)

plt.plot(theta, np.cos(theta))
plt.scatter(x, y, marker='*', c='red')
plt.show()
