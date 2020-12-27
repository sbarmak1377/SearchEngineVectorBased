class MaxHeap:
    heap = [[-1, -1]]
    front = 1

    def isLeaf(self, pos):
        if pos >= len(self.heap) / 2 and pos <= len(self.heap):
            return True
        return False

    def swap(self, spos, fpos):
        self.heap[fpos], self.heap[spos] = (self.heap[spos], self.heap[fpos])

    def parent(self, pos):
        return pos / 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def heapify(self, pos):
        if not self.isLeaf(pos):
            if (self.heap[pos][1] < self.heap[self.leftChild(pos)][1] or
                    self.heap[pos][1] < self.heap[self.rightChild(pos)][1]):

                if (self.heap[self.leftChild(pos)][1] >
                        self.heap[self.rightChild(pos)][1]):
                    self.swap(pos, self.leftChild(pos))
                    self.heapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.heapify(self.rightChild(pos))

    def push(self, element):
        self.heap.append(element)
        x = len(self.heap) - 1
        while self.heap[x][1] > self.heap[self.parent(x)][1] and self.parent(x) >= self.front:
            self.swap(x, self.parent(x))
            x = self.parent(x)

    def pop(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[len(self.heap) - 1]
        del self.heap[len(self.heap) - 1]
        self.heapify(self.front)
        return popped
