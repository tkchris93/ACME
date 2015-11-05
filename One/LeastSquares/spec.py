#spec.py

# Problem 1
def least_squares(A,b):
    """Return the least squares solutions to Ax = b using QR decomposition."""
    pass

# Problem 2
def line_fit():
    """Plot linepts and its best-fit line on the same plot."""
    pass

# Problem 3
def ellipse_fit():
    """Plot ellipsepts and its best-fit line on the same plot."""
    pass

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
    pass
    
# Problem 5
def QR_algorithm(A,niter,tol):
    """Return the eigenvalues of A using the QR algorithm."""
    pass
