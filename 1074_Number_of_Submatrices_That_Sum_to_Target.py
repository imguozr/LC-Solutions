from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # generate prefix sum
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i - 1]

        res = 0
        for i in range(n):
            for j in range(i, n):
                counter = defaultdict(int)
                counter[0] = 1
                curr = 0

                # for each pairs of column, iterate row for max sum.
                for k in range(m):
                    curr += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += counter[curr - target]
                    counter[curr] += 1

        return res
