import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# function that returns dy/dt
def model(y, t):
    if t < 10.0:
        u = 0
    else:
        u = 2
    dydt = (-y + u)/5.0
    return dydt


# initial condition
y0 = 1

# time points
t = np.linspace(0, 35)

# solve ODEs
y = odeint(model, y0, t)

# plot results
plt.plot(t, y, 'r-', linewidth=2, label='k=0.1')
# plt.plot(t, y2, 'b--', linewidth=2, label='k=0.2')
# plt.plot(t, y3, 'g:', linewidth=2, label='k=0.5')
plt.xlabel('time')
plt.ylabel('y(t)')
#plt.legend()
plt.show()
