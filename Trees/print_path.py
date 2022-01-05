class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data > data:
            if not self.left: self.left = Node(data)
            else: self.left.insert(data)
        else:
            if not self.right: self.right = Node(data)
            else: self.right.insert(data)
    
    def find_path(self, root, target):
        path = []
        self.has_path(root, target, path)
        return path
    
    def has_path(self, root, target, path):
        if not root:
            return False
        path.append(root.data)
        if root.data == target:
            return True
        if (self.has_path(root.left, target, path) or self.has_path(root.right, target, path)):
            return True
        path.pop()
        return False

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)
    print(root.find_path(root, 5))