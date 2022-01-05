class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data > data:
            if self.left is None: self.left = Node(data)
            else: self.left.insert(data)
        else:
            if self.right is None: self.right = Node(data)
            else: self.right.insert(data)
    
    def bottom_view(self, root):
        res = []
        if root:
            bottomview_dict = dict()
            q = [(root, 0)]
            while q:
                popped = q.pop(0)
                bottomview_dict[popped[1]] = popped[0].data
                if popped[0].left: q.append((popped[0].left, popped[1]-1))
                if popped[0].right: q.append((popped[0].right, popped[1]+1))
            for i in sorted(bottomview_dict):
                res.append(bottomview_dict[i])
        return res
    
    def bottom_view_recur(self, root):
        res = []
        if root:
            bottom_view_dict = dict()
            self.bottom_view_recur_util(root, bottom_view_dict, 0, 0)
            for i in sorted(bottom_view_dict):
                res.append(bottom_view_dict[i][0])
        return res
    
    def bottom_view_recur_util(self, root, bottom_view_dict, hor_dist, level):
        if not root:
            return
        if hor_dist in bottom_view_dict:
            if level >= bottom_view_dict[hor_dist][1]:
                bottom_view_dict[hor_dist] = (root.data, level)
        else:
            bottom_view_dict[hor_dist] = (root.data, level)
        self.bottom_view_recur_util(root.left, bottom_view_dict, hor_dist-1, level+1)
        self.bottom_view_recur_util(root.right, bottom_view_dict, hor_dist+1, level+1)

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)
    print(root.bottom_view(root))
    print(root.bottom_view_recur(root))