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
    
    def levelorder_traversal(self, root):
        res = []
        for level in range(1, self.height(root)+1):
            res.append(self.curr_level(root, level))
        return res
    
    def curr_level(self, root, level):
        res = []
        if root:
            if level == 1:
                res.append(root.val)
            else:
                res = self.curr_level(root.left, level - 1)
                res += self.curr_level(root.right, level - 1)
        return res
    
    def height(self, root):
        if not root:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1


if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)

    levelorder = root.levelorder_traversal(root)
    
    print("Level Order Traversal")
    for level, curr_level in enumerate(levelorder):
        print(f"Level {level+1}", end = "       ")
        print(*curr_level)
