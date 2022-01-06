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
    
    def find_lca(self, root, n1, n2):
        if not root:
            return None
        if root.val == n1 or root.val == n2:
            return root
        left_lca = self.find_lca(root.left, n1, n2)
        right_lca = self.find_lca(root.right, n1, n2)
        if left_lca and right_lca:
            return root
        if left_lca: return left_lca
        return right_lca

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)
    print(root.find_lca(root, 5, 7).val)