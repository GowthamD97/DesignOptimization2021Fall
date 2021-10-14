from matplotlib import pyplot
import torch as t
from torch.autograd import Variable
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math as m

x_1=np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
x_2= 1 - (x_1)
p_i=np.array([28.1,34.4,36.7,36.9,36.8,36.7,36.5,35.4,32.9,27.7,17.5])

T=20
aW1=8.07131
aW2=1730.63
aW3=233.426

aD1=7.43155
aD2=1554.679
aD3=240.337

LPW= aW1 - (aW2/(T+aW3))
PSat_water= 10 ** LPW

LPD= aD1 - (aD2/(T+aD3))
PSat_dioxane= 10 ** LPD

x = Variable(t.tensor([1.0, 1.0]), requires_grad=True)
s = 0.001


res = []

for i in range(100):
    for i in range(0,11):
        loss = (((x1[i]t.exp(x[0]((x[1]x2[i])/(x[0]*x1[i]+x[1]*x2[i]))2)*PSat_water) + (x2[i]*t.exp(x[1]((x[0]x1[i])/(x[0]*x1[i]+x[1]*x2[i]))2)*PSat_dioxane)) - p_i[i])*2
        loss.backward()
    x.grad.numpy()
    with t.no_grad():
       x -= s * x.grad
       x.grad.zero_()
print(x.data.numpy())
print(loss.data.numpy())
for i in range(0,11):
  P_opt = ((x1[i]m.exp(x[0]((x[1]x2[i])/(x[0]*x1[i]+x[1]*x2[i]))2)*PSat_water) + (x2[i]*m.exp( x[1]((x[0]x1[i])/(x[0]*x1[i]+x[1]*x2[i]))*2)*PSat_dioxane))
  print("P_Optimised",i+1," =",P_opt)
  print("P_measured",i+1," =", p_i[i])
  print("Error  P",i+1,"value =" , p_i[i]-P_opt)