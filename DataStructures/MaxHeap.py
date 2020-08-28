class MaxHeap:
    # constructor : initializing a list that will contain the values of the heap
    def __init__(self):
        self.heap = []

    def insert(self, val):
        # append => add element to the end of the list heap
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        # if there is more than 1 element in the list heap
        if len(self.heap) > 1:
            max = self.heap[0]
            # negative index = indexing into some indexable container relative to the end of the contaier,
            # rather than the start
            # https://www.quora.com/What-is-negative-index-in-Python
            # so here, self.heap[-1] would be the last element in the list.
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max

        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max

        else:
            return None

    # function to restore the heap invariant
    # in this implementation, we want the parent node to be bigger than the child node
    # so, if the child node is bigger, than we will swap with the parent node.
    # After swapping, the function is called recursively on each parent node until the root is reached.

    # Time complexity = O(log (n)), bc thats the maximum # of nodes that would have to be checked/swapped
    def __percolateUp(self, index):
        # double slash operator does a floor division (rounds down to the nearest whole number)
        # index - 1 b/c the first index of this version of maxHeap starts at 0
        parent = (index-1)//2
        # if index is the root or smaller than the root
        if(index <= 0):
            return
        elif self.heap[parent] < self.heap[index]:
            tmp = self.heap[parent]
            # the parent node now will have the value of the value of index.
            self.heap[parent] = self.heap[index]
            # the index value now will store the temp value (or the value parent node previously had)
            self.heap[index] = tmp
            # recursion to check and swap the parents node to meet the maxHeap invariant
            self.__percolateUp(parent)

    # resotores the heap property after a node is removed from the maxHeap.
    # swaps the values of the parent nodes with the values of their largest child nodes until the heap property is restored.
    def __maxHeapify(self, index):
        left = (index * 2) + 1
        right = (index*2) + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        # if the largest has been updated by the previous conditionals
        # and if it doesn't equal the provided index parameter,
        # swap happens.
        # recursively traverses down the heap to fix and maintain the maxHeap invariant
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__maxHeapify(largest)

    # this function restores and creates a heap from the parameter arr (list)
    # it calls _maxHeapify method at every index starting from the last index
    # of the list building a heap.
    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr)-1, -1, -1):
            self.__maxHeapify(i)


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(100)

print(heap.getMax())
