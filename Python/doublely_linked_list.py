#Simple doublely linked list. Mainly implemented for stacks and queues so not as many methods like in the singlely linked list

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DoublelyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    def append(self, val):
        #add a value to the end of the list
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def insert_at_head(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1


    def remove_head(self):
        if self.head:
            self.head = self.head.next
            if self.length > 1:
                self.head.prev = None
            self.length -= 1


    def remove_tail(self):
        if self.head:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.length -= 1


    def __len__(self):
        return self.length


    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(str(current.val))
            current = current.next
        return " <-> ".join(nodes)
            
            