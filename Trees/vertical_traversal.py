# Leetcode Problem - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

from collections import defaultdict

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.val > data:
            if not self.left: self.left = Node(data)
            else: self.left.insert(data)
        else:
            if not self.right: self.right = Node(data)
            else: self.right.insert(data)

    def vertical_traversal(self, root):
        res = []
        if root:
            vert_trav_dic = defaultdict(list)
            self.vertical_traversal_util(root, vert_trav_dic, 0, 0)
            for i in sorted(vert_trav_dic):
                temp = []
                vert_trav_dic[i].sort(key = lambda x: (x[1], x[0]))
                for j in vert_trav_dic[i]:
                    temp.append(j[0])
                res.append(temp)
        return res
    
    def vertical_traversal_util(self, root, vert_trav_dic, hor_dist, level):
        if not root:
            return
        vert_trav_dic[hor_dist].append((root.val, level))
        self.vertical_traversal_util(root.left, vert_trav_dic, hor_dist-1, level+1)
        self.vertical_traversal_util(root.right, vert_trav_dic, hor_dist+1, level+1)

if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(5)
    print(root.vertical_traversal(root))
        