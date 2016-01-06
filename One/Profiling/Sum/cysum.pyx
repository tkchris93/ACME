def cysum(double[:] A):
    cdef double total = 0
    cdef int i
    for i in xrange(len(A)):
        total += A[i]
    return total
