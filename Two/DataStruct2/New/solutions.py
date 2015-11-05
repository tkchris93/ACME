# name this file 'solutions.py'
"""Volume II Lab 5: Data Structures II (Trees)
Tanner Christensen
<Class>
<Date>
"""

from Trees import BST
from Trees import AVL
from LinkedLists import LinkedList
from WordList import create_word_list
import time
import numpy as np
from matplotlib import pyplot as plt

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
    def _search(node, data):
        while node is not None:
            if node.data == data:
                return data
            else:
                return _search(node.next, data)
        raise ValueError(str(data) + " is not in the list.")
    current = linkedlist.head
    return _search(current, data)

# Problem 2: Implement BST.insert() in Trees.py.


# Problem 3: Implement BST.remove() in Trees.py


# Problem 4: Test build and search speeds for LinkedList, BST, and AVL objects.
def plot_times(filename="English.txt", start=500, stop=5500, step=500):
    """Vary n from 'start' to 'stop', incrementing by 'step'. At each
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
        start (int): the lower bound on the sample interval.
        stop (int): the upper bound on the sample interval.
        step (int): the space between points in the sample interval.
    
    Returns:
        Show the plot, but do not return any values.
    """
    ll = LinkedList()
    bst = BST()
    avl = AVL()

    ll_add = []
    bst_add = []
    avl_add = []

    ll_search = []
    bst_search = []
    avl_search = []

    for items in range(start,stop,step):
        wordlist = create_word_list()[:items]
        
        ll = LinkedList()
        before = time.time()
        for i in xrange(items):
            ll.add(wordlist[i])
        after = time.time()
        ll_add.append(after - before)
    
        random_indices = np.random.random_integers(0,items,5)
        temp = []
        for i in xrange(len(random_indices)):
            before = time.time()
            iterative_search(ll, wordlist[random_indices[i]]) 
            after = time.time()
            temp.append(after - before)
        ll_search.append(sum(temp)/len(temp))
    
        bst = BST()
        before = time.time()
        for i in xrange(items):
            bst.insert(wordlist[i])
        after = time.time()
        bst_add.append(after - before)

        temp = []
        for i in xrange(len(random_indices)):
            before = time.time()
            bst.find(wordlist[random_indices[i]])
            after = time.time()
            temp.append(after - before)
        bst_search.append(sum(temp)/len(temp))

        avl = AVL()
        before = time.time()
        for i in xrange(items):
            avl.insert(wordlist[i])
        after = time.time()
        avl_add.append(after - before)
        
        temp = []
        for i in xrange(len(random_indices)):
            before = time.time()
            avl.find(wordlist[random_indices[i]])
            after = time.time()
            temp.append(after - before)
        avl_search.append(sum(temp)/len(temp))
    
    plt.subplot(1,2,1)
    plt.title("Build Times")
    plt.plot(ll_add, "b", label="Single-Linked List")
    plt.plot(bst_add, "g", label="Binary Search Tree")
    plt.plot(avl_add, "r", label ="AVL Tree")
    plt.legend(loc="upper left")
    plt.subplot(1,2,2)
    plt.title("Search Times")
    plt.plot(ll_search, "b", label="Single-Linked List")
    plt.plot(bst_search, "g", label="Binary Search Tree")
    plt.plot(avl_search, "r", label="AVL Tree")
    plt.legend(loc="upper left")
    plt.show()
    plt.close()
    
    return ll_add, ll_search, bst_add, bst_search, avl_add, avl_search

# =============================== END OF FILE =============================== #
