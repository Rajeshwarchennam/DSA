class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        if self.val > val:
            if not self.left: self.left = Node(val)
            else: self.left.insert(val)
        else:
            if not self.right: self.right = Node(val)
            else: self.right.insert(val)
    
    def is_identical(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1:
            return False
        if not root2:
            return False
        if root1.val != root2.val:
            return False
        if (self.is_identical(root1.left, root2.left) and self.is_identical(root1.right, root2.right)):
            return True
        return False

if __name__ == "__main__":
    root1 = Node(12)
    root1.insert(6)
    root1.insert(14)
    root1.insert(3)
    root2 = Node(12)
    root2.insert(6)
    root2.insert(14)
    root2.insert(5)
    root2.insert(10)
    root2.insert(15)
    root2.insert(11)

    print(root1.is_identical(root1, root2))
    print(root1.is_identical(root1, root1))
    