# solutions.py
"""Volume I Lab 5: Invertible Affine Transformations and Linear Systems.
Name: Tanner Christensen
Date: Fall 2015
"""

import numpy as np
import time
from matplotlib import pyplot as plt
from scipy import linalg as la

# Helper Functions
def plot_transform(original, new):
    """Display a plot of points before and after a transform.
    
    Inputs:
        original (array) - Array of size (2,n) containing points in R2 as columns.
        new (array) - Array of size (2,n) containing points in R2 as columns.
    """
    window = [-5,5,-5,5]
    plt.subplot(1, 2, 1)
    plt.title('Before')
    plt.gca().set_aspect('equal')
    plt.scatter(original[0], original[1])
    plt.axis(window)
    plt.subplot(1, 2, 2)
    plt.title('After')
    plt.gca().set_aspect('equal')
    plt.scatter(new[0], new[1])
    plt.axis(window)
    plt.show()

def type_I(A, i, j):  
    """Swap the i-th and j-th rows."""
    A[i], A[j] = np.copy(A[j]), np.copy(A[i])
    
def type_II(A, i, const):  
    """Multiply the i-th row of A by const."""
    A[i] *= const
    
def type_III(A, i, j, const):  
    """Add a constant of the j-th to the i-th row."""
    A[i] += const*A[j]


# Problem 1
def dilation2D(A, x_factor, y_factor):
    """Scale the points in A by x_factor in the x direction and y_factor in
    the y direction.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        x_factor (float) - scaling factor in the x direction.
        y_factor (float) - scaling factor in the y direction.
    """
    T = np.array([[x_factor,0],[0,y_factor]])
    return T.dot(A)
    
# Problem 2
def rotate2D(A, theta):
    """Rotate the points in A about the origin by theta radians.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        theta (float) - number of radians to rotate points in A.
    """
    T = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
    return T.dot(A)
    
# Problem 3
def translate2D(A, b):
    """Translate the points in A by the vector b.
    
    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        b (2-tuple (b1,b2)) - Translate points by b1 in the x direction and by b2 
            in the y direction.
    """
    b = np.vstack([b[0],b[1]])
    return A + b
   
# Problem 4
def rotatingParticle(time, omega, direction, speed):
    """Display a plot of the path of a particle P1 that is rotating 
    around another particle P2.
    
    Inputs:
     - time (2-tuple (a,b)): Time span from a to b seconds.
     - omega (float): Angular velocity of P1 rotating around P2.
     - direction (2-tuple (x,y)): Vector indicating direction.
     - speed (float): Distance per second.
    """
    direction = np.array(direction)
    T = np.linspace(time[0],time[1],100)
    start_P1 = [1,0]
    posP1_x = []
    posP1_y = []
    
    for t in T:
        posP2 = speed*t*direction/la.norm(direction)
        posP1 = translate2D(rotate2D(start_P1, t*omega), posP2)[0]
        posP1_x.append(posP1[0])
        posP1_y.append(posP1[1])
        
    plt.plot(posP1_x, posP1_y)
    plt.gca().set_aspect('equal')
    plt.show()
    
# Problem 5
def REF(A):
    """Reduce a square matrix A to REF. During a row operation, do not
    modify any entries that you know will be zero before and after the
    operation."""
    
    A1 = np.array(np.copy(A), dtype=float)
    
    step = 1
    for j in xrange(1,len(A1[0])):
        step = j
        for i in xrange(len(A1)-step):
            A1[i+step,step-1:] -= (A1[i+step,step-1]/A1[step-1,step-1]) * A1[step-1,step-1:]
    return A1
    
# Problem 6
def LU(A):
    """Returns the LU decomposition of a square matrix."""
    U = np.array(np.copy(A), dtype=float)
    L = np.identity(np.sqrt(A.size))
    
    for i in xrange(1,A.shape[0]):
        for j in xrange(i):
            L[i,j] = U[i,j]/U[j,j]
            U[i,j:] -= L[i,j]*U[j,j:]
    return L,U

# Problem 7
def time_LU():
    """Print the times it takes to solve a system of equations using
    LU decomposition and (A^-1)B where A is 1000x1000 and B is 1000x500."""
    
    A = np.random.random((1000,1000))
    B = np.random.random((1000,500))
    
    before = time.time()
    LU = la.lu_factor(A)
    time_lu_factor = time.time() - before
    
    before = time.time()
    A_inv = la.inv(A)
    time_inv = time.time() - before
    
    before = time.time()
    a = la.lu_solve(LU,B)
    time_lu_solve = time.time() - before
    
    before = time.time()
    b = A_inv.dot(B)
    time_inv_solve = time.time() - before

    print "LU solve: " + str(time_lu_factor + time_lu_solve)
    print "Inv solve: " + str(time_inv + time_inv_solve)
    
    # What can you conclude about the more efficient way to solve linear systems?
    print "For matrices of this size, LU decomposition is measureably faster."
    
    
