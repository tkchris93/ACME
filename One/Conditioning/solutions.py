from __future__ import division
import numpy as np
from numpy.random import normal
from matplotlib import pyplot as plt
from scipy import linalg as la

##############  Problem 1  ##############
def prob1():
    '''
    Randomly perturb w_coeff by replacing each coefficient a_i with a_i*r_i, where
    r_i is drawn from a normal distribution centered at 1 with varience 1e-10.
        
    Plot the roots of 100 such experiments in a single graphic, along with the roots
    of the unperturbed polynomial w(x)
        
    Using the final experiment only, estimate the relative and absolute condition number
    (in any norm you prefer).
        
    RETURN:
    Should display graph of all 100 perturbations.
    Should print values of relative and absolute condition.
    '''
    w_roots = np.arange(1, 21)
    w_coeffs = np.array([1, -210, 20615, -1256850, 53327946, -1672280820,
                40171771630, -756111184500, 11310276995381,
                    -135585182899530, 1307535010540395,
                    -10142299865511450, 63030812099294896,
                    -311333643161390640, 1206647803780373360,
                    -3599979517947607200, 8037811822645051776,
                    -12870931245150988800, 13803759753640704000,
                    -8752948036761600000, 2432902008176640000])
    
    # visualization of perturbed roots
    for i in xrange(100):
        perturb = normal(1,1e-10,size=21)
        perturbed_coeffs = w_coeffs*perturb
        perturbed_roots = np.roots(np.poly1d(perturbed_coeffs))
        plt.scatter(np.real(perturbed_roots), np.imag(perturbed_roots), 
                    marker='.', s=1, color='k')
    plt.scatter(np.real(w_roots), np.imag(w_roots),marker='o',color='b')
    
    # calculation of relative and absolute condition number
    perturbed_roots = np.sort(perturbed_roots)
    abs_k = la.norm(perturbed_roots-w_roots, np.inf)/la.norm(perturb, np.inf)
    rel_k = abs_k*la.norm(w_coeffs, np.inf)/la.norm(w_roots, np.inf)
    
    print "Absolute:\t" + str(abs_k)
    print "Relative:\t" + str(rel_k)
    plt.show()

##############  Problem 2  ##############   
def eig_condit(M):
    '''
    Approximate the condition number of the eigenvalue problem at M.
    
    INPUT:
    M - A 2-D square NumPy array, representing a square matrix.
    
    RETURN:
    A tuple containing approximations to the absolute and 
    relative condition numbers of the eigenvalue problem at M.
    '''
    raise NotImplementedError('eig_condit not implemented')



#   1 pt extra credit
def plot_eig_condit(x0=-100, x1=100, y0=-100, y1=100, res=10):
    '''
    Create a grid of points. For each pair (x,y) in the grid, find the 
    relative condition number of the eigenvalue problem, using the matrix 
    [[1 x]
     [y 1]]
    as your input. You can use plt.pcolormesh to plot the condition number
    over the entire grid.
    
    INPUT:
    x0 - min x-value of the grid
    x1 - max x-value
    y0 - min y-value
    y1 - max y-value
    res - number of points along each edge of the grid
    '''
    raise NotImplementedError('plot_eig_condit not implemented')

##############  Problem 3  ##############
def integral(n):
    '''
    RETURN I(n)
    '''
    raise NotImplementedError('integral not implemented')

def prob3():
    '''
    For the values of n in the problem, compute integral(n). Compare
    the values to the actual values, and print your explanation of what
    is happening.
    '''
    
    #actual values of the integral at specified n
    actual_values = [0.367879441171, 0.145532940573, 0.0838770701034, 
                 0.0590175408793, 0.0455448840758, 0.0370862144237, 
                 0.0312796739322, 0.0270462894091, 0.023822728669, 
                 0.0212860390856, 0.0192377544343] 
    raise NotImplementedError('Problem 3 not implemented')

if __name__ == "__main__":
    prob1()
