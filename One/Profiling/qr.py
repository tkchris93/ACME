import numpy as np
from scipy import linalg as la
def qr(A):
	norm = la.norm
	ncols = A.shape[1]
	Q = A.copy()
	R = np.zeros((ncols, ncols))
	for i in range(ncols):
		R[i, i] = norm(Q[:, i])
		Q[:, i] = Q[:, i]/R[i, i]
		for j in range(i+1, ncols):
			R[i, j] = Q[:, j].dot(Q[:, i])
			Q[:,j] = Q[:,j]-R[i, j]*Q[:,i]
	return Q, R
