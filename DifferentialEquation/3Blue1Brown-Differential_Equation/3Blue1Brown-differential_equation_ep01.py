import numpy as np
import matplotlib.pyplot as plt

# Physical constants
g = 9.8
L = 2
mu = 0.1

THETA_0 = np.pi/3   # 60 degrees
THETA_DOT_0 = 0     # No initial angular velocity

# Definition of ODE
def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g/L) * np.sin(theta)

# Solution to the differential equation
def theta(t, delta_t, THETA_0, THETA_DOT_0):
    # Initialize changing values
    theta = THETA_0
    theta_dot = THETA_DOT_0
    # delta_t = 0.01 # Some time stop
    theta_list = []
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(
            theta, theta_dot
        )
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
        theta_list.append(theta)
    return theta_list

if __name__ == '__main__':

    theta_0 = THETA_0
    theta_dot_0 = THETA_DOT_0
    final_t = 100
    delta_t = 0.01

    t = np.arange(0, final_t, delta_t)
    plt.figure(figsize=(8, 6))
    plt.plot(t, theta(final_t, delta_t, theta_0, theta_dot_0))
    plt.show()