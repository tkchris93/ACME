from mpi4py import MPI
import numpy as np
import sys
import random

RANK = MPI.COMM_WORLD.Get_rank()
SIZE = MPI.COMM_WORLD.Get_size()

m = int(sys.argv[1])
p = int(sys.argv[2])

a = np.zeros(1,dtype=float)


if RANK == 0:
    # collect everything
    total = 0.
    for i in xrange(1,SIZE):
        MPI.COMM_WORLD.Recv(a, source=i)
        total += a[0]
    print total/(SIZE-1)*(2**m)
else:
    count = 0
    for i in xrange(p/SIZE):  
        # we don't take the squareroot, because it will still be less than 1
        if np.sum([random.uniform(-1.0,1.0)**2 for j in xrange(m)]) <= 1:
            count += 1
    a[0] = float(count)/(p/SIZE)
    MPI.COMM_WORLD.Send(a)

