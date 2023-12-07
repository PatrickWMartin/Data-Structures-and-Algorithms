class ListQueue:
    def __init__(self) -> None:
        self.values = []
    
    def enqueue(self, value):
        self.values.insert(0, value)
    
    def dequeue(self):
        return self.values.pop()
    
    def peek(self):
        if len(self.values) > 0:
            return self.values[-1]
        return None
    
    def size(self):
        return len(self.values)