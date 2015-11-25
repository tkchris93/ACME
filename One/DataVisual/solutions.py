#Implement this function
import numpy as np
from matplotlib import pyplot as plt

def problemOne():
    '''
    Order and plot the data as a horizontal bar chart.
    '''
    male = np.array([179.2,160.0,177.8,178.9,178,176,172.5,165.6,170.8,183.2,182.4,164,163.6,175.4,174,176.1,165.7])
    female = np.array([167.6,142.2,164.5,165.3,165,164,158,154.9,157.4,168.4,168,151,151.4,164,158.9,162.1,155.2])
    country = 'Austria', 'Bolivia', 'England', 'Finland', 'Germany', 'Hungary', 'Japan','North Korea', 'South Korea', 'Montenegro', 'Norway', 'Peru','Sri Lanka', 'Switzerland', 'Turkey', 'U.S.', 'Vietnam'
    male_mask = np.argsort(male)
    female_mask = np.argsort(female)
    
    pos = np.arange(len(country)) + .5
    plt.barh(pos, male[male_mask], align='center')
    plt.yticks(pos, country[male_mask])
    plt.show()
    
# Implement this function
def problemTwo():
    '''
    Plot some histograms with white reference lines.  Do this for 20 bins,
    10 bins, 5 bins, and 3 bins
    '''
    raise NotImplementedError("Problem 2 not implemented.")

# Implement this function
def problemThree():
    '''
    Plot y = x^2 * sin(x) using 1000 data points and x in [0,100]
    '''
    raise NotImplementedError("Problem 3 not implemented.")

# Implement this function
def problemFour():
    '''
    Plot a scatter plot of the average heights of men against women
    using the data from problem 1.
    '''
    raise NotImplementedError("Problem 4 not implemented.")
    
# Implement this function
def problemFive():
    '''
    Plot a contour map of z = sin(x) + sin(y) where x is in [0,12*pi] and
    y is in [0,12*pi]
    '''
    raise NotImplementedError("Problem 5 not implemented.")
    
# Implement this function
def problemSix():
    '''
    Plot each data set.
    '''
    dataI = np.array([[10,8.04],[8.,6.95],[13.,7.58],[9,8.81],[11.,8.33],[14.,9.96],[6.,7.24],[4.,4.26],[12.,10.84],[7.,4.82],[5.,5.68]])
    dataII = np.array([[10,9.14],[8.,8.14],[13.,8.74],[9,8.77],[11.,9.26],[14.,8.10],[6.,6.13],[4.,3.10],[12.,9.13],[7.,7.26],[5.,4.74]])
    dataIII = np.array([[10,7.46],[8.,6.77],[13.,12.74],[9,7.11],[11.,7.81],[14.,8.84],[6.,6.08],[4.,5.39],[12.,8.15],[7.,6.42],[5.,5.73]])
    dataIV = np.array([[8.,6.58],[8.,5.76],[8.,7.71],[8.,8.84],[8.,8.47],[8.,7.04],[8.,5.25],[19.,12.50],[8.,5.56],[8.,7.91],[8.,6.89]])
    raise NotImplementedError("Problem 6 not implemented.")

# Implement this function
def problemSeven():
    '''
    Change the surface to a heatmap or a contour plot.  Return a string
    of the benefits of each type of visualization.
    '''
    raise NotImplementedError("Problem 7 not implemented.")

# Implement this function
def problemEight():
    '''
    Plot y = x^2 * sin(x) where x is in [0,100] and adjust to y limit to be
    [-10^k,10^k] for k = 0,1,2,3,4.
    '''
    raise NotImplementedError("Problem 8 not implemented.")


# Implement this function
def problemNine():
    '''
    Simplify one of your previous graphs.
    '''
    raise NotImplementedError("Problem 10 not implemented.")

# Implement this function
def problemTen():
    '''
    Plot the Bernstein polynomials for v,n in [0,3] as small multiples
    and as the cluttered version.
    '''
    raise NotImplementedError("Problem 11 not implemented.")
