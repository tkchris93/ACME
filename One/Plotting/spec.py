# name this file 'solutions.py'
"""Volume I Lab 3: Plotting with matplotlib
Tanner Christensen
Sept 18, 2015
"""

# Add your import statements here.

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
    plt.plot(x1,y1,'m--',x2,y2,'m--')
    plt.show()

# Problem 2
def colormesh():
    """Plot the function f(x,y) = sin(x)sin(y)/(xy) on [-2*pi, 2*pi]x[-2*pi, 2*pi].
    Include the scale bar in your plot.
    """
    pass

# Problem 3
def histogram():
    """Plot a histogram and a scatter plot of 50 random numbers chosen in the
    interval [0,1).
    """
    pass
    
# Problem 4
def ripple():
    """Plot z = sin(10(x^2 + y^2))/10 on [-1,1]x[-1,1] using Mayavi."""
    pass
    
