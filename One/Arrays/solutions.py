#solutions.py
"""Volume 1 Lab 2: NumPy and SciPy
Written Summer 2015 (Tanner Christensen)
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# student's file should be called solutions.py

# Problem 1: Perform matrix multiplication

A = np.array([[2,4,0],[-3,1,-1],[0,3,2]])
B = np.array([[3,-1,2],[-2,-3,0],[1,0,-2]])
product = A.dot(B)


# Problem 2: Return an array with all nonnegative numbers

def nonnegative(my_array):
    """Changes all negative entries in the inputed array to 0.

    Example:
    >>> my_array = np.array([-3,-1,3])
    >>> nonnegative(my_array)
    array([0,0,3])
    """
    
    my_array[my_array<0] = 0
    return my_array

# Problem 3: nxn array of floats and operations on that array

def normal_var(n):
    """Creates nxn array with values from the normal distribution, computes 
    the mean of each row and computes the variance of these means.
    """
    my_array = np.random.randn(n*n).reshape((n,n))
    return np.var(np.mean(my_array,axis=1))
   
# Problem 4: Solving Laplace's Equation using the Jacobi method and array slicing

def laplace(A, tolerance):
    """Solve Laplace's Equation using the Jacobi method and array slicing."""
    B = np.copy(A)
    difference = tolerance
    while difference >= tolerance:
        B[1:-1,1:-1] = (A[:-2,1:-1] + A[2:,1:-1] + A[1:-1,:-2] + A[1:-1,2:])/4.
        difference = np.max(np.abs(A-B))
        A[1:-1,1:-1] = B[1:-1,1:-1]
    return A   

def laplace_plot():    
    """Visualize your solution to Laplace equation"""
    n = 100
    tol = .0001
    U = np.ones ((n, n))
    U[:,0] = 100 # sets north boundary condition
    U[:,-1] = 100 # sets south boundary condition
    U[0] = 0 # sets west boundary condition
    U[-1] = 0 # sets east boundary condition
    # U has been changed in place (note that laplace is the name of
    # the function in this case).
    laplace(U, tol)
    x = np.linspace(0, 1, n)
    y = np.linspace(0, 1, n)
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.plot_surface (X, Y, U, rstride=5)
    plt.show()

# Problem 5: Blue shift an RGB image

def blue_shift():
    """Create a 100x100x3 array and perform a blue shift"""
    my_array = np.random.random_integers(0,255,100*100*3).reshape((100,100,3))
    blue = np.copy(my_array)
    blue[:,:,:2] = 0.5*my_array[:,:,:2]   
    return my_array, blue 

def blue_shift_plot():
    """Visualize the original and the blue_shift image"""
    original, blue = blue_shift()
    original = 255 - original
    blue = 255 - blue
    plt.subplot(1,2,1)
    plt.imshow(original)
    plt.subplot(1,2,2)
    plt.imshow(blue)
    plt.show()
    

