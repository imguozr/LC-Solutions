class Solution:
    """
    DP.
    '?' means any single character.
    '*' means any sequence of characters (including the empty sequence).
    """

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True
        for i in range(1, n + 1):
            # pattern is full * can only match empty string
            dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[-1][-1]
