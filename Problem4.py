import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# function that returns dy/dt
def model(z, t):
    x = z[0]
    y = z[1]
    dxdt = 3.0 * np.exp(-t)
    dydt = 3.0 - y
    return [dxdt,dydt]


# initial condition
z0 = [0,0]

# time points
t = np.linspace(0, 10)

# solve ODEs
z = odeint(model, z0, t)

x = z[:,0]
y = z[:,1]
# plot results
plt.plot(t, x, 'r-')
plt.plot(t, y, 'b:')

plt.xlabel('time')
plt.legend(['x(t)','y(t)'])
plt.show()
