cdef extern from "cppsum.h":
    double cppsum(double* a)
    
cpdef cy_cppsum(double[:] a):
    return cppsum(&a[0])
