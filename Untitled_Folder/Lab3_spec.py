import Node
LLN = Node.LinkedListNode

#This is a comment
'''
This is a multiline comment
'''
a = 0

class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def add_node(self, data):
        new_node = LLN(data)
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
                if current_node.next is None:
                    print "Not in list"
                    return
            new_next_node = current_node.next.next
            current_node.next = new_next_node
    
    def insert_node(self, new_data, old_data):
        #if empty (we check this to avoid a seg fault)
        if self.head is None:
            return
        
        #if inserted at head
        new_node = LLN(new_data)
        if self.head.next.data == old_data:
            new_node.next = self.head
            self.head = new_node
        
        #otherwise
        else:
            current_node = self.head
            while current_node.next.data != old_data:
                current_node = current_node.next
                if current_node.next is None:
                    print "Not in list"
                    return
            new_node.next = current_node.next
            current_node.next = new_node
        
    
    def __repr__(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(current_node.data)
            current_node = current_node.next
        return str(output)
