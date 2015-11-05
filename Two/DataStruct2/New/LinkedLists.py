# LinkedLists.py
"""Volume II Lab 4: Data Structures 1 (Linked Lists)
Auxiliary file. Modify this file for problems 1-5.
Tanner Christensen
Sept 12, 2015
"""


# Problem 1: Add the magic methods __str__, __lt__, __eq__, and __gt__.
class Node(object):
    """A Node class for storing data."""
    def __init__(self, data):
        """Construct a new node that stores some data."""
        self.data = data
    def __str__(self):
        return str(self.data)
    def __lt__(self,other):
        if self.data < other.data:
            return True
        else:
            return False
    def __eq__(self,other):
        if self.data == other.data:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.data > other.data:
            return True
        else:
            return False


class LinkedListNode(Node):
    """A Node class for linked lists. Inherits from the 'Node' class.
    Contains a reference to the next node in the list.
    """
    def __init__(self, data):
        """Construct a Node and initialize an attribute for
        the next node in the list.
        """
        Node.__init__(self, data)
        self.next = None

    def __str__(self):
        return str(self.data)

# Problems 2-4: Finish implementing this class.
class LinkedList(object):
    """Singly-linked list data structure class.
    The first node in the list is referenced to by 'head'.
    """
    def __init__(self):
        """Create a new empty linked list. Create the head
        attribute and set it to None since the list is empty.
        """
        self.head = None

    def add(self, data):
        """Create a new Node containing 'data' and add it to
        the end of the list.
        
        Example:
            >>> my_list = LinkedList()
            >>> my_list.add(1)
            >>> my_list.head.data
            1
            >>> my_list.add(2)
            >>> my_list.head.next.data
            2
        """
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    # Problem 2: Implement the __str__ method so that a LinkedList instance can
    #   be printed out the same way that Python lists are printed.
    def __str__(self):
        """String representation: the same as a standard Python list.
        
        Example:
            >>> my_list = LinkedList()
            >>> my_list.add(1)
            >>> my_list.add(2)
            >>> my_list.add(3)
            >>> print(my_list)
            [1, 2, 3]
            >>> str(my_list) == str([1,2,3])
            True
        """
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        return str(output)
    
    # Problem 3: Finish implementing LinkedList.remove() so that if the node
    #   is not found, an exception is raised.
    def remove(self, data):
        """Remove the node containing 'data'. If the list is empty, or if the
        target node is not in the list, raise a ValueError with error message
        "<data> is not in the list."
        
        Example:
            >>> print(my_list)
            [1, 2, 3]
            >>> my_list.remove(2)
            >>> print(my_list)
            [1, 3]
            >>> my_list.remove(2)
            2 is not in the list.
            >>> print(my_list)
            [1, 3]
        """
        if self.head is None:
            raise ValueError("{} is not in the list.".format(data))
        
        if self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next.data != data:
                current_node = current_node.next
                if current_node.next is None:
                    # reached the end of the list
                    raise ValueError("{} is not in the list.".format(data))
            new_next_node = current_node.next.next
            current_node.next = new_next_node

    # Problem 4: Implement LinkedList.insert().
    def insert(self, data, place):
        """Create a new Node containing 'data'. Insert it into the list before
        the first Node in the list containing 'place'. If the list is empty, or
        if there is no node containing 'place' in the list, raise a ValueError
        with error message "<place> is not in the list."
        
        Example:
            >>> print(my_list)
            [1, 3]
            >>> my_list.insert(2,3)
            >>> print(my_list)
            [1, 2, 3]
            >>> my_list.insert(2,4)
            4 is not in the list.
        """
        if self.head is None:
            raise ValueError("{} is not in the list.".format(place))
        
        current_node = self.head
        if self.head.data != place:
            while current_node.next.data != place:
                current_node = current_node.next
                if current_node.next is None:
                    raise ValueError("{} is not in the list.".format(place))            
            new_node = LinkedListNode(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            new_node = LinkedListNode(data)
            new_node.next = self.head
            self.head = new_node

class DoublyLinkedListNode(LinkedListNode):
    """A Node class for doubly-linked lists. Inherits from the 'Node' class.
    Contains references to the next and previous nodes in the list.
    """
    def __init__(self,data):
        """Initialize the next and prev attributes."""
        Node.__init__(self,data)
        self.next = None
        self.prev = None

# Problem 5: Implement this class.
class DoublyLinkedList(LinkedList):
    """Doubly-linked list data structure class. Inherits from the 'LinkedList'
    class. Has a 'head' for the front of the list and a 'tail' for the end.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        """Create a new Node containing the data and add it 
        to the end of the list
        """
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove(self, data):
        if self.head is None:
            raise ValueError("{} is not in the list.".format(data))
        
        if self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next.data != data:
                current_node = current_node.next
                if current_node.next is None: #you have reached the end
                    raise ValueError("{} is not in the list.".format(data))
            #if tail
            if current_node.next == self.tail:
                del current_node.next
                current_node.next = None
                self.tail = current_node
                return
            else:
                new_next_node = current_node.next.next
                current_node.next = new_next_node  
                del new_next_node.prev
                new_next_node.prev = current_node
                             
    def insert(self, data, place):
        #check to see if it's empty
        if self.head is None:
            raise ValueError("{} is not in the list.".format(place))
        
        #if inserting at the head
        new_node = DoublyLinkedListNode(data)
        if self.head.data == place:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        #otherwise
        else:
            current_node = self.head
            while current_node.next.data != place:
                current_node = current_node.next
                if current_node.next is None:
                    raise ValueError("{} is not in the list.".format(place))
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node
            new_node.prev = current_node
# Problem 6: Implement this class. Use an instance of your object to implement
# the sort_words() function in solutions.py.
class SortedLinkedList(DoublyLinkedList):
    """Sorted doubly-linked list data structure class."""

    # Overload add() and insert().
    def add(self, data):
        """Create a new Node containing 'data' and insert it at the
        appropriate location to preserve list sorting.
        
        Example:
            >>> print(my_list)
            [3, 5]
            >>> my_list.add(2)
            >>> my_list.add(4)
            >>> my_list.add(6)
            >>> print(my_list)
            [2, 3, 4, 5, 6]
        """
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        #if adding to front
        elif data < self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        #if adding to the end
        elif data > self.tail.data:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        else:
            current_node = self.head
            while current_node.next.data <= data:
                current_node = current_node.next
            
            #add it to current_node's next spot
            new_node.next = current_node.next
            current_node.next.prev = new_node
            new_node.prev = current_node
            current_node.next = new_node
            return
            
    def insert(self, *args):
        raise NotImplementedError("insert() has been disabled for this class.")

# =============================== END OF FILE =============================== #
