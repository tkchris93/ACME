from __future__ import division
import numpy as np
from scipy import linalg as la

def unit_sphere():
    """I wasn't getting good estimates with 10000, so I bumped it up."""
    #numPoints = 10000
    numPoints = 1000000
    
    points = np.random.rand(3,numPoints)
    points = points*2-1
    
    """
    This part here is the only major difference. I'm honestly not sure
    why you were getting the answers you were. If you look at the 
    documentation for np.hypot, it accepts 2 sides of a triangle and 
    an output array. So points[2,:] was being passed as an output 
    array. I have no idea what the function does with that, but I 
    chose to use la.norm instead. I think the cleanest way to solve 
    this problem is to use np.apply_along_axis, but at this point in
    the lab, they haven't seen that yet. So here is how I would do it.
    """
    #circleMask = np.hypot(points[0,:], points[1,:], points[2,:]) <= 1
    circleMask = [la.norm(points[:,i]) <= 1 for i in xrange(numPoints)]

    """
    Since circleMask is all 1's and 0's, you can just sum it up to know
    how many points were inside the sphere. Not a big deal.
    """
    #numInCircle = np.count_nonzero(circleMask)
    numInCircle = np.sum(circleMask)
    
    """I just changed this to be a return instead of print."""
    return 8.*numInCircle/numPoints

"""
When I'm calling functions from a script, I like doing it this way (I 
think Shane had this in a previous lab.) This is equivalent to 
"int main()" in c++. This way you can import functions from this file
without executing anything. If this is new to you, it's definitey worth
knowing and we can talk about it later.
"""
if __name__ == "__main__":
    print(unit_sphere())
