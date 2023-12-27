class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        new_node = BSTNode(val)

        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


    def get_min(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr.val


    def get_max(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr.val

