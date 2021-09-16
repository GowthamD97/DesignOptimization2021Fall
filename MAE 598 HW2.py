import numpy as np
obj = lambda x: (x[0] - 1)**2 + (x[1] + 1)**2
def grad(x):
    return [2 * (x[0] - 1), 2 * (x[1] + 1)]
eps = 1e-3
x0 = 0
k = 0
soln = [x0]
x = soln[k]
error = np.linalg.norm(grad(x))
a = 0.01
def line_search(x):
    a = 1
    d = -grad(x)
    phi = lambda a, x: obj(x) + a*0.8*grad(x).T*d
    while phi(a,x)<obj(x-a*grad(x)):
       a = 0.5*a
    return a
while error >= eps:
   #a = line_search(x)
    x = x - a*grad(x)
    soln.append(x)
    error = np.linalg.norm(grad(x))