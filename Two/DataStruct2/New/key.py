# solutions.py
"""Volume II Lab 5: Data Structures II (Trees)
Solutions file. Written by Shane A. McQuarrie.
"""

# ============================== Trees.py ============================== #
# Modify this file for problems 2 and 3

class BSTNode(object):
    """A Node class for Binary Search Trees. Contains some data, a
    reference to the parent node, and references to two child nodes.
    """
    def __init__(self, data):
        """Construct a new node and set the data attribute. The other
        attributes will be set when the node is added to a tree.
        """
        self.data = data
        self.prev = None        # A reference to this node's parent node
        self.left = None        # self.left.data < self.data
        self.right = None       # self.data < self.right.data
        
    def __str__(self):
        """String representation: the data contained in the node."""
        return str(self.data)

# Modify this class for problems 2 and 3
class BST(object):
    """Binary Search Tree data structure class.
    The first node is referenced to by 'root'.
    """
    def __init__(self):
        """Initialize the root attribute."""
        self.root = None
    
    def find(self, data):
        """Return the node containing 'data'. If there is no such node in the
        tree, raise a ValueError with error message "<data> is not in the tree."
        """
        # First, check to see if the tree is empty
        if self.root is None:
            raise ValueError(str(data) + " is not in the tree.")
        
        # Define a recursive function to traverse the tree
        def _step(current, item):
            """Recursively step through the tree until the node containing
            'item' is found. If there is no such node, raise a Value Error.
            """
            if current is None:                     # Base case 1: dead end
                raise ValueError(str(data) + " is not in the tree.")
            if item == current.data:                # Base case 2: data matches
                return current
            if item < current.data:                 # Step to the left
                return _step(current.left,item)
            else:                                   # Step to the right
                return _step(current.right,item)
        
        # Start the recursion on the root of the tree.
        return _step(self.root, data)
    
    # Problem 2: Implement BST.insert()
    def insert(self, data):
        """Insert a new node containing 'data' at the appropriate location.
        Do not allow for duplicates in the tree: if there is already a node
        containing 'data' in the tree, raise a ValueError.
        
        Example:
            >>> b = BST()       |   >>> b.insert(1)     |       (4)
            >>> b.insert(4)     |   >>> print(b)        |       / \
            >>> b.insert(3)     |   [4]                 |     (3) (6)
            >>> b.insert(6)     |   [3, 6]              |     /   / \
            >>> b.insert(5)     |   [1, 5, 7]           |   (1) (5) (7)
            >>> b.insert(7)     |   [8]                 |             \
            >>> b.insert(8)     |                       |             (8)
        """
        
        def _find_parent(current, item):
            """Recursively descend through the tree to find the node that
            should be the parent of the new node. Do not allow for duplicates.
            """
            if item == current.data:                # Base case 1: duplicate
                raise ValueError(str(item) + " is already in the tree.")
            if current is None:                     # Base case 2: failure
                raise ValueError("_find_parent() failed for " + str(item))
            if item < current.data:                 # Step to the left
                if current.left:
                    return _find_parent(current.left,item)
                else:                               # Base case: parent found
                    return current
            else:                                   # Step to the right
                if current.right:
                    return _find_parent(current.right,item)
                else:                               # Base case: parent found
                    return current
        
        n = BSTNode(data)                           # Make a new node
        if self.root is None:                       # Case 1: empty tree
            self.root = n                               # reset the root
        else:                                       # Case 2: use _find_parent
            parent = _find_parent(self.root,data)       # Get the parent
            if data < parent.data:                      # Insert as left child
                parent.left = n
            else:                                       # Insert as right child
                parent.right = n
            n.prev = parent                             # Double link
    
    # Problem 3: Implement BST.remove()
    def remove(self, data):
        """Remove the node containing 'data'. Consider several cases:
            - The tree is empty
            - The target is the root:
                - The root is a leaf node, hence the only node in the tree
                - The root has one child
                - The root has two children
            - The target is not the root:
                - The target is a leaf node
                - The target has one child
                - The target has two children
            If the tree is empty, or if there is no node containing 'data',
            raise a ValueError.
        
        Examples:
        
            >>> print(b)        |   >>> b.remove(1)     |   [3]
            [4]                 |   >>> b.remove(7)     |   [5]
            [3, 6]              |   >>> b.remove(6)     |   [8]
            [1, 5, 7]           |   >>> b.remove(4)     |
            [8]                 |   >>> print(b)        |
        """
        
        def _predecessor(node):
            """Find the next-smallest node in the tree by travelling
            right once, then left as far as possible.
            """
            if node.right is None:          # Function called inappropriately
                raise ValueError("IOP problem")
            node = node.right               # Step right once
            while node.left:
                node = node.left            # Step right until done
            return node
        
        # Case 1: the tree is empty
        if self.root is None:
            raise ValueError("The tree is empty.")
        # Case 2: the target is the root
        target = self.find(data)
        if target == self.root:
            # Case 2a: no children
            if not self.root.left and not self.root.right:
                self.__init__()
            # Case 2b: one child
            if not target.right:
                self.root = target.left
            elif not target.left:
                self.root = target.right
            # Case 2c: two children
            else:
                pred = _predecessor(target)
                self.remove(pred.data)
                target.data = pred.data
            # reset the new root's prev to None
            if self.root:
                self.root.prev = None
        # Case 3: the target is not the root
        else:
            # Case 3a: no children
            if not target.left and not target.right:
                parent = target.prev
                if target.data < parent.data:
                    parent.left = None
                elif target.data > parent.data:
                    parent.right = None
            # Case 3b: one child
            elif not target.right:
                parent = target.prev
                if parent.right == target:
                    parent.right = target.left
                elif parent.left == target:
                    parent.left = target.left
                target.left.prev = parent
            elif not target.left:
                parent = target.prev
                if parent.right == target:
                    parent.right = target.right
                elif parent.left == target:
                    parent.left = target.right
                target.right.prev = parent
            # Case 3c: two children
            else:
                pred = _predecessor(target)
                self.remove(pred.data)
                target.data = pred.data
    
    def __str__(self):
        """String representation: a hierarchical view of the BST.
        Do not modify this function, but use it often to test this class.
        (this function uses a depth-first search; can you explain how?)
        
        Example:  (3)
                  / \     '[3]          The nodes of the BST are printed out
                (2) (5)    [2, 5]       by depth levels. The edges and empty
                /   / \    [1, 4, 6]'   nodes are not printed.
              (1) (4) (6)
        """
        
        if self.root is None:                   # Print an empty tree
            return "[]"
        # If the tree is nonempty, create a list of lists.
        # Each inner list represents a depth level in the tree.
        str_tree = [list() for i in xrange(_height(self.root) + 1)]
        visited = set()                         # Track visited nodes
        
        def _visit(current, depth):
            """Add the data contained in 'current' to its proper depth level
            list and mark as visited. Continue recusively until all nodes have
            been visited.
            """
            str_tree[depth].append(current.data)
            visited.add(current)
            if current.left and current.left not in visited:
                _visit(current.left, depth+1)  # travel left recursively (DFS)
            if current.right and current.right not in visited:
                _visit(current.right, depth+1) # travel right recursively (DFS)
        
        _visit(self.root,0)                     # Load the list of lists.
        out = ""                                # Build the final string.
        for level in str_tree:
            if level != list():                 # Ignore empty levels.
                out += str(level) + "\n"
            else:
                break
        return out

