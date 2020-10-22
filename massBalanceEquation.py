# Assumptions
# Constant water density
# Constant Area
# No spillover
# constant supply pressure

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def tank(height, time, c, valve):
    density = 1000  # kg/m^3
    area = 1  # m^2

    dh_dt = (c / (density * area)) * valve
    return dh_dt


# Time spac for the simulation
ts = np.linspace(0, 10, 101)

# valve operation
c = 50.0  # valve coefficient (kg/s / %open)

# input
u = np.zeros(101)  # u - valve % open
u[21:70] = 100.0

# level initial condition
h0 = 0

# for storing results
z = np.zeros(101)

# simulate with ODEINT
for i in range(100):
    valve = u[i + 1]
    y = odeint(tank, h0, [0.0, 0.1], args=(c, valve))
    h0 = y[-1]
    z[i + 1] = h0

# plot results
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(ts, z, 'b-', linewidth=3)
plt.subplot(2, 1, 2)
plt.plot(ts,u, 'r--', linewidth=3)
plt.ylabel('Valve')
plt.xlabel('Time (s)')

plt.show()
