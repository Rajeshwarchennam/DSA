class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data > data:
            if not self.left: self.left = Node(data)
            else: self.left.insert(data)
        else:
            if not self.right: self.right = Node(data)
            else: self.right.insert(data)

    def top_view_recur(self, root):
        res = []
        if root:
            top_view_dict = dict()
            self.top_view_util_recur(root, top_view_dict, 0, 0)
            for i in sorted(top_view_dict):
                res.append(top_view_dict[i][0])
        return res

    def top_view_util_recur(self, root, top_view_dict, hor_dist, level):
        if not root:
            return
        
        if hor_dist not in top_view_dict:
            top_view_dict[hor_dist] = (root.data, level)
        else:
            if top_view_dict[hor_dist][1] > level:
                top_view_dict[hor_dist] = (root.data, level)
            
        self.top_view_util_recur(root.left, top_view_dict, hor_dist-1, level+1)
        self.top_view_util_recur(root.right, top_view_dict, hor_dist+1, level+1)

    def top_view_iter(self, root):
        res = []
        if root:
            q = [(root, 0)]
            top_view_dict = dict()
            while q:
                popped = q.pop(0)
                if popped[1] not in top_view_dict:
                    top_view_dict[popped[1]] = popped[0].data
                if popped[0].left: q.append((popped[0].left, popped[1]-1))
                if popped[0].right: q.append((popped[0].right, popped[1]+1))
            for i in sorted(top_view_dict):
                res.append(top_view_dict[i])
        return res
if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)
    print(root.top_view_recur(root))
    print(root.top_view_iter(root))