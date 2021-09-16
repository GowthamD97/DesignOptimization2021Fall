import numpy as np
import matplotlib.pyplot as plt
from line_search_bt import *

x = np.array([1, 1])
convergence_criteria = .001
conv = 1
alpha = 1
error = 1
err = []
sol = []

xstar = [-0.14247862, 0.78547484]


def func(x):
    return 5 * x[0] ** 2 + 12 * x[0] * x[1] - 8 * x[0] + 10 * x[1] ** 2 - 14 * x[1] + 5


def gradient(x):
    return np.array([10 * x[0] + 12 * x[1] - 8, 12 * x[0] + 20 * x[1] - 14])


Hessian = np.array([[10, 12], [12, 20]])

sol.append(float(abs(func(x) - func(xstar))))

while conv >= convergence_criteria:
    d = -np.matmul(np.linalg.inv(Hessian), gradient(x))

    alpha = line_search_bt(x, func, gradient, alpha, .5, .5, d)

    x = x - alpha * np.matmul(np.linalg.inv(Hessian), gradient(x))

    ans = func(x)

    diff = abs(func(x) - func(xstar))

    sol.append(float(diff))

    conv = np.linalg.norm(gradient(x))

x = np.array([-2 * x[0] - 3 * x[1] + 1, x[0], x[1]])
print(x)

plt.plot(sol)
plt.title("Newton's Method W/ Line Tracking")
plt.xlabel("Iteration")
plt.ylabel("Convergence")
plt.yscale("log")

