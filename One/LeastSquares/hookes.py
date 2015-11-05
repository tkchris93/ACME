import numpy as np
from scipy import linalg as la
from matplotlib import pyplot as plt

P = np.array([[1.02,3.11],
              [2.03,5.97],
              [2.95,9.07],
              [3.92,12.02],
              [5.06,15.02],
              [6.00,17.91],
              [7.07,21.23]])

A = np.vstack(P[:,0])
b = np.vstack(P[:,1])
k = la.lstsq(A,b)[0]
print k
x0 = np.linspace(0,8,100)
y0 = k[0]*x0
plt.plot(A,b,"*",x0,y0)
plt.show()
