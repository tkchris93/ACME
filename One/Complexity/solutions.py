import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg
from scipy import sparse
from scipy.sparse import linalg as sl
import time

'''Functions for use in problem 1.'''
# Run through a single for loop.
def func1(n):
    n = 500*n
    sum(xrange(n))

# Run through a double for loop.
def func2(n):
    n = 3*n
    t = 0
    for i in xrange(n):
        for j in xrange(i):
            t += j

# Square a matrix.
def func3(n):
    n = int(1.2*n)
    A = np.random.rand(n, n)
    np.power(A, 2)

# Invert a matrix.
from scipy import linalg as la
def func4(n):
    A = np.random.rand(n, n)
    la.inv(A)

# Find the determinant of a matrix.
from scipy import linalg as la
def func5(n):
    n = int(1.25*n)
    A = np.random.rand(n, n)
    la.det(A)


def Problem1():
    """Create a plot comparing the times of func1, func2, func3, func4, 
    and func5. Time each function 4 times and take the average of each.
    """
    sizes = [100,200,400,800]
    func1_times = []
    func2_times = []
    func3_times = []
    func4_times = []
    func5_times = []
    
    for n in sizes:
        before = time.time()
        func1(n)
        func1_times.append(time.time()-before)
        
        before = time.time()
        func2(n)
        func2_times.append(time.time()-before)
        
        before = time.time()
        func3(n)
        func3_times.append(time.time()-before)
        
        before = time.time()
        func4(n)
        func4_times.append(time.time()-before)
        
        before = time.time()
        func5(n)
        func5_times.append(time.time()-before)
        
    plt.plot(sizes, func1_times, label="Function 1")
    plt.plot(sizes, func2_times, label="Function 2")
    plt.plot(sizes, func3_times, label="Function 3")
    plt.plot(sizes, func4_times, label="Function 4")
    plt.plot(sizes, func5_times, label="Function 5")
    plt.legend(loc="upper left")
    plt.show()

def Problem2(n):
    """takes an integer argument n and returns a sparse nxn 
    tri-diagonal array with 2's along the diagonal and -1's along
    the two sub-diagonals above and below the diagonal.
    """
    diag_entries = np.empty((3,n))
    diag_entries[0] = np.ones(n)*(-1)
    diag_entries[1] = np.ones(n)*2
    diag_entries[2] = np.ones(n)*(-1)
    A = sparse.spdiags(diag_entries, [-1,0,1],n,n,format="csr")
    return A

def Problem3(n):
    """Generate an nx1 random array b and solve the linear system Ax=b
    where A is the tri-diagonal array in Problem 2 of size nxn
    """
    A = Problem2(n)
    b = np.vstack(np.random.random(n))
    return A,sl.spsolve(A,b),b

def Problem4(n):
    """Write a function that accepts an integer argument n and returns
    (lambda)*n^2 where (lamba) is the smallest eigenvalue of the sparse 
    tri-diagonal array you built in Problem 2. Print the limit of (lambda)*n^2.
    """
    A = Problem2(n)
    eig = min(sl.eigs(A.asfptype(), which='SM')[0])
    
    print "lamba*n^2 approaches pi^2 as n goes to infinity"
    return eig*n**2

