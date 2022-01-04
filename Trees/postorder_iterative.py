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
    def postorder_iterative(self, root):
        s1 = []
        s2 = []
        if root:
            s1.append(root)
            while s1:
                popped = s1.pop()
                if popped.left: s1.append(popped.left)
                if popped.right: s1.append(popped.right)
                s2.append(popped.val)
        s2.reverse()
        return s2
    
if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)

    postorder_traversal = root.postorder_iterative(root)

    print("Postorder Traversal", end = " ")
    print(*postorder_traversal, sep = "->")