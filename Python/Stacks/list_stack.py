class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if self.values:
            return self.values.pop()
        return None

    def peek(self):
        if self.values:
            return self.values[-1]
        return None

    def size(self):
        return len(self.values)

