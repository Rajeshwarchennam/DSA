# LeetCode - https://leetcode.com/problems/balanced-binary-tree/

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
    
    def is_balanced(self, root) -> bool:
        if not root:
            return True
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            if abs(left_height-right_height) > 1:
                return False
            return (self.is_balanced(root.left) and self.is_balanced(root.right))
    
    def height(self, root):
        if root is None: return 0
        return 1 + max(self.height(root.left), self.height(root.right))


if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    print(root.is_balanced(root))
        