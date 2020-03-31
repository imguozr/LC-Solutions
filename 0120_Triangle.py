from typing import List


class Solution:
    """
    DP.
    """

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * (n + 1)

        for level in range(n - 1, -1, -1):
            for i in range(level + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[level][i]

        return dp[0]
