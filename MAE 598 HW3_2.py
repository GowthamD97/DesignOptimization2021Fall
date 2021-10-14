from bayes_opt import BayesianOptimization
from matplotlib import pyplot

def function(x, y):
    return -((4-2.1*x*2+(x4)/3)*x2+x*y+(-4+4*y2)*y*2)
pbounds = {'x': (-3, 3), 'y': (-2, 2)}

optimizer = BayesianOptimization(f=function,pbounds=pbounds,random_state=1)

optimizer.maximize(init_points=2,n_iter=15)
print(optimizer.max)