# ======= TEST DRIVER ===========
# Test script
def test(student_module, late=False):
    """Test script. You must import the students file as a module.
    
    10 points for problem 1
    10 points for problem 2
    10 points for problem 3
    10 points for problem 4
    10 points for problem 5
    10 points for problem 6
    10 points for problem 7
    
    Parameters:
        student_module: the imported module for the student's file.
        late (bool, opt): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 55.
        feedback (str): a printout of results for the student.
    """

    def strTest(x,y,m):
        """Test to see if x and y have the same string representation. If
        correct, award a points and return no message. If incorrect, return
        0 and return 'm' as feedback.
        """
        if str(x) == str(y): return 1, ""
        else:
            m += "\n\t\tCorrect response: " + str(x)
            m += "\n\t\tStudent response: " + str(y)
            return 0, m

    def grade(p,m):
        """Manually grade a problem worth 'p' points with error message 'm'."""
        part = -1
        while part > p or part < 0:
            part = int(input("\nScore out of " + str(p) + ": "))
        if part == p: return p,""
        else: return part,m

    s = student_module
    score = 0
    total = 70
    feedback = s.__doc__
    PI = np.load('pi.npy')
    try:    # Problem 1: 10 points
        feedback += "\n\nProblem 1 (10 points):"
        points = 0
        
        print "x_facter = 1, y_factor = 1.5"
        plot_transform(PI, s.dilation2D(PI, 1, 1.5))
        p,f = grade(3, "Failed when scaling x")
        points += p; feedback += f
        
        print "x_facter = 1.5, y_factor = 1"
        plot_transform(PI, s.dilation2D(PI, 1.5, 1))
        p,f = grade(3, "Failed when scaling y")
        points += p; feedback += f
        
        print "x_factor = 0.5, y_factor = 0.5"
        plot_transform(PI, s.dilation2D(PI, .5, .5))
        p,f = grade(4, "Failed when scaling x and y")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 10 points
        feedback += "\n\nProblem 2 (10 points):"
        points = 0
        
        print "theta = pi/4"
        plot_transform(PI, s.rotate2D(PI, np.pi/4))
        p,f = grade(5, "Failed when rotating pi/4")
        points += p; feedback += f
        
        print "theta = 3pi/4"
        plot_transform(PI, s.rotate2D(PI, 3*np.pi/4))
        p,f = grade(5, "Failed when rotating 3pi/4")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 3: 10 points
        feedback += "\n\nProblem 3 (10 points):"
        points = 0
        
        print "b = (1,0)"
        plot_transform(PI, s.translate2D(PI, np.vstack([1,0])))
        p,f = grade(3, "Failed when translating (1,0)")
        points += p; feedback += f
        
        print "b = (0,1)"
        plot_transform(PI, s.translate2D(PI, np.vstack([0,1])))
        p,f = grade(3, "Failed when translating (0,1)")
        points += p; feedback += f
        
        print "b = (1,1)"
        plot_transform(PI, s.translate2D(PI, np.vstack([1,1])))
        p,f = grade(4, "Failed when translating (1,1)")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    
    try:    # Problem 4: 10 points
        feedback += "\n\nProblem 5 (10 points):"
        points = 0
        
        s.rotatingParticle((0,10), np.pi, (1,1), 2)
        
        p,f = grade(10, "Incorrect answer")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message    
    
    try:    # Problem 5: 10 points
        feedback += "\n\nProblem 5 (10 points):"
        points = 0
        
        A = np.array([[1,2,3],[4,5,6],[7,8,9]])
        print "Correct Response"
        print REF(A)
        
        print "Student Response"
        print s.REF(A)
        
        p,f = grade(5, "Incorrect answer")
        points += p; feedback += f
        
        A = np.array([[2, 7, 9], [9, 9, 4],[7, 5, 5]])
        print "Correct Response"
        print REF(A)
        
        print "Student Response"
        print s.REF(A)
        
        p,f = grade(5, "Incorrect answer")
        points += p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    
    try:    # Problem 6: 10 points
        feedback += "\n\nProblem 6 (10 points):"
        points = 0
        
        A = np.array([[2, 8, 9], [1, 2, 9], [2, 7, 5]])
        L,U = s.LU(A)
        print "\nLower Triangular:"
        print L
        p,f = grade(3, "L was not lower triangular") 
        points += p; feedback += f
        
        print "\nUpper Triangular:"
        print U
        p,f = grade(3, "U was not upper triangular")
        points += p; feedback += f
        
        points += 4*np.allclose(L.dot(U), A)
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    try:    # Problem 7: 10 points
        feedback += "\n\nProblem 7 (10 points):"
        points = 0
        
        s.time_LU()

        p,f = grade(10, "Incorrect output") 
        points += p; feedback += f

        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message

    if late:    # Late submission penalty
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score.
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if   percentage >=  98.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    return score, feedback
