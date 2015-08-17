from mpi4py import MPI
RANK = MPI.COMM_WORLD.Get_rank()

if RANK % 2 == 0:
	print "Hello from process {}".format(RANK)
else:
	print "Goodbye from process {}".format(RANK)
