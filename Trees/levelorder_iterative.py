class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        if self.val > val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
    
    def levelorder_iterative(self, root):
        res = []
        if root:
            q = [root]
            while len(q) > 0:
                popped = q.pop(0)
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
                res.append(popped.val)
        return res

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)

    levelorder = root.levelorder_iterative(root)

    print("Level Order Traversal", end = " ")
    print(*levelorder, sep = "->")
            