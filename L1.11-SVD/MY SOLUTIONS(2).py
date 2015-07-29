def svd_approx(A, k):
    '''
    A - np.ndarray of size mxn
    k - rank 
    
    returns best rank k approximation to A with respect to the induced 2-norm
    '''
    U,s,Vt = svd(A, full_matrices=False)
    S = np.diag(s[:k])
    Ahat = U[:,:k].dot(S).dot(Vt[:k,:])
    print norm(A-Ahat)
    return Ahat

def lowest_rank_approx(A,e):
    U,s,Vt = svd(A, full_matrices=False)
    k = np.where(s<e)[0][0]
    S = np.diag(s[:k])
    return U[:,:k].dot(S).dot(Vt[:k,:])
	
img_red = plt.imread("hubble_image.jpg")[:,:,0].astype(float)
img_green = plt.imread("hubble_image.jpg")[:,:,1].astype(float)
img_blue = plt.imread("hubble_image.jpg")[:,:,2].astype(float)

original_img = plt.imread("hubble_image.jpg").astype(float)

e = 200

adjust = 255 + np.zeros_like(original_img)

img = np.copy(original_img)
img[:,:,0] = lowest_rank_approx(img_red, e)
img[:,:,1] = lowest_rank_approx(img_green, e)
img[:,:,2] = lowest_rank_approx(img_blue, e)

img = np.round(img)

plt.subplot(1,2,1)
plt.imshow(adjust - original_img)

plt.subplot(1,2,2)
plt.imshow(adjust - img)

plt.show()