from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def weights(x):
    w = []
    for i in xrange(len(x)):
        temp = x[i] - x
        den = temp[temp != 0]
        w.append(1./np.prod(den))
    return w
def barycentric(x,y):
    w = weights(x)
    X = np.linspace(min(x),max(x),500)
    Xv = np.vstack(X)
    p = lambda a : np.sum(w*y/(a-x))/np.sum(w/(a-x))
    Y = np.apply_along_axis(p,1,Xv)
    Y[0] = y[0]
    Y[-1] = y[-1]
    return X,Y
   
x2 = np.linspace(-1,1,500)
y2 = np.sin(np.pi*x2)
plt.plot(x2,y2,color='k',label="Original Function",lw=2)
   
x0 = np.linspace(-1,1,4)
y0 = np.sin(np.pi*x0)
X0, Y0 = barycentric(x0,y0)
#plt.scatter(x0,y0)
plt.plot(X0,Y0,color='r',label="Uniform Interpolation")

x1 = np.cos(np.arange(4)*np.pi/3)
y1 = np.sin(np.pi*x1)
X1, Y1 = barycentric(x1,y1)
#plt.scatter(x1,y1)
plt.plot(X1,Y1,color='g',label="Chebyshev Interpolation")


plt.legend(loc='upper left')
plt.show() 
