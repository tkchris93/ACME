import time
import numpy as np

# Problem 14

def smallest(my_list):
    minimum = my_list[0]
    minimum_index = 0
    for i in xrange(len(my_list)):
        if my_list[i] < minimum:
            minimum = my_list[i]
            minimum_index = i
    return minimum_index
    
    """
     Temporal comlexity: 
        best/worst case: O(n)  
     Spatial complexity:
        best/worst case: O(n)
    """    

# Problem 15

def selection_sort(my_list):
    """Sorts the inputed list using the selection sort method."""

    for i in xrange(len(my_list)):
        index = smallest(my_list[i:])
        temp = my_list[i]
        my_list[i] = my_list[index+i]
        my_list[index+i] = temp
    return my_list

    """
    The algorithm will only run because after the loop runs n-1 times, the nth
        element of the list will already be in the correct order by the nature
        of the algorithm
    
    Temporal complexity:
        best/worst: O(n^2)
    Spatial complexity:
        best/worst: O(n)
    """

# Problem 16

def closest(l):
    """Finds the two points that are closest to each other.
    
    Inputs:    
        l (list): accepts a list of tuples
        
    Returns:
        min_pair (list): a list of the 2 points that are closest to each other.
    """
    
    min_dist = (l[0][0] - l[1][0])**2 + (l[0][1] - l[1][1])**2
    min_pair = [l[0],l[1]]    
    for i in xrange(len(l)):
        current = l[i]
        for other in l[(i+1):]:
            distance = (current[0]-other[0])**2 + (current[1]-other[1])**2
            if distance < min_dist:
                min_dist = distance
                min_pair = [current,other]
    return min_pair
    
    """
    We do not need to compute the squareroot function in this algorithm. We use
        the fact that sqrt(x) < sqrt(y) implies x < y. We never return the explicit
        distance between two points, we just want to know which are closest.
    
    The inner-most level of the loop will execute n(n+1)/2 times. n(n+1)/2 is in O(n^2).
    """

# Problem 17

def prob17():
    for k in xrange(1,5):
        A = np.random.rand(10**k,10**k)
        B = np.random.rand(10**k,10**k)
        x = np.random.rand(10**k,1)
        before1 = time.time()
        np.dot(np.dot(A,B),x) 
        after1 = time.time()  

        before2 = time.time()
        np.dot(A, np.dot(B,x))
        after2 = time.time()

        print "k = " + str(k)
        print "(AB)x " + str(after1 - before1)
        print "A(Bx) " + str(after2 - before2)

    """
    OUTPUT:
    k = 1
    (AB)x = 0.00284
    A(Bx) = 1.7e-05

    k = 2
    (AB)x = 0.00914
    A(Bx) = 0.00014
    
    k = 3
    (AB)x = 0.88541
    A(Bx) = 0.00569

    k = 4
    (AB)x = 863.488
    A(Bx) = 2.66071
    
    ------------
    According to the book, matrix-matrix multiplication is about 2n^3 FLOPS 
        where n is the number of rows.
        matrix-vector multiplication is about 2n^2 + n FLOPS.
    (AB)x : matrix-matrix mult + matrix-vector mult = 2n^3 + 2n^2 - n
    A(Bx) : matrix-vector mult + matrix-vector mult = 4n^2 + 2n
    
    The ratio between these approaches (n+1)/2 for large n. More exactly, 
        the ratio is (2n^3 + 2n^2 - n)/(4n^2 + 2n)
    
    """

# Problem 18

def prob18():
    for k in xrange(1,5):
        I = np.eye(10**k)
        u = np.random.rand(10**k,1)
        v = np.random.rand(10**k,1)
        x = np.random.rand(10**k,1)
        before1 = time.time()
        ans1 = np.dot(I + np.dot(u,v.T),x)
        after1 = time.time()

        before2 = time.time()
        ans2 = x + np.dot(np.dot(v.T,x)[0,0],u)
        after2 = time.time()

        print "k = " + str(k)
        print "(I + uv.T)x = " + str(after1 - before1)
        print "x + (v.Tx)u = " + str(after2 - before2)
        print ""
        
    """
    k = 1
    (I + uv.T)x = 0.0012629032135
    x + (v.Tx)u = 5.69820404053e-05

    k = 2
    (I + uv.T)x = 0.000365972518921
    x + (v.Tx)u = 5.60283660889e-05

    k = 3
    (I + uv.T)x = 0.0468370914459
    x + (v.Tx)u = 0.000144004821777

    k = 4
    (I + uv.T)x = 2.30172514915
    x + (v.Tx)u = 0.000309944152832
    
    ---------------
    (I + uv.T)x : matrix-matrix mult + matrix addition + matrix-vector mult
                    = 2n^3 + n^2 + 2n^2 - n = 2n^3 + 3n^2 - n
    x + (v.Tx)u : vector addition + vector inner product + scalar mult
                    = n + 2n - 1 + n = 4n - 1
    
    The ratio between these approaches (2n^2 + 3n)/4. More exactly, the
        ratio is (2n^3 + 3n^2 - n)/(4n - 1).
    
    """
