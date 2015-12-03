import numpy as np
from __future__ import division
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

f = lambda x: abs(x)
for n in xrange(2,21):
    plt.subplot(7,3,n-1)
    plt.title("Degree %d" % n)
    x = np.linspace(-1,1,n+1)
    y = f(x)
    plt.scatter(x,y)
    X,Y = barycentric(x,y)
    plt.plot(X,Y)
    plt.plot([-1,0,1],[1,0,1])
    plt.axis([-1.2,1.2,-0.2,1.2])
    plt.gca().get_xaxis().set_ticks([])
    plt.gca().get_yaxis().set_ticks([])
plt.show()



