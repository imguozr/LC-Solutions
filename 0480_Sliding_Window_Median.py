from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    """
        Similar with # 295. Use 2 heaps.
        Because it's sliding window, should add/remove elements in heap dynamically.
    """

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums:
            return []

        n = len(nums)
        res = [0] * (n - k + 1)
        max_heap, min_heap = [], []

        j, count, index = 0, 0, 0
        for i in range(n - k + 1):
            while j < n and count < k:
                max_heap, min_heap = self.add(max_heap, min_heap, nums[j])
                count += 1
                j += 1
            if count == k:
                if len(max_heap) == len(min_heap):
                    res[index] = (-max_heap[0] + min_heap[0]) / 2
                else:
                    res[index] = -max_heap[0]
            index += 1
            count -= 1
            max_heap, min_heap = self.remove(max_heap, min_heap, nums[i])
        return res

    def add(self, max_heap, min_heap, num):
        heappush(max_heap, -num)
        max_heap_top = -heappop(max_heap)
        heappush(min_heap, max_heap_top)
        if len(max_heap) < len(min_heap):
            heappush(max_heap, -heappop(min_heap))
        return max_heap, min_heap

    def remove(self, max_heap, min_heap, num):
        if num <= -max_heap[0]:
            max_heap.remove(-num)
            heapify(max_heap)
        else:
            min_heap.remove(num)
            heapify(min_heap)
        return max_heap, min_heap
