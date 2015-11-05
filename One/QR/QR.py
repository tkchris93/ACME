import numpy as np
from scipy import linalg as la

def MGS(A):
    norm = np.linalg.norm
    m, n = A.shape
    Q = np.copy(A)
    R = np.zeros((n,n))
    for i in xrange(0,n):
        R[i,i] = norm(Q[:,i])
        Q[:,i] = Q[:,i]/R[i,i]
        for j in xrange(i+1,n):
            R[i,j] = np.dot(Q[:,j], Q[:,i])
            Q[:,j] = Q[:,j] - R[i,j]*Q[:,i]
    return Q,R
	
def determinant(A):
    Q,R = la.qr(A)
    return np.product(R.diagonal())
	
def householder(A):
    norm = la.norm
    m,n = np.shape(A)
    R = np.copy(A)
    Q = np.eye(m,m)
    for k in xrange(0,n):
        u = np.copy(R[k:,k])
        u[0] += np.sign(u[0])*norm(u)
        u /= norm(u)
        R[k:,k:] -= 2*np.outer(u,u.dot(R[k:,k:]))
        Q[k:] -= 2*np.outer(u,u.dot(Q[k:]))
    return np.matrix.getH(np.matrix(Q)),R
	
def hessenberg(A):
    m,n = np.shape(A)
    H = np.copy(A)
    Q = np.eye(m,m)
    for k in xrange(0,n-2):
        u = np.copy(H[k+1:,k])
        u[0] += np.sign(u[0])/la.norm(u)
        u = u/la.norm(u)
        H[k+1:,k:] -= 2*np.outer(u, u.dot(H[k+1:,k:]))
        H[:,k+1:] -= 2*np.outer(H[:,k+1:].dot(u), u)
        Q[k+1:] -= 2*np.outer(u, u.dot(Q[k+1:]))
    return Q,H
