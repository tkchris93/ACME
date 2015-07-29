class Node(object):

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

class StrNode(Node):
    def __init__(self, data):
        if type(data) == str:
            Node.__init__(self,data)
        else:
            self.data = None
            
class LinkedListNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.next = None
        
class DoublyLinkedListNode(Node):
    def __init__(self, data):
        Node.__init__(self, data)
        self.prev = None
        self.next = None
        
class SortedListNode(StrNode):
    def __init__(self, data):
        StrNode.__init__(self, data)
        self.prev = None
        self.next = None