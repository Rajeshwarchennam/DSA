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
    
    def get_width(self, root, level):
        if not root: return 0
        if level == 1: return 1
        return (self.get_width(root.left, level - 1) 
        + self.get_width(root.right, level - 1))

    def max_width(self, root):
        max_width = 0
        level = 1
        while True:
            width = self.get_width(root, level)
            level += 1
            max_width = max(max_width, width)
            if width == 0:
                return max_width

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)
    root.insert(15)
    print(root.max_width(root))
    
    