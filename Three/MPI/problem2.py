import numpy as np
from mpi4py import MPI
import sys

RANK = MPI.COMM_WORLD.Get_rank()

n = int(sys.argv[1])
a = np.zeros(n)

if RANK == 0:
	a[:] = np.random.random_sample(n)
	MPI.COMM_WORLD.Send(a, dest=1)
elif RANK == 1:
	MPI.COMM_WORLD.Recv(a, source=0)
	print a



