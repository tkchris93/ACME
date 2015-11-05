# solutions.py
"""Volume I Lab 6: QR Decomposition.
Name: Tanner Christensen
Date: 10/22/15
"""
import numpy as np
from scipy import linalg as la

def QR(A):
    '''
    Compute the QR decomposition of a matrix.
    Accept an m by n matrix A of rank n. 
    Return Q, R
    '''
    if A.dtype != "float64":
        A = np.array(A,dtype=float)
    norm = np.linalg.norm
    m, n = A.shape
    Q = np.copy(A)
    R = np.zeros((n,n))
    for i in xrange(0,n):
        print "ping"
        R[i,i] = float(norm(Q[:,i]))
        Q[:,i] = Q[:,i]/R[i,i]
        for j in xrange(i+1,n):
            R[i,j] = np.dot(Q[:,j].T, Q[:,i])
            Q[:,j] -= R[i,j]*Q[:,i]
    return Q,R
    
def prob2(A):
    '''
    Use your QR decomposition from the previous problem to compute 
    the determinant of A.
    Accept a square matrix A of full rank.
    Return |det(A)|.
    '''
    Q,R = la.qr(A)
    return np.product(R.diagonal())

def householder(A):
    '''
    Use the Householder algorithm to compute the QR decomposition
    of a matrix.
    Accept an m by n matrix A of rank n. 
    Return Q, R
    '''
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
    '''
    Compute the Hessenberg form of a matrix. Find orthogonal Q and upper
    Hessenberg H such that A = QtHQ.
    Accept a non-singular square matrix A.
    Return Q, H
    '''
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

def givens(A):
    '''
    EXTRA 20% CREDIT
    Compute the Givens triangularization of matrix A.
    Assume that at the ijth stage of the algorithm, a_ij will be nonzero.
    Accept A
    Return Q, R
    '''
    m,n = A.shape
    R = np.copy(A)
    Q = np.eye(n,n)
    G = np.empty((2,2))
    for j in xrange(0,n):
        for i in xrange(m-1,j,-1):
            print j,i
            a,b = R[i-1,j],R[i,j]
            G = np.array([[a,b],[-b,a]])/np.sqrt(a**2 + b**2)
            print G
            R[i-1:i+1,j:] = G.dot(R[i-1:i+1,j:])
            Q[i-1:i+1,:] = G.dot(Q[i-1:i+1,:])
    return Q.transpose(), R

def prob6(H):
    '''
    EXTRA 20% CREDIT
    Compute the Givens triangularization of an upper Hessenberg matrix.
    Accept upper Hessenberg H.
    '''
    m,n = A.shape
    R = np.copy(A)
    Q = np.eye(n,n)
    G = np.empty((2,2))
    for i in xrange(0,n-1):
        a,b = R[i,i],R[i+1,i]
        G = np.array([[a,b],[-b,a]])/sqrt(a**2 + b**2)
        R[i:i+2,i:] = G.dot(R[i:i+2,i:])
        Q[i:i+2,:i+2] = G.dot(Q[i:i+2,:i+2])
    return Q.transpose(),R
