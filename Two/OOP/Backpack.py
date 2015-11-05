# Backpack.py
"""Volume II Lab 2: Object Oriented Programming (Auxiliary file)
Modify this file for problems 1 and 3.
Tanner Christensen
Sept 4, 2015
"""

# Problem 1: Modify this class. Add 'name' and max_size' attributes, modify
#   the put() method, and add a dump() method. Remember to update docstrings.
class Backpack:
    """A Backpack object class. Has a color and a list of contents.
    
    Attributes:
        color (str): the color of the backpack.
        contents (list): the contents of the backpack.
        name (str): the name of the backpack.
        max_size (int): the maximum number of things the backpack can hold.
    """
    
    def __init__(self, color='black', name='backpack', max_size=5):
        """Constructor for a backpack object.
        Set the color, name, and max_size and initialize the contents list.
        
        Inputs:
            color (str, opt): the color of the backpack. Defaults to 'black'.
            name (str, opt): the name of the backpack. Deaults to 'backpack'.
            max_size (int, opt): the maximum number of things the backpack can hold. 
                                  Defaults to 5.
        
        Returns:
            A backpack object wth no contents.
        """
        
        self.color = color
        self.contents = []
        self.name = name
        self.max_size = max_size
    
    def dump(self):
        """Empties backpack"""
        self.contents = []
    
    def put(self, item):
        """Add 'item' to the backpack's content list."""
        if len(self.contents) == self.max_size:
            print "Backpack Full."
        else:    
            self.contents.append(item)
    
    def take(self, item):
        """Remove 'item' from the backpack's content list."""
        self.contents.remove(item)
    
    # -------------------- Magic Methods (Problem 3) -------------------- #
    
    def __add__(self, other):
        """Add the contents of 'other' to the contents of 'self'.
        Note that the contents of 'other' are unchanged.
        
        Inputs:
            self (Backpack): the backpack on the left-hand side
                of the '+' addition operator.
            other (Backpack): The backpack on the right-hand side
                of the '+' addition operator.
        """
        self.contents = self.contents + other.contents
    
    def __lt__(self, other):
        """Compare two backpacks. If 'self' has fewer contents
        than 'other', return True. Otherwise, return False.
        
        Inputs:
            self (Backpack): the backpack on the left-hand side
                of the '<' comparison operator.
            other (Backpack): The backpack on the right-hand side
                of the '<' comparison operator.
        """    
        return len(self.contents) < len(other.contents)
    
    # Problem 3: write the __str__ and __eq__ magic methods for the Backpack.
    def __str__(self):
        """String Representation: a list of the backpack's attributes.
        
        Examples:                           |
            >>> b = Backpack()              |   Or,
            >>> b.put('something')          |
            >>> b.put('something else')     |   >>> c = Backpack('red','Bob',3)
            >>> print(b)                    |   >>> print(c)
            Name:       backpack            |   Name:       Bob
            Color:      black               |   Color:      red
            Size:       2                   |   Size:       0
            Max Size:   5                   |   Max Size:   3
            Contents:                       |   Contents:   Empty
                        something           |
                        something else      |
        """
        s = "Name:\t\t" + self.name + '\n'
        s += "Color:\t\t" + self.color + '\n'
        s += "Size:\t\t" + str(len(self.contents)) + '\n'
        s += "Max Size:\t" + str(self.max_size) + '\n'
        
        if len(self.contents) == 0:
            s += "Contents:\tEmpty\n"
        else:
            s += "Contents:\n"
            for i in self.contents:
                s+= "\t\t" + str(i) + '\n'
        return s
        
    def __eq__(self,other):
        """Backpacks are equal if they have the same name, color and contents"""
        if (self.name == other.name) and (self.color == other.color):
            if set(self.contents) == set(other.contents):
                return True
            else:
                return False
        else:
            return False

# Study this example of inheritance. You are not required to modify it.
class Knapsack(Backpack):
    """A Knapsack object class. Inherits from the Backpack class.
    A knapsack is smaller than a backpack and can be tied closed.
    
    Attributes:
        color (str): the color of the knapsack.
        name (str): the name of the knapsack.
        max_size (int): the maximum number of items that can fit in the
            knapsack.
        contents (list): the contents of the backpack.
        closed (bool): whether or not the knapsack is tied shut.
    """
    
    def __init__(self, color='brown', name='knapsack', max_size=3):
        """Constructor for a knapsack object. A knapsack only holds 3 item by
        default instead of 5. Use the Backpack constructor to initialize the
        name and max_size attributes.
        
        Inputs:
            color (str, opt): the color of the knapsack. Defaults to 'brown'.
            name (str, opt): the name of the knapsack. Defaults to 'knapsack'.
            max_size (int, opt): the maximum number of items that can be
                stored in the knapsack. Defaults to 3.
        
        Returns:
            A knapsack object with no contents.
        """
        
        Backpack.__init__(self, color, name, max_size)
        self.closed = True
    
    def put(self, item):
        """If the knapsack is untied, use the Backpack put() method."""
        if self.closed:
            print "Knapsack closed!"
        else:
            Backpack.put(self, item)
    
    def take(self, item):
        """If the knapsack is untied, use the Backpack take() method."""
        if self.closed:
            print "Knapsack closed!"
        else:
            Backpack.take(self, item)
    
    def untie(self):
        """Untie the knapsack."""
        self.closed = False
    
    def tie(self):
        """Tie the knapsack."""
        self.closed = True

# ============================== END OF FILE ================================ #
