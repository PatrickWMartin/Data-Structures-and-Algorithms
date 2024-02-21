class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, node):
        if node == self.nil or node.right == self.nil:
            return

        child = node.right
        node.right = child.left

        if child.left != self.nil:
            child.left.parent = node

        child.parent = node.parent
        if node.parent is None:
            self.root = child
        elif node.parent.left == node:
            node.parent.left = child
        elif node.parent.right == node:
            node.partent.right = child

        child.left = node
        node.parent = child

    def rotate_right(self, node):

        if node == self.nil or node.right == self.nil:
            return

        child = node.left
        node.left = child.right

        if child.right != self.nil:
            child.right.parent = node

        child.parent = node.parent
        if node.parent is None:
            self.root = child
        elif node.parent.right == node:
            node.parent.right = child
        else:
            node.partent.left = child

        child.right = node
        node.parent = child

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.red = True
        new_node.right = self.nil
        new_node.left = self.nil

        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # Just ingnoreing duplicates
                return

        new_node.parent = current
        if parent is None:
            self.root = new_node
        elif parent.val > new_node.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_up(new_node)

    def fix_up(self, node):

        if node.parent is None:
            return  # return if the root node

        while node.parent.red:
            if node.parent == node.parent.parent.right:  # if parent is a right child
                uncle = node.parent.parent.left

                if uncle.red:  # if the uncle is reversed
                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_left(node.parent.parent)
            else:
                uncle = node.parent.parent.right

                if uncle.red:  # if the uncle is reversed
                    uncle.red = False
                    node.parent.red = False
                    node.parent.parent.red = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.red = False
                    node.parent.parent.red = True
                    self.rotate_right(node.parent.parent)

        self.root.red = False
