import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import fftconvolve

def gen_sample(f, n):
    """ generate a discrete sample of f of length 2^n """
    x = np.linspace(0,1,2**n+1)
    return x, f(x)


def plot_mother(b):
    y = np.zeros(len(b)*2+1)
    y[::2] = b
    y[1::2] = -b
    y[-1] = 0
    x = np.linspace(0,1,len(y))
    plt.step(x,y,where="post")
    plt.show()




if __name__ == "__main__":
    # Exercise 4.36
    f = lambda x: np.sin(2*np.pi*x - 5)/np.sqrt(np.abs(x - np.pi/20))
    '''
    for n in xrange(1,11):
        x,y = gen_sample(f,n)
        plt.step(x,y,where="post")
        '''
    plt.subplot(3,1,1)
    plt.title("Original Function")
    x = np.linspace(0,1,1000)
    plt.plot(x,f(x))
    
    # Exercise 4.40
    L = np.ones(2)/np.sqrt(2)
    H = np.array([-1,1])/np.sqrt(2)
    
    n = 10
    
    for l in xrange(1,10):
        x, A = gen_sample(f,n)
        my_list = []
        for i in xrange(l):
            my_list.append(fftconvolve(A,H)[1::2])
            A = fftconvolve(A,L)[1::2]
            i+=1
        my_list.append(A)
        my_list = np.array(my_list[::-1])
        
        plt.subplot(3,1,2)
        plt.title("Approximation")
        plt.step(x[::2**l],my_list[0],where="post")
        b = my_list[1]
        y = np.zeros(len(b)*2+1)
        y[:-1:2] = b
        y[1::2] = -b
        y[-1] = 0
        x1 = np.linspace(0,1,len(y))
        plt.subplot(3,1,3)
        plt.title("Approximation and Detail")
        plt.step(x[::2**l],my_list[0],where="post")
        plt.step(x1,y,where="post")
    plt.show()

