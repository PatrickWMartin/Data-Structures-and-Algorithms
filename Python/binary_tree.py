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

    
    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right.get_min()
        self.right = self.right.delete(min_larger_node.val)
        return self


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
    

    def pre_order_traverse(self, path=None):
        if path is None:
            path = []
        path.append(self.val)
        if self.left:
            self.left.pre_order_traverse(path)
        if self.right:
            self.right.pre_order_traverse(path)
        return path


    def post_order_traverse(self, path=None):
        
        if path is None:
            path = []   
        if self.left:
            self.left.post_order_traverse(path)
        if self.right:
            self.right.post_order_traverse(path)
            
        path.append(self.val)
        return path


    def in_order_traverse(self, path=None):
        if path is None:
            path = []
        if self.left:
            self.left.in_order_traverse(path)
        path.append(self.val)
        if self.right:
            self.right.in_order_traverse(path)
        return path


    def breadth_first_search(self):
        #Using a list as a queue for simplicity 
        search_queue = [self]

        while search_queue:
            search = search_queue.pop(0)
            if search.left:
                search_queue.append(search.left)
            if search.right:
                search_queue.append(search.right)
            print(search.val)
    

def build_tree_from_ordered_list(ordered_list):
    
    if len(ordered_list) <1:
        return None
    if len(ordered_list) == 1:
        return BSTNode(ordered_list[0])
    mid = len(ordered_list)//2
    root = BSTNode(ordered_list[mid])
    root.left = build_tree_from_ordered_list(ordered_list[:mid])
    root.right = build_tree_from_ordered_list(ordered_list[mid+1:])
    return root

