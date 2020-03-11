from typing import List


class Solution:
    """
        Use cache to store dfs results.
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])

        cache = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, cache))
        return res

    def dfs(self, matrix, i, j, cache):
        if cache[i][j]:
            return cache[i][j]

        for a, b in (0, 1), (0, -1), (1, 0), (-1, 0):
            x, y = i + a, j + b
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], self.dfs(matrix, x, y, cache))
        cache[i][j] += 1
        return cache[i][j]
