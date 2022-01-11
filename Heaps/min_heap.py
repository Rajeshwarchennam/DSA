class MinHeap:
    def __init__(self):
        self.size = 0
        self.heap = []
    def parent(self, pos):
        return (pos-1)//2
    def leftChild(self, pos):
        return 2*pos + 1
    def rightChild(self, pos):
        return 2*pos + 2
    def isLeaf(self, pos):
        if pos >= self.size//2 and pos < self.size:
            return True
        return False
    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]
    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            leftChild = None if self.leftChild(pos) >= self.size else self.heap[self.leftChild(pos)]
            rightChild = None if self.rightChild(pos) >= self.size else self.heap[self.rightChild(pos)]
            parent = self.heap[pos]
            if leftChild and rightChild and (parent > leftChild or parent > rightChild):
                if leftChild < rightChild:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
            elif leftChild and parent > leftChild:
                self.swap(pos, self.leftChild(pos))
                self.minHeapify(self.leftChild(pos))

    def insert(self, element):
        self.size += 1
        self.heap.append(element)
        current = self.size - 1
        while current!= 0 and self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def print(self):
        print("Parent  LeftChild   RightChild")
        for i in range(self.size//2):
            parent = self.heap[i]
            leftChild = -1 if self.leftChild(i) >= self.size else self.heap[self.leftChild(i)]
            rightChild = -1 if self.rightChild(i) >= self.size else self.heap[self.rightChild(i)]
            print(parent, leftChild, rightChild, sep = "      ")
    def minHeap(self):
        for pos in reversed(range(self.size//2)):
            self.minHeapify(pos)
    def extractMin(self):
        mini = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heap.pop()
        self.size -= 1
        self.minHeapify(0)
        return mini
    def decreaseKey(self, pos, value):
        self.heap[pos] = value
        current = pos
        while (current!=0 and self.heap[current] < self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
    def deleteKey(self, pos):
        self.decreaseKey(pos, -float("inf"))
        self.extractMin()

if __name__ == "__main__":
    minHeap = MinHeap()
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.minHeap()

    minHeap.print()

    print(f"Extracted Min element is {minHeap.extractMin()}")
    minHeap.print()

    minHeap.decreaseKey(3, 9)
    minHeap.print()

    minHeap.deleteKey(4)
    minHeap.print()

