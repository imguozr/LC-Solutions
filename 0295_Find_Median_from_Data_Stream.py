import heapq


class MedianFinder:
    """
        Use 2 heaps to store data flow.
        Divide data into 2 sorted parts, median is max of the left part when total # is odd,
        median is average of max of the left part and min of the right part when total # is even.

        To achieve that, there are 2 restrictions:
            1. max_heap top <= min_heap top
            2. len(max_heap) = len(min_heap) (+ 1 if total # is odd)
    """

    def __init__(self):
        self.cnt = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        self.cnt += 1
        # Because Python doesn't have max heap, push -num into heap to get same effect.
        heapq.heappush(self.max_heap, -num)
        max_heap_top = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.cnt % 2:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

    def findMedian(self) -> float:
        if self.cnt % 2:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] + (-self.max_heap[0])) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
