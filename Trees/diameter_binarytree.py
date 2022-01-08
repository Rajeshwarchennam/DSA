# Find the max number of edges between any two nodes
# https://leetcode.com/problems/diameter-of-binary-tree/
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

    def height(self, root):
        if not root: return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameter_binaryTree(self, root):
        maxi = [0]
        self.find_max(root, maxi)
        
        return maxi[0]
    
    def find_max(self, root, maxi):
        if not root:
            return
        maxi[0] = max(self.height(root.left) + self.height(root.right), maxi[0])
        self.find_max(root.left, maxi)
        self.find_max(root.right, maxi)

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)

    print(root.diameter_binaryTree(root))