cdef extern from "csum.h":
    double csum(double* a)
    
cpdef cysum(double[:] a):
    return csum(&a[0])
