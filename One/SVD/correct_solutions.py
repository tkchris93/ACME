# solutions.py
from scipy import linalg as la
import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def truncated_svd(A,r=None,tol=10**-6):
    """Computes the truncated SVD of A. If r is None or equals the number 
        of nonzero singular values, it is the compact SVD.
    Parameters:
        A: the matrix
        r: the number of singular values to use
        tol: the tolerance for zero
    Returns:
        U - the matrix U in the SVD
        s - the diagonals of Sigma in the SVD
        Vh - the matrix V^H in the SVD
    """
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

# Problem 2
def visualize_svd(A):
    """Plot each transformation associated with the SVD of A."""
    S = np.load("circle.npz")["circle"]
    vec = np.load("circle.npz")["unit_vectors"]
    
    U,s,Vh = la.svd(A)
    
    VhS = Vh.dot(S)
    SigVhS = np.diag(s).dot(VhS)
    USigVhS = U.dot(SigVhS)
    
    Vhvec = Vh.dot(vec)
    SigVhvec = np.diag(s).dot(Vhvec)
    USigVhvec = U.dot(SigVhvec)

    border1 = [-1.1, 1.1, -1.1, 1.1]
    border2 = [-4.5, 4.5, -4.5, 4.5]
    plt.subplot(2,2,1)
    plt.plot(S[0],S[1],vec[0],vec[1])
    plt.axis(border1)
    plt.axis("equal")
    plt.subplot(2,2,2)
    plt.plot(VhS[0],VhS[1],Vhvec[0],Vhvec[1])
    plt.axis(border1)
    plt.axis("equal")
    plt.subplot(2,2,3)
    plt.plot(SigVhS[0],SigVhS[1],SigVhvec[0],SigVhvec[1])
    plt.axis(border2)
    plt.axis("equal")
    plt.subplot(2,2,4)
    plt.plot(USigVhS[0],USigVhS[1],USigVhvec[0],USigVhvec[1])
    plt.axis(border2)
    plt.axis("equal")
    plt.show()

# Problem 3
def svd_approx(A, k):
    """Returns best rank k approximation to A with respect to the induced 2-norm.
    
    Inputs:
    A - np.ndarray of size mxn
    k - rank 
    
    Return:
    Ahat - the best rank k approximation
    """
    U,s,Vt = la.svd(A, full_matrices=False)
    S = np.diag(s[:k])
    print S
    u1,s1,vt1 = U[:,:k],S[:k,:k],Vt[:k,:]
    diff = (u1.nbytes + np.diag(s1).nbytes + vt1.nbytes) - A.nbytes
    if diff > 0:
        print "WARNING: Given parameters do not result in compressed data."
    Ahat = U[:,:k].dot(S).dot(Vt[:k,:])
    return Ahat
    
# Problem 4
def lowest_rank_approx(A,e):
    """Returns the lowest rank approximation of A with error less than e 
    with respect to the induced 2-norm.
    
    Inputs:
    A - np.ndarray of size mxn
    e - error
    
    Return:
    Ahat - the lowest rank approximation of A with error less than e.
    """
    U,s,Vt = la.svd(A, full_matrices=False)
    k = np.where(s<e)[0][0]
    return svd_approx(A,k)
    
# Problem 5
def compress_image(filename,k):
    """Plot the original image found at 'filename' and the rank k approximation
    of the image found at 'filename.'
    
    filename - jpg image file path
    k - rank
    """
    orig_img = plt.imread(filename).astype(float)
    red = orig_img[:,:,0]
    green = orig_img[:,:,1]
    blue = orig_img[:,:,2]
    
    img = np.zeros(orig_img.shape)
    img[:,:,0] = svd_approx(red,k)
    img[:,:,1] = svd_approx(green,k)
    img[:,:,2] = svd_approx(blue,k)
    
    img = np.round(img)/255.
    orig_img = np.round(orig_img)/255.
    img[img<0] = 0.
    img[img>1] = 1.
    
    plt.subplot(1,2,1)
    plt.title("Original Image")    
    plt.imshow(orig_img)
    plt.subplot(1,2,2)
    plt.title("Rank " + str(k) + " Approximation")
    plt.imshow(img)
    plt.show()
