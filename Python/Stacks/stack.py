class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
    

    def push(self, val):
        new_node = Node(val)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        self.length +=1

    def pop(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            self.length -= 1
            return head.val
        return None

    def peek(self):
        if self.head:
            return self.head.val
        return None


    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes)