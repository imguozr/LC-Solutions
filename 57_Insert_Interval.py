class Solution:
    """
        1. Insert new_interval into original list, return this question into #56 (Merge Intervals)
        2. Greedy.
    """

    def insert_1(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        intervals.append(new_interval)
        intervals.sort(key=lambda x: x[0])

        res = []
        for itvl in intervals:
            if res and res[-1][1] >= itvl[0]:
                res[-1][1] = max(res[-1][1], itvl[1])
            else:
                res.append(itvl)
        return res

    def insert_2(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
            1. Add to the output all the intervals starting before new interval.
            2. Add to the output newInterval. Merge it with the last added interval
            if new interval starts before the last added interval.
            3. Add the next intervals one by one. Merge with the last added interval
            if the current interval starts before the last added interval.
        """
        res, i = [], 0
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            e = min(intervals[i][0], new_interval[0])
            s = max(intervals[i][1], new_interval[1])
            new_interval = [e, s]
            i += 1
        res.append(new_interval)
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