class AVL(BST):
    """AVL Binary Search Tree data structure class. Inherits from the BST
    class. Includes methods for rebalancing upon insertion. If your
    BST.insert() method works correctly, this class will work correctly.
    Do not modify.
    """
    def _checkBalance(self, n):
        if abs(_height(n.left) - _height(n.right)) >= 2:
            return True
        else:
            return False
    
    def _rotateLeftLeft(self, n):
        temp = n.left
        n.left = temp.right
        if temp.right:
            temp.right.prev = n
        temp.right = n
        temp.prev = n.prev
        n.prev = temp
        if temp.prev:
            if temp.prev.data > temp.data:
                temp.prev.left = temp
            else:
                temp.prev.right = temp
        if n == self.root:
            self.root = temp
        return temp
    
    def _rotateRightRight(self, n):
        temp = n.right
        n.right = temp.left
        if temp.left:
            temp.left.prev = n
        temp.left = n
        temp.prev = n.prev
        n.prev = temp
        if temp.prev:
            if temp.prev.data > temp.data:
                temp.prev.left = temp
            else:
                temp.prev.right = temp
        if n == self.root:
            self.root = temp
        return temp
    
    def _rotateLeftRight(self, n):
        temp1 = n.left
        temp2 = temp1.right
        temp1.right = temp2.left
        if temp2.left:
            temp2.left.prev = temp1
        temp2.prev = n
        temp2.left = temp1
        temp1.prev = temp2
        n.left = temp2
        return self._rotateLeftLeft(n)
    
    def _rotateRightLeft(self, n):
        temp1 = n.right
        temp2 = temp1.left
        temp1.left = temp2.right
        if temp2.right:
            temp2.right.prev = temp1
        temp2.prev = n
        temp2.right = temp1
        temp1.prev = temp2
        n.right = temp2
        return self._rotateRightRight(n)
    
    def _rebalance(self,n):
        """Rebalance the subtree starting at the node 'n'."""
        if self._checkBalance(n):
            if _height(n.left) > _height(n.right):
                # Left Left case
                if _height(n.left.left) > _height(n.left.right):
                    n = self._rotateLeftLeft(n)
                # Left Right case
                else:
                    n = self._rotateLeftRight(n)
            else:
                # Right Right case
                if _height(n.right.right) > _height(n.right.left):
                    n = self._rotateRightRight(n)
                # Right Left case
                else:
                    n = self._rotateRightLeft(n)
        return n
    
    def insert(self, data):
        """Insert a node containing 'data' into the tree, then rebalance."""
        # insert the data like usual
        BST.insert(self, data)
        # rebalance from the bottom up
        n = self.find(data)
        while n:
            n = self._rebalance(n)
            n = n.prev
    
    def remove(self, *args):
        """Disable remove() to keep the tree in balance."""
        raise NotImplementedError("remove() has been disabled for this class.")

