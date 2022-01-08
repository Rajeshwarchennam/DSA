class Node:
    def __init__(self, val) -> None:
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
    def left_boundary(self, root, path):
        if not root:
            return
        if root.left:
            path.append(root.val)
            self.left_boundary(root.left, path)
        elif root.right:
            path.append(root.val)
            self.left_boundary(root.right, path)
    def right_boundary(self, root, path):
        if not root:
            return
        if root.right:
            path.insert(0, root.val)
            self.right_boundary(root.right, path)
        elif root.left:
            path.insert(0, root.val)
            self.right_boundary(root.left, path)
    
    def leaf_boundary(self, root, path):
        if not root:
            return
        if not root.left and not root.right:
            path.append(root.val)
        else:
            self.leaf_boundary(root.left, path)
            self.leaf_boundary(root.right, path)

    def boundary_traversal(self, root):
        left_boundary = []
        self.left_boundary(root, left_boundary)

        right_boundary = []
        self.right_boundary(root, right_boundary)

        leaf_boundary = []
        self.leaf_boundary(root, leaf_boundary)

        boundary_traversal = []
        # Removing the last value from right_boundary as it is root itself, which is already
        # there in left_boundary
        boundary_traversal = left_boundary + leaf_boundary + right_boundary[:-1]
        return boundary_traversal

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(13)
    root.insert(12)
    root.insert(3)
    root.insert(7)
    root.insert(5)

    boundary_traversal = root.boundary_traversal(root)

    print("Boundary Traversal:", end=" ")
    print(*boundary_traversal, sep = "->")

    