class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    
    def iter_inorder_traversal(self):
        res = []
        stack = []
        currentNode = self
        while currentNode or stack:
            if currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                popped = stack.pop()
                res.append(popped.data)
                currentNode = popped.right
        return res

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    inorder_traversal = root.iter_inorder_traversal()
    print("Inorder Traversal", end = " ")
    print(*inorder_traversal, sep="->")