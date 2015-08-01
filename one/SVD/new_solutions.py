#solutions
import numpy as np
import scipy.linalg as la

def truncated_svd_retry(A,r=None,tol=10**6):
    m,n = A.shape
    eigs,evecs = la.eig(A.conj().T.dot(A))

    s = np.sqrt(eigs)
    sort_indices = np.argsort(s)
    s = s[sort_indices]
    evecs = evecs[:,sort_indices]
    if r is not None:
        if r > len(s):
            raise ValueError("r is too big")
        else:
            s = s[:r]

    V = np.empty((n,len(s)))
    for i in xrange(len(evecs)):
        V[:,i] = evecs[:,i]

    U = np.empty((m,len(s)))
    for i in xrange(len(s)):
        U[:,i] = (1./s[i])*A.dot(V[:,i])

    return U, s, V.conj().T


def truncated_svd(A,r=None,tol=10**-6):
    m,n = A.shape
    A = np.matrix(A)
    AHA = A.H.dot(A)
    evals,evecs = la.eig(AHA) 
    s = evals**(.5)
    print "length s: " + str(len(s))
    if r is not None:
        if r > len(s):
            raise ValueError("r is too big")
        else:
            s = s[:r]
    
    U = np.empty((m,len(s)))
    V = np.empty((n,len(s)))
    
    for i in xrange(len(s)):
        V[:,i] = evecs[i]
    V = np.matrix(V)
    Vh = V.H
    
    for j in xrange(len(s)):
        U[:,i] = ((1/s[i])*A.dot(V[:,i])).T
    return U,s,Vh
    '''
    Vh = []
    if r is not None:
    #truncated
        s = s[:r]
        for i in xrange(r):
            Vh.append(evecs[i])
    else:
    #compact.  No adjustment to s needed
        for i in xrange(len(evecs)):
            Vh.append(evecs[i])
    Vh = np.matrix(Vh)
    #V = Vh.H
    Ut = []
    print "shape A: " + str(A.shape)
    print "shape Vh: " + str(Vh.shape)
    for i in xrange(len(s)):
        Ut.append(1/s[i]*(A.dot(Vh[i].H)))
    print Ut
    Ut = np.matrix(Ut)
    U = Ut.H
    return U,s,Vh
    '''

def their_truncated_svd(A,r=None,tol=10**-6):
    '''
    Computes the truncated SVD of A. If r is None or equals the number of nonzero singular values, it is the compact SVD.
    Parameters:
        A: the matrix
        r: the number of singular values to use 
        tol: the tolerance for zero
    Returns:
        U - the matrix U in the SVD
        s - the diagonals of Sigma in the SVD
        Vh - the matrix V^H in the SVD
    '''
    #Initialize things
    m,n = A.shape

    #Find eigenvalues and eigenvectors of A^H A
    eigs, vr = la.eig(A.conj().T.dot(A)) 
    #Find singular values
    sigs = np.sqrt(eigs) 
    #Find how many singular values are nonzero
    mask = sigs > tol 
    num_eigs = np.sum(mask)
    if (r==None):
        #Return compact SVD
        r=num_eigs
    elif (num_eigs < r):
        print 'less nonzero eigenvalues than given size'
        return
    #Initialize things
    U = np.empty((m,r))
    s = np.zeros(r)
    V = np.empty((n,r))
    
    
    #Sort the singular values and only keep the greatest r
    sorted_index = np.argsort(sigs)[::-1]
    sigs = sigs[sorted_index]
    s[:r] = sigs[:r]
    #Keep eigenvectors matching the order of the singular values
    vr = vr[:,sorted_index]
    
    #Calculate V
    #Only keep the first r columns corresponding to the first r singular values
    V = vr[:,:r]

    #Calculate U
    #The first r columns are 1/sigma*A V_i where V_i is the ith column of V.
    #Only use columns that correspond to the first r singular values
    U = 1./sigs[:r]*A.dot(V[:,:r])
    
    return U, s, V.conj().T
