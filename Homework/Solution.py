from scipy.optimize import minimize
funcn = lambda x: (x[0] - x[1]) ** 2 + (x[1] + x[2] - 2) ** 2 + (x[3] - 1) ** 2 + (x[4] - 1) ** 2
const = ({'type': 'eq', 'func': lambda x: x[0] + 3 * x[1]},
        {'type': 'eq', 'func': lambda x: x[2] + x[3] - 2 * x[4]},
        {'type': 'eq', 'func': lambda x: x[1] - x[4]})
bounds = ((-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10))
result = minimize(funcn, (1, 2, 3, 4, 5), method='SLSQP', bounds=bounds, constraints=const)
print(result)