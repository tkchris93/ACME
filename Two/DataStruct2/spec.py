# name this file 'solutions.py'
"""Volume II Lab 5: Data Structures II (Trees)
<Name>
<Class>
<Date>
"""

from Trees import BST
from Trees import AVL

def iterative_search(linkedlist, data):
    """Find the node containing 'data' using an iterative approach.
    If there is no such node in the list, or if the list is empty,
    raise a ValueError with error message "<data> is not in the list."
    
    Inputs:
        linkedlist (LinkedList): a linked list object
        data: the data to find in the list.
    
    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    # Start the search at the head.
    current = linkedlist.head
    
    # Iterate through the list, checking the data of each node.
    while current is not None:
        if current.data == data:
            return current
        current = current.next
    
    # If 'current' no longer points to a Node, raise a value error.
    raise ValueError(str(data) + " is not in the list.")


# Problem 1: rewrite iterative_search() using recursion.
def recursive_search(linkedlist, data):
    """Find the node containing 'data' using a recursive approach.
    If there is no such node in the list, raise a ValueError with error
    message "<data> is not in the list."
    
    Inputs:
        linkedlist (LinkedList): a linked list object
        data: the data to find in the list.
    
    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    raise NotImplementedError("Problem 1 incomplete")


# Problem 2: Implement BST.insert() in Trees.py.


# Problem 3: Implement BST.remove() in Trees.py


# Problem 4: Test build and search speeds for LinkedList, BST, and AVL objects.
def plot_times(filename="English.txt"):
    """Vary n from 500 to 5000, inclusive, incrementing by 500. At each
    iteration, use the create_word_list() from the 'WordList' module to
    generate a list of n randomized words from the specified file.
    
    Time (separately) how long it takes to load a LinkedList, a BST, and
    an AVL with the data set.
    
    Choose 5 random words from the data set. Time how long it takes to
    find each word in each object. Calculate the average search time for
    each object.
    
    Create one plot with two subplots. In the first subplot, plot the
    number of words in each dataset against the build time for each object.
    In the second subplot, plot the number of words against the search time
    for each object.
    
    Inputs:
        filename (str): the file to use in creating the data sets.
    
    Returns:
        Show the plot, but do not return any values.
    """
    raise NotImplementedError("Problem 4 incomplete")

# =============================== END OF FILE =============================== #