def _height(current):
    """Calculate the height of a given node by descending recursively until
    there are no further child nodes. Return the number of children in the
    longest chain down. Helper function for the AVL class and BST.__str__.
    Do not modify.
                                node | height
    Example:  (c)                  a | 0
              / \                  b | 1
            (b) (f)                c | 3
            /   / \                d | 1
          (a) (d) (g)              e | 0
                \                  f | 2
                (e)                g | 0
    """
    if current is None:     # Base case: the end of a branch.
        return -1           # Otherwise, descend down both branches.
    return 1 + max(_height(current.right), _height(current.left))

# ============================== solutions.py ============================== #

# from Trees import BST
# from Trees import AVL
from WordList import create_word_list
from time import time
from matplotlib import pyplot as plt
from random import randint


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
    def _step(current):
        """Check the current node, and step right if not found."""
        if current is None:         # Base case 1: dead end
            raise ValueError(str(data) + " is not in the list.")
        if current.data == data:    # Base case 2: the data matches
            return current
        else:                       # Recurse if not found
            return _step(current.next)
    
    return _step(linkedlist.head)


# Problem 2: Implement BST.insert() in BST.py.


# Problem 3: Implement BST.remove() in BST.py


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
    
    Returns:
        Show the plot, but do not return any values.
    """
    
    # Initialize lists to hold results
    lls_build, lls_search = list(), list()
    bst_build, bst_search = list(), list()
    avl_build, avl_search = list(), list()
    
    # Get the values [start, start + step, ..., stop - step]
    domain = list()
    for n in xrange(start,stop,step):
    
        # Initialize wordlist and data structures
        word_list = create_word_list(filename)[:n]
        bst = BST()
        avl = AVL()
        lls = LinkedList()
        
        # Time the singly-linked list build
        start = time()
        for word in word_list:
            lls.add(word)
        lls_build.append(time() - start)
        
        # Time the binary search tree build
        start = time()
        for word in word_list:
            bst.insert(word)
        bst_build.append(time() - start)
        
        # Time the AVL tree build
        start = time()
        for word in word_list:
            avl.insert(word)
        avl_build.append(time() - start)
        
        # Search Times
        search1, search2, search3 = list(), list(), list()
        for i in xrange(5):
            target = word_list[randint(0, n-1)]
            
            # Time LinkedList.find
            start = time()
            iterative_search(lls, target)
            search1.append(time() - start)
            
            # Time BST.find
            start = time()
            bst.find(target)
            search2.append(time() - start)
            
            # Time AVL.find
            start = time()
            avl.find(target)
            search3.append(time() - start)
        
        lls_search.append(sum(search1)/len(search1))
        bst_search.append(sum(search2)/len(search2))
        avl_search.append(sum(search3)/len(search3))
        domain.append(n)
    
    # Plot the data
    plt.subplot(121)
    plt.title("Build Times")
    plt.plot(domain,lls_build,label='Singly-Linked List')
    plt.plot(domain,bst_build,label='Binary Search Tree')
    plt.plot(domain,avl_build,label='AVL Tree')
    plt.ylabel("seconds")
    plt.xlabel("data points")
    plt.legend(loc='upper left')
    
    plt.subplot(122)
    plt.title("Search Times")
    plt.plot(domain,lls_search,label='Singly-Linked List')
    plt.plot(domain,bst_search,label='Binary Search Tree')
    plt.plot(domain,avl_search,label='AVL Tree')
    plt.ylabel("seconds")
    plt.xlabel("data points")
    plt.legend(loc='upper left')
    
    plt.show()


# ============================= END OF SOLUTIONS ============================ #

import inspect

# Simple singly-linked list objects for testing problem 1
class LinkedListNode(object):
    """Simple singly-linked list node. Used to test problem 1."""
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class LinkedList(object):
    """Simple singly-linked list. Used to test problem 1."""
    def __init__(self):
        self.head = None
    def add(self, data):
        """Add a Node containing 'data' to the end of the list."""
        n = LinkedListNode(data)
        if self.head is None: self.head = n
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = n

# Test script
def test(student_module, late=False):
    """Test script. You must import the students file as a module.
    
     5 points for problem 1
    15 points for problem 2
    25 points for problem 3
    15 points for problem 4
    
    Parameters:
        student_module: the imported module for the student's file.
        late (bool, opt): if True, half credit is awarded.
    
    Returns:
        score (int): the student's score, out of 60.
        feedback (str): a printout of results for the student.
    """
    
    def strTest(x,y,m):
        """Test to see if x and y have the same string representation. If
        correct, award a points and return no message. If incorrect, return
        0 and return 'm' as feedback.
        """
        if str(x) == str(y): return 1, ""
        else:
            m += "\n\t\tCorrect response:\n" + str(x)
            m += "\n\t\tStudent response:\n" + str(y)
            return 0, m
    
    def grade(p,m):
        """Manually grade a problem worth 'p' points with error message 'm'."""
        part = -1
        while part > p or part < 0:
            part = int(input("\nScore out of " + str(p) + ": "))
        if part == p: return p, ""
        else: return part, m
    
    s = student_module
    score = 0
    total = 60
    feedback = ""
    
    try:    # Problem 1: 5 points
        feedback += "\n\nProblem 1 (5 points):"
        points = 0
        lls = LinkedList()
        # Check recursive_search on empty list
        try:
            s.recursive_search(lls,1)
            feedback += "\n\trecursive_search() failed on empty list"
        except ValueError: points += 1
        # Check recursive_search for items in list
        lls.add(1); lls.add('a'); lls.add(2)
        p,f = strTest(iterative_search(lls,1), s.recursive_search(lls,1),
                                "\n\trecursive_search(x) failed for x in list")
        points += p; feedback += f
        p,f = strTest(iterative_search(lls,'a'), s.recursive_search(lls,'a'),
                                "\n\trecursive_search(x) failed for x in list")
        points += p; feedback += f
        p,f = strTest(iterative_search(lls,2), s.recursive_search(lls,2),
                                "\n\trecursive_search(x) failed for x in list")
        points += p; feedback += f
        # Check recursive_serach for items not in list
        try:
            s.recursive_search(lls,3)
            feedback += "\n\trecursive_search(x) failed for x not in list"
        except ValueError: points += 1
        # Check that recursion is used somewhere
        text = inspect.getsourcelines(s.recursive_search)[0]; code = ""
        text = text[len(s.recursive_search.__doc__.splitlines()) + 1 :]
        for line in text: code += line
        print "\nStudent Code (check for recursion):\n", code
        p,f = grade(1,"\n\trecursive_search() must use recursion!")
        points *= p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    try:    # Problem 2: 15 points
        feedback += "\n\nProblem 2 (15 points):"
        points = 0
        # Empty tree (0 pts)
        tree1 =   BST()
        tree2 = s.BST()
        p,f = strTest(tree1,tree2,"BST() failed initially!")
        feedback += f
        # Inserting at the root (2 pts)
        tree1.insert(4); tree2.insert(4)
        p,f = strTest(tree1,tree2,"BST.insert(4) failed on root insertion")
        points += (p * 2); feedback += f
        # Inserting nonroot (13 pts)
        tree1.insert(2); tree2.insert(2)
        p,f = strTest(tree1,tree2,"BST.insert(2) failed on nonroot insertion")
        points += p; feedback += f
        tree1.insert(1); tree2.insert(1)
        p,f = strTest(tree1,tree2,"BST.insert(1) failed on nonroot insertion")
        points += p; feedback += f
        tree1.insert(3); tree2.insert(3)
        p,f = strTest(tree1,tree2,"BST.insert(3) failed on nonroot insertion")
        points += p; feedback += f
        tree1.insert(10); tree2.insert(10)
        p,f = strTest(tree1,tree2,"BST.insert(10) failed on nonroot insertion")
        points += p; feedback += f
        tree1.insert(5); tree2.insert(5)
        p,f = strTest(tree1,tree2,"BST.insert(5) failed on nonroot insertion")
        points += p; feedback += f
        tree1.insert(6); tree2.insert(6)
        p,f = strTest(tree1,tree2,"BST.insert(6) failed on nonroot insertion")
        points += p; feedback += f
        tree1.insert(9); tree2.insert(9)
        p,f = strTest(tree1,tree2,"BST.insert(9) failed on nonroot insertion")
        points += p; feedback += f
        tree1.insert(7); tree2.insert(7)
        p,f = strTest(tree1,tree2,"BST.insert(7) failed on nonroot insertion")
        points += p; feedback += f
        tree1.insert(11); tree2.insert(11)
        p,f = strTest(tree1,tree2,"BST.insert(11) failed on nonroot insertion")
        points += p; feedback += f
        # Inserting already existing value (4 pts)
        try:
            tree2.insert(4)
            feedback += "\n\tBST.insert(x) failed for x already in tree"
        except ValueError: points += 1
        try:
            tree2.insert(1)
            feedback += "\n\tBST.insert(x) failed for x already in tree"
        except ValueError: points += 1
        try:
            tree2.insert(7)
            feedback += "\n\tBST.insert(x) failed for x already in tree"
        except ValueError: points += 2
        
        if points < 15:
            feedback += "\n\tAll BST.remove() tests are likely to fail"
            feedback += "\n\t\tunless all BST.insert() tests pass!"
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 3: 30 points
        feedback += "\n\nProblem 3 (30 points):"
        points = 0
        # Remove non-existant (5 pts)
        try:
            tree2.remove(0)
            feedback += "\n\tBST.remove(x) failed for x not in tree"
        except ValueError: points += 2
        try:
            tree2.remove(7.5)
            feedback += "\n\tBST.insert(x) failed for x not in tree"
        except ValueError: points += 3
        # Remove non-root leaf (5 pts)
        tree1.remove(1); tree2.remove(1)
        p,f = strTest(tree1, tree2,
                "BST.remove(1) failed on non-root leaf node")
        points += (p * 2); feedback += f
        tree1.remove(7); tree2.remove(7)
        p,f = strTest(tree1, tree2,
                "BST.remove(7) failed on non-root leaf node")
        points += (p * 3); feedback += f
        # Remove non-root with 1 child (5 pts)
        tree1.remove(2); tree2.remove(2)
        p,f = strTest(tree1, tree2,
                "BST.remove(2) failed on non-root with one child")
        points += (p * 2); feedback += f
        tree1.remove(6); tree2.remove(6)
        p,f = strTest(tree1, tree2,
                "BST.remove(6) failed on non-root with one child")
        points += (p * 3); feedback += f
        # Remove non-root with 2 children (5 pts)
        tree1.remove(10); tree2.remove(10)
        p,f = strTest(tree1, tree2,
                "BST.remove(10) failed on non-root two children")
        points += (p * 3); feedback += f
        tree1.remove(9); tree2.remove(9)
        p,f = strTest(tree1, tree2,
                "BST.remove(9) failed on non-root two children")
        points += (p * 2); feedback += f
        # Remove root with 2 children
        tree1.remove(11); tree2.remove(11)
        tree1.remove(4); tree2.remove(4)
        p,f = strTest(tree1, tree2,
                "BST.remove(9) failed on non-root two children")
        points += (p * 3); feedback += f
        # Remove root with 1 child
        tree1.remove(3); tree2.remove(3)
        p,f = strTest(tree1, tree2,
                "BST.remove(9) failed on non-root two children")
        points += (p * 3); feedback += f
        # Remove root with no children
        tree1.remove(5); tree2.remove(5)
        p,f = strTest(tree1, tree2,
                "BST.remove(9) failed on non-root two children")
        points += (p * 2); feedback += f
        # Remove from empty tree (2 pts)
        try:
            tree2.remove(5)
            feedback += "\n\tBST.remove() failed for empty tree"
        except ValueError: points += 2
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
        
    try:    # Problem 4: 10 points
        feedback += "\n\nProblem 4 (10 points):"
        s.plot_times("English.txt", 1000, 4000, 1000)
        p,f = grade(10, "\n\tSee instructor for feedback")
        points = p; feedback += f
        
        score += points; feedback += "\nScore += " + str(points)
    except Exception as e: feedback += "\nError: " + e.message
    
    if late:    # Late submission penalty
        feedback += "\n\nHalf credit for late submission."
        feedback += "\nRaw score: " + str(score) + "/" + str(total)
        score *= .5
    
    # Report final score.
    feedback += "\n\nTotal score: " + str(score) + "/" + str(total)
    percentage = (100.0 * score) / total
    feedback += " = " + str(percentage) + "%"
    if percentage < 72.0 and not late:
        feedback += "\n\nOn any given problem, if one test fails then"
        feedback += " subsequent tests are likely to fail.\nFix the tests in"
        feedback += " the order that they are mentioned in this feedback file."
    if   percentage >=  98.0: feedback += "\n\nExcellent!"
    elif percentage >=  90.0: feedback += "\n\nGreat job!"
    return score, feedback