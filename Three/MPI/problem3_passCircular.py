import numpy as np
from mpi4py import MPI
import sys

RANK = MPI.COMM_WORLD.Get_rank()
SIZE = MPI.COMM_WORLD.Get_size()

a = np.zeros(1,dtype=int)

if RANK == 0:
    a[0] = 0
    print "{} sending: {}\n".format(RANK, a[0])
    MPI.COMM_WORLD.Send(a,dest=1)
    MPI.COMM_WORLD.Recv(a, source=SIZE-1)
    print "{} received: {}\n".format(RANK, a[0])
elif RANK == SIZE-1:
    a[0] = SIZE-1
    print "{} sending: {}\n".format(RANK, a[0])
    MPI.COMM_WORLD.Send(a, dest=0)
    MPI.COMM_WORLD.Recv(a, source=RANK-1)
    print "{} received: {}\n".format(RANK, a[0])
else:
    a[0] = RANK
    print "{} sending: {}\n".format(RANK, a[0])
    MPI.COMM_WORLD.Send(a,dest=RANK+1)
    MPI.COMM_WORLD.Recv(a, source=RANK-1)
    print "{} received: {}\n".format(RANK, a[0])
