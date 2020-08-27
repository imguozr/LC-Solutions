from collections import deque
from typing import List


class Solution:
    """
    Monotonic Queue
    """
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []

        res = []
        q = deque()

        for i in range(len(nums)):
            # left element out of window
            if q and i - q[0] == k:
                q.popleft()

            # Remove indexes of all elements smaller
            # than the current one
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                res.append(nums[q[0]])

        return res
