from bisect import bisect_left, insort
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def max_sum_sub_array(prefix):
            max_sum = float('-inf')
            curr_sum = 0
            sums = [0]
            for num in prefix:
                curr_sum += num
                # find the lower bound of the index
                idx = bisect_left(sums, curr_sum - k)
                if idx < len(sums):
                    max_sum = max(max_sum, curr_sum - sums[idx])
                # insert curr_sum into sums in order
                insort(sums, curr_sum)
            return max_sum

        m, n = len(matrix), len(matrix[0])
        res = float('-inf')

        # generate prefix sum list for each column
        for left in range(n):
            prefix = [0] * m
            for right in range(left, n):
                for row in range(m):
                    prefix[row] += matrix[row][right]

                # max sum of current column
                curr_max = max_sum_sub_array(prefix)
                res = max(res, curr_max)

        return res
