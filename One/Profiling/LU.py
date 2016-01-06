import numpy as np

def LU1(A):
    """Returns the LU decomposition of a square matrix."""
    m,n = A.shape
    U = np.array(np.copy(A), dtype=float)
    L = np.eye(np.sqrt(A.size))
    for i in xrange(1,A.shape[0]):
        for j in xrange(i):
            L[i,j] = U[i,j]/U[j,j]
            U[i,j:] -= L[i,j]*U[j,j:]
    return L,U

def LU2(A):
    """Returns the LU decomposition of a square matrix A."""
    m,n = A.shape
    U = np.array(np.copy(A), dtype=float)
    L = np.zeros((n,n))
    for i in range(n):
        L[i,i] = 1
    for i in range(1,n):
        for j in range(i):
            L[i,j] = U[i,j]/U[j,j]
            for k in range(j,n):
                U[i,k] -= U[j,k]*U[i,j]/U[j,j]
    return L,U
