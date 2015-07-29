import sys
import matrix_multiply
import time

output = []

if len(sys.argv) == 1:
    print "No Input"
elif sys.argv[1] != "matrices.npz":
    print "Invalid Input"
else:    
    A,B = matrix_multiply.load_matrices(sys.argv[1])
    
    m1_time1 = time.time()
    matrix_multiply.method1(A,B)
    m1_time2 = time.time()
    
    output.append(m1_time2 - m1_time1)
    
    m2_time1 = time.time()
    matrix_multiply.method2(A,B)
    m2_time2 = time.time()
    
    output.append(m2_time2 - m2_time1)
    
    m3_time1 = time.time()
    matrix_multiply.method3(A,B)
    m3_time2 = time.time()
    
    output.append(m3_time2 - m3_time1)
    
    print output