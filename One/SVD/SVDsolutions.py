
# coding: utf-8

# In[79]:

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from scipy import linalg as la


# In[82]:

'''
- plt.imshow() doesn't like RGB values between 0-255.  It does some weird inverted thing.
- if you are getting speckles that shouldn't be there, that means that you have values that
  are less than 0 or greater than 1 (outside the correct range)
- plt.imread() will read in jpg as numbers between 0-255. It will read png as numbers between 0-1.
- for some reason, our algorithm won't work on numbers between 0-1.  So change the numbers to 0-255 
  then back to 0-1 before plotting.
- QUESTION FOR JEFF OR SOMEONE SMART: So are the U,s,Vt arrays the ones that are sent across the network?
'''

def svd_approx(A, k):
    '''
    A - np.ndarray of size mxn
    k - rank 
    
    returns best rank k approximation to A with respect to the induced 2-norm
    '''
    U,s,Vt = la.svd(A, full_matrices=False)
    S = np.diag(s[:k])
    u1,s1,vt1 = U[:,:k],S[:k,:k],Vt[:k,:]
    diff = (u1.nbytes + np.diag(s1).nbytes + vt1.nbytes) - A.nbytes
    if diff > 0:
        print "WARNING: Given parameters do not result in compressed data."
    Ahat = U[:,:k].dot(S).dot(Vt[:k,:])
    return Ahat

def lowest_rank_approx(A,e):
    U,s,Vt = la.svd(A, full_matrices=False)
    k = np.where(s<e)[0][0]
    S = np.diag(s[:k])
    u1,s1,vt1 = U[:,:k],S[:k,:k],Vt[:k,:]
    diff = (u1.nbytes + np.diag(s1).nbytes + vt1.nbytes) - A.nbytes
    if diff > 0:
        print "WARNING: Given parameters do not result in compressed data."
    return U[:,:k].dot(S).dot(Vt[:k,:])

def compress(filename, x, mode='error'):
    #check which mode you are in
    if mode == "error":
        func = lowest_rank_approx
    elif mode == "rank":
        func = svd_approx
    else:
        print "invalid mode!  Valid modes are 'error' and 'rank'."
        return
    
    #check the filetype and read in data in chunks of R,G,B
    if filename[-4:] == ".jpg":
        img_red = plt.imread(filename)[:,:,0].astype(float)
        img_green = plt.imread(filename)[:,:,1].astype(float)
        img_blue = plt.imread(filename)[:,:,2].astype(float)
        original_img = plt.imread(filename).astype(float)
    elif filename[-4:] == ".png":
        img_red = 255 * plt.imread(filename)[:,:,0].astype(float)
        img_green = 255 * plt.imread(filename)[:,:,1].astype(float)
        img_blue = 255 * plt.imread(filename)[:,:,2].astype(float)
        original_img = 255 * plt.imread(filename).astype(float)
    else:
        print "invalid filetype! Only .jpg and .png supported."
    
    img = np.copy(original_img)
    img[:,:,0] = func(img_red, x)
    img[:,:,1] = func(img_green, x)
    img[:,:,2] = func(img_blue, x)
    
    img = np.round(img)/255.
    original_img /= 255.

    #clean up numbers less than 0 and numbers greater than 1
    img[img<0] = 0.
    img[img>1] = 1.
    
    plt.subplot(2,1,1)
    plt.imshow(original_img)

    plt.subplot(2,1,2)
    plt.imshow(img)

    plt.show()

    return img


# In[82]:




# In[82]:




# In[82]:




# In[82]:




# In[37]:




# In[68]:




# In[82]:




# In[81]:




# In[ ]:



