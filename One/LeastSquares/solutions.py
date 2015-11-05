#solutions.py
from matplotlib import pyplot as plt
from scipy import linalg as la
import numpy as np
from numpy.lib import scimath as sm

# Problem 1
def least_squares(A,b):
    """Return the least squares solutions to Ax = b using QR decomposition."""
    Q,R = la.qr(A)
    return la.solve_triangular(R, np.dot(Q.T,b))

# Problem 2
def line_fit():
    """Plot linepts and its best-fit line on the same plot."""
    linepts = np.load('data.npz')['linepts']
    
    A = np.copy(linepts)
    A[:,1] = 1

    B = np.copy(linepts[:,1])
    x_hat = la.lstsq(A,B)[0,0]

    x0 = np.linspace(0,4000,100)
    y0 = x_hat*x0
    plt.plot(A[:,:1],B,'.',x0,y0)
    plt.axis([0,4000,0,20000])
    plt.show()

# Problem 3
def ellipse_fit():
    """Plot ellipsepts and its best-fit line on the same plot."""
    ellipsepts = np.load('data.npz')['ellipsepts']
    x_pts = ellipsepts[:,:1]
    y_pts = ellipsepts[:,1:]
    A = np.hstack((x_pts**2, x_pts, x_pts*y_pts, y_pts, y_pts**2))
    b = np.vstack((np.ones(len(ellipsepts))))
    a,b,c,d,e = la.lstsq(A,b)[0]
    plot_ellipse(x_pts,y_pts,a,b,c,d,e)

def plot_ellipse(X, Y, a, b, c, d, e):
    """Plots an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1.

    Input:
      X (array) - x-coordinates of all the data points.
      Y (array) - y-coordinates of all the data points.
      a,b,c,d,e (float) - the coefficients from the equation of an 
                    ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1.
    """
    def get_r(a, b, c, d, e):
        theta = np.linspace(0,2*np.pi,200)
        A = a*(np.cos(theta)**2) + c*np.cos(theta)*np.sin(theta) + e*(np.sin(theta)**2)
        B = b*np.cos(theta) + d*np.sin(theta)
        r = (-B + np.sqrt(B**2 + 4*A))/(2*A)
        return r, theta
        
    r,theta = get_r(a,b,c,d,e)
    plt.plot(r*np.cos(theta), r*np.sin(theta), color = "r")
    plt.plot(X,Y,".", color = "b")
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()

# Problem 4
def power_method(A,tol):
    """Return the dominant eigenvalue of A and its corresponding eigenvector."""
    size = A.shape[0]
    random_vector = []
    for i in xrange(size):
        random_vector.append(np.random.randint(10))
    norm = la.norm(random_vector)
    random_vector = np.array(random_vector, dtype = np.float)
    random_vector /= norm
    
    while True:
        product = np.dot(A,random_vector)
        new_vector = product/la.norm(product)
        if (la.norm(new_vector - random_vector) < tol):
            break  
        random_vector = new_vector
    
    eigenvector = random_vector
    eigenvalue = np.inner(np.dot(A,eigenvector),eigenvector)/la.norm(eigenvector)
    return eigenvalue, eigenvector
    
# Problem 5
def QR_algorithm(A,niter,tol):
    """Return the eigenvalues of A using the QR algorithm."""
    H = la.hessenberg(A)
    for i in xrange(niter):
        Q,R = la.qr(H)
        H = np.dot(R,Q)
    S = H
    print S
    eigenvalues = []
    i = 0
    while i < S.shape[0]:
        if i == S.shape[0]-1:
            eigenvalues.append(S[i,i])
        elif abs(S[i+1,i]) < tol:
            eigenvalues.append(S[i,i])
        else:
            a = S[i,i]
            b = S[i,i+1]
            c = S[i+1,i]
            d = S[i+1,i+1]
            B = -1*(a+d)
            C = a*d-b*c
            eigen_plus = (-B + sm.sqrt(B**2 - 4*C))/2.
            eigen_minus = (-B - sm.sqrt(B**2 - 4*C))/2.
            
            eigenvalues.append(eigen_plus)
            eigenvalues.append(eigen_minus)
            i+=1
        i+=1
    return eigenvalues
