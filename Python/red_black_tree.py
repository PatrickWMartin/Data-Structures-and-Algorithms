class RBTreeNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = false
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def inser(self, val):
        pass
