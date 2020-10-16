import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# function that returns dy/dt
def model(z, t, u):
    x = z[0]
    y = z[1]

    dxdt = (x + u) / 2.0
    dydt = (-2*y + x) / 5.0
    dzdt = [dxdt, dydt]
    return dzdt


# initial condition
z0 = [0, 0]

# time points
n = 100
t = np.linspace(0, 10, 100)

u = np.zeros(n)
x = np.zeros(n)
y = np.zeros(n)
u[51:] = 2

for i in range(1,n):
    # solve ODEs
    tspan = [t[i-1],t[i]]
    z = odeint(model, z0, tspan, args=(u[i],))
    z0 = z[1]
    x[i] = z0[0]
    y[i] = z0[1]


# plot results
plt.plot(t, x, 'r-')
plt.plot(t, y, 'b:')
plt.plot(t,u, 'k:')

plt.xlabel('time')
plt.legend(['u(t)','x(t)', 'y(t)'])
plt.show()
