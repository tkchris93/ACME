# name this file 'solutions.py'
"""Volume I Lab 3: Plotting with matplotlib
Tanner Christensen
Sept 18, 2015
"""

# Add your import statements here.
from matplotlib import pyplot as plt
import numpy as np
from mayavi import mlab

# Problem 1
def curve():
    """Plot the curve 1/(x-1) on [-2,6]. Plot the two sides of the curve separately
    (still with a single call to plt.plot()) so that the graph looks discontinuous 
    at x = 1.
    """
    x1 = np.linspace(-2,.999,500)
    y1 = 1/(x1-1)
    x2 = np.linspace(1.001,6,500)
    y2 = 1/(x2-1)
    plt.axis([-2,6,-6,6])
    plt.plot(x1,y1,'m--',x2,y2,'m--',linewidth=5)
    plt.show()

# Problem 2
def colormesh():
    """Plot the function f(x,y) = sin(x)sin(y)/(xy) on [-2*pi, 2*pi]x[-2*pi, 2*pi].
    Include the scale bar in your plot.
    """
    x = np.linspace(-2*np.pi, 2*np.pi,500)
    y = np.linspace(-2*np.pi, 2*np.pi,500)
    X,Y = np.meshgrid(x,y)
    f = np.sin(X)*np.sin(Y)/(X*Y)
    plt.pcolormesh(X,Y,f,cmap='seismic')
    plt.colorbar()
    plt.gca().set_aspect('equal')
    plt.axis([-6,6,-6,6])
    plt.show()

# Problem 3
def histogram():
    """Plot a histogram and a scatter plot of 50 random numbers chosen in the
    interval [0,1).
    """
    y = np.random.rand(50)
    x = np.linspace(1,50,50)
    plt.subplot(1,2,1)
    plt.hist(y, bins=5)
    plt.subplot(1,2,2)
    plt.scatter(x,y)
    avg = np.mean(y)
    avg = np.ones(50)*avg
    plt.plot(x, avg,'r')
    plt.axis([0,50,0,1])
    plt.show()
    
# Problem 4
def ripple():
    """Plot z = sin(10(x^2 + y^2))/10 on [-1,1]x[-1,1] using Mayavi."""
    X,Y = np.mgrid[-1:1:0.025, -1:1:0.025]
    Z = np.sin(10*(X**2 + Y**2))/10
    mlab.surf(X,Y,Z)
    
