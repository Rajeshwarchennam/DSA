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
    
    def left_view_util(self, root, result, level):
        if not root:
            return
        if len(result) == level:
            result.append(root.val)
        self.left_view_util(root.left, result, level+1)
        self.left_view_util(root.right, result, level+1)
    
    def left_view(self, root):
        result = []
        self.left_view_util(root, result, 0)
        return result

    def right_view_util(self, root, result, level):
        if not root:
            return
        if len(result) == level:
            result.append(root.val)
        self.right_view_util(root.right, result, level+1)
        self.right_view_util(root.left, result, level+1)
    
    def right_view(self, root):
        result = []
        self.right_view_util(root, result, 0)
        return result

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)

    left_view = root.left_view(root)
    print("Left View")
    print(*left_view, sep = "\n ↓ \n")

    right_view = root.right_view(root)
    print("Right View")
    print(*right_view, sep = "\n ↓ \n")