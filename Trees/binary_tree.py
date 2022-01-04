class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if data < self.data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    # Inorder Traversal Left -> Root -> Right
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res += self.inorder_traversal(root.right)
        return res
    
    # Preorder Traversal Root -> Left -> Right
    def preorder_traversal(self, root):
        res = []
        if root:
            res = [root.data]
            res += self.preorder_traversal(root.left)
            res += self.preorder_traversal(root.right)
        return res
    
    # Postorder Traversal Left -> Right -> Root
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)
            res += self.postorder_traversal(root.right)
            res.append(root.data)
        return res

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    inorder_traversal = root.inorder_traversal(root)
    preorder_traversal = root.preorder_traversal(root)
    postorder_traversal = root.postorder_traversal(root)
    
    print("Inorder Traversal", end = " ")
    print(*inorder_traversal, sep="->")

    print("Preorder Traversal", end = " ")
    print(*preorder_traversal, sep = "->")

    print("Postorder Traversal", end = " ")
    print(*postorder_traversal, sep = "->")
    
    