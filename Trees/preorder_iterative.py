class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.val > data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
    
    def preorder_iterative(self):
        res = []
        stack = []
        current_node = self
        while current_node or stack:
            if current_node:
                res.append(current_node.val)
                stack.append(current_node)
                current_node = current_node.left
            else:
                popped = stack.pop()
                current_node = popped.right
        return res

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    preorder_traversal = root.preorder_iterative()

    print("Preorder Traversal", end = " ")
    print(*preorder_traversal, sep = "->")