class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    

    def enqueue(self, val):
        new_node = Node(val)

        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length +=1


    def dequeue(self):
        
        head = self.head
        if self.head:
            self.head = self.head.next
            self.length -= 1
            return head.val 
        return None
    

    def peek(self):
        if self.head:
            return self.head.val
        return None

    
    def __len__(self):
        return self.length


    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)
