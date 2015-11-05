from matplotlib import pyplot as plt
import numpy as np

# Problem 1
def prob1():
    x = np.linspace(-2,.999,100)
    y = 1./(x-1)
    plt.plot(x,y,'m--',linewidth=5)
    x = np.linspace(1.001,6,100)
    y = 1./(x-1)
    plt.plot(x,y,'m--',linewidth=5)
    plt.axis([-2,6,-6,6])
    plt.show()

# Problem 2
def prob2():
    x = np.linspace(-2*np.pi,2*np.pi)
    y = np.linspace(-2*np.pi,2*np.pi)
    X, Y = np.meshgrid(x,y)
    f = (np.sin(X)*np.sin(Y))/(X*Y)
    plt.pcolormesh(X,Y,f,cmap='seismic')
    plt.colorbar()
    plt.axis([-2*np.pi,2*np.pi,-2*np.pi,2*np.pi])
    plt.gca().set_aspect('equal')
    plt.show()

# Problem 3
def prob3():
    y = np.random.rand(50)
    plt.subplot(1,2,1)
    plt.hist(y,bins=5)
    x = np.linspace(1,50,num=50)
    plt.subplot(1,2,2)
    plt.scatter(x,y)
    plt.axis([0,50,-.2,1.2])
    z = np.mean(y)
    z = np.ones(len(x))*z
    plt.plot(x,z,color='r')
    plt.show()
