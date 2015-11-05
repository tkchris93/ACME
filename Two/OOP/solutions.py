"""Volume II Lab 2: Object Oriented Programming
Tanner Christensen
Sept 4, 2015
"""

from Backpack import Backpack
import numpy as np

# Problem 1: Modify the 'Backpack' class in 'Backpack.py'.

# Study the 'Knapsack' class in 'Backpack.py'. You should be able to create a 
#   Knapsack object after finishing problem 1.


# Problem 2: Write a 'Jetpack' class that inherits from the 'Backpack' class.
class Jetpack(Backpack):
    """A Jetpack object class. Inherits from the Backpack class.
    
    Attributes:
        color (str): color of jetpack
        contents (list): list of contents
        name (str): name of jetpack
        max_size (int): maximum number of contents the jetpack can hold
        fuel (int): amount of fuel in the jetpack.
    """
    
    def __init__(self, color='silver', name='jetpack', max_size=2, fuel=10):
        """Constructor for a jetpack object.
        Set the color, name, and max_size and initialize the contents list.
        
        Inputs:
            color (str, opt): the color of the jetpack. Defaults to 'black'.
            name (str, opt): the name of the jetpack. Deaults to 'jetpack'.
            max_size (int, opt): the maximum number of things the jetpack can hold. 
                                  Defaults to 5.
            fuel (int, opt): amount of fuel in the jetpack. Defaults to 10.
        
        Returns:
            A jetpack object wth no contents.
        """
        self.color = color
        self.contents = []
        self.name = name
        self.max_size = max_size
        self.fuel = fuel
        
    def fly(self, f):
        """Use 'f' fuel to fly.
        Let user know if they are attempting to use too much fuel.
        
        Inputs:
            f (int): amount of fuel to burn
        """
        if f > self.fuel:
            print "Not enough fuel!"
        else:
            self.fuel -= f
    
    def dump(self):
        """Empties backpack and fuel."""
        self.contents = []
        self.fuel = 0

# Problem 3: write __str__ and __eq__ for the 'Backpack' class in 'Backpack.py'


# Problem 4: Write a ComplexNumber class.
class ComplexNumber(object):
    """A Complex number object class. Has a real and imaginary part.
    
    Attributes:
        real (int): the real part of the complex number.
        imag (int): the imaginary part of the complex number.
    """
    def __init__(self, real, imag):
        """Constructor for ComplexNumber object
        
        Inputs:
            real (int): the real part of the complex number.
            imag (int): the imaginary part of the complex number.
            
        Returns:
            a ComplexNumber object
        """
        self.real = real
        self.imag = imag
        
    def conjugate(self):
        """Calculates the conjugate and returns the a ComplexNumber object."""
        return ComplexNumber(self.real, -self.imag)
    
    def norm(self):
        """Calculates and returns the norm of a ComplexNumber."""
        return np.sqrt(self.real**2 + self.imag**2)
        
    def __add__(self, other):
        """Add two ComplexNumber objects"""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
        
    def __sub__(self, other):
        """Subtract two ComplexNumber objects"""
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
        
    def __mul__(self, other):
        """Multiply two ComplexNumber objects"""
        temp_real = self.real*other.real - self.imag*other.imag
        temp_imag = self.real*other.imag + self.imag*other.real
        return ComplexNumber(temp_real, temp_imag)
        
    def __div__(self, other):
        """Divide two ComplexNumber objects"""
        num = self.__mul__(other.conjugate())
        temp_real = num.real/float(other.norm()**2)
        temp_imag = num.imag/float(other.norm()**2)
        return ComplexNumber(temp_real, temp_imag)
# =============================== END OF FILE =============================== #
