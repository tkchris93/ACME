import numpy as np
import scipy.stats as ss
from matplotlib import pyplot as plt

# BETA(1,1)

plt.subplot(2,1,1)
x = np.linspace(0,1,200)
y1 = np.ones(x.shape)
plt.title("Beta(1,1)")
plt.plot(x,y1)

# Beta(1,1) mean=(1/2) var=(1/12)
x = np.linspace(0,1,200)
y = []
mu = 1/2.
var = 1/12.
for n in [1,2,4,8,16,32]:
    coefficient = 1/(np.sqrt(2*np.pi*var/n))
    y.append(coefficient*np.exp(-1*(x - mu)**2/(2*var/n)))

for i in y: 
    plt.plot(x,i)
    
for n in [1,2,4,8,16,32]:
    nums = ss.beta.rvs(1,1,size=(n,1000))
    #sum up the columns and multiply by 1/n
    x_bar = (1./n)*nums.sum(axis=0)
    plt.hist(x_bar,normed=True)    

# BETA(1,4)
plt.subplot(2,1,2)
x = np.linspace(0,1,200)
y2 = 4*(1-x)**3
plt.title("Beta(1,4)")
plt.plot(x,y2)

# Beta(1,1) mean=(1/2) var=(1/12)
x = np.linspace(0,1,200)
y = []
mu = 1/5.
var = 3/75.
for n in [1,2,4,8,16,32]:
    coefficient = 1/(np.sqrt(2*np.pi*var/n))
    y.append(coefficient*np.exp(-1*(x - mu)**2/(2*var/n)))

for i in y: 
    plt.plot(x,i)
    
for n in [1,2,4,8,16,32]:
    nums = ss.beta.rvs(1,4,size=(n,1000))
    #sum up the columns and multiply by 1/n
    x_bar = (1./n)*nums.sum(axis=0)
    plt.hist(x_bar,normed=True)   
    
plt.show()
