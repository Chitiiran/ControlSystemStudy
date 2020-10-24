import sympy as sp
sp.init_printing()
x, u = sp.symbols(['x', 'u'])
dxdt = -1 * x**2 + sp.sqrt(u)

print(sp.diff(dxdt, x))
print(sp.diff(dxdt, u))



