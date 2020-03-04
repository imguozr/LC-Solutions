from typing import List


class Solution:
    """
        Greedy.
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start.
        intervals.sort(key=lambda x: x[0])

        res = []
        for interval in intervals:
            # Current interval overlap with the previous
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res
