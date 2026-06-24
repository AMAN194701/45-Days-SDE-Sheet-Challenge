import heapq
class MedianFinder:

    def __init__(self):
        self.left = []   # max Heap (store -ve)
        self.right = []  # min Heap
    def addNum(self, num: int) -> None:
        # decide where the no should go
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        # balance the heap
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        elif len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
        

    def findMedian(self):
        # same size
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        # left heap has one extra element
        elif len(self.left) > len(self.right):
            return -self.left[0]
        # right heap has one extra element
        else:
            return self.right[0]
        
