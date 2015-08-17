from Node import LinkedListNode
from Node import DoublyLinkedListNode
from Node import SortedListNode

class LinkedList(object):
    """A class for creating linked list objects."""
    
    def __init__(self):
        """Creates a new linked list. Create the head attribute and set 
        it to None since the list is empty.
        """
        self.head = None
        
    def add_node(self, data):
        """Create a new Node containing the data and add it 
        to the end of the list
        """
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            
    def remove_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next.data != data:
                current_node = current_node.next
                if current_node.next is None: #you have reached the end
                    print "Node not in list"
                    return
            new_next_node = current_node.next.next
            current_node.next = new_next_node
            
    def insert_node(self, new_data, old_data):
        #check to see if it's empty
        if self.head is None:
            return
        
        #if inserting at the front of the list
        new_node = LinkedListNode(new_data)
        if old_data == self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        
        else:
            current_node = self.head
            while current_node.next.data != old_data:
                current_node = current_node.next
                if current_node.next is None:
                    print "Node not in list"
                    return
            new_node.next = current_node.next
            current_node.next = new_node
          
    def __repr__(self):
        #method using lists
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        return str(output)
    
class DoublyLinkedList(LinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, data):
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
    
    def remove_node(self, data):
        #if head
        if self.head.data == data:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next.data != data:
                current_node = current_node.next
                if current_node.next is None: #you have reached the end
                    print "Node not in list"
                    return
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
                             
    def insert_node(self, new_data, old_data):
        #check to see if it's empty
        if self.head is None:
            return
        
        #if inserting at the head
        new_node = DoublyLinkedListNode(new_data)
        if self.head.data == old_data:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        #otherwise
        else:
            current_node = self.head
            while current_node.next.data != old_data:
                current_node = current_node.next
                if current_node.next is None:
                    print "Node not in list"
                    return
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node
            new_node.prev = current_node
                    
class SortedList(DoublyLinkedList):
    def __init__(self):
        DoublyLinkedList.__init__(self)
    def add_node(self, data):
        new_node = SortedListNode(data)
        #if empty
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
            
#took 10:59 to sort data.txt