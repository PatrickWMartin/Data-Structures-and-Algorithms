class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return f"{self.val}"

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        if head:
            self.length = 1
        else:
            self.length = 0
        
    def add(self, node):
        #add a new node to the front of the linked list
        node.next = self.head
        self.head = node
        self.length += 1
        
    def append(self, node):
        #adds a new node to the end of the linked list
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.length += 1
    
    def clear(self):
        #clears linked list
        self.head = None
        self.length = 0
        
    def empty(self):
        return self.length == 0
    
    def get_at(self, index):
        #get a value at a certain index
        if (index >= self.length or index < 0) and self.length != 0:
            raise Exception("index out of bounds")

        count = 0
        current = self.head
        while count < index:
            current = current.next
            count+=1
        
        return current
    
    def insert_at(self, index, node):
        #get a value at a certain index
        if (index >= self.length+1 or index < 0) and self.length != 0:
            raise Exception("index out of bounds")
        
        if index == 0:
            self.add(node)
        elif index == self.length:
            self.append(node)
        else:
            count = 0
            current = self.head
            prev = None
            while count < index:
                prev = current
                current = current.next
                count+=1
        
            prev.next = node
            node.next = current
            self.length += 1
            
    def set_at(self, index, value):
        #get a value at a certain index
        if (index >= self.length or index < 0) and self.length != 0:
            raise Exception("index out of bounds")

        count = 0
        current = self.head
        while count < index:
            current = current.next
            count+=1
        
        current.val = value
        
    def index_of(self, value):
        current = self.head
        count = 0
        while current:
            if current.val == value:
                return count
            count +=1
            current = current.next
            
        return None
    
    def remove_at(self, index):
        #get a value at a certain index
        if (index >= self.length or index < 0) and self.length != 0:
            raise Exception("index out of bounds")
        if not self.head:
            return 
        if index == 0:
            self.head = self.head.next
        else:
            count = 0
            prev = None
            current = self.head
            while count < index:
                prev = current
                current = current.next
                count+=1
            prev.next = current.next
            
    
    def remove(self, value):
        current = self.head
        while current.next:
            if current.next.val == value:
                current.next = current.next.next
                self.length -= 1
                break
            current = current.next
        
    def __len__(self):
        return self.length
    
    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)