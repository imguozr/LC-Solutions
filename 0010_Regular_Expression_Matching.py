class Solution:
    """
    DP.
    '.' means any single character.
    '*' means zero or more of the preceding element.
    """

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # whether the 1st i characters in s can match the 1st j characters in p
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # empty string matches empty pattern
        dp[0][0] = True
        # dp[i][0] = False. non-empty string can't match empty pattern
        # dp[0][j] depends on the '*' in the pattern.
        # If '*' is on even positions and pattern length is even,
        # empty string can match non-empty pattern.
        for j in range(2, n + 1, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] != '.' and p[j - 2] != s[i - 1]:
                        # (#)* is counted as empty
                        dp[i][j] = dp[i][j - 2]
                    else:
                        # .* is empty or one or multiple.
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]

        return dp[-1][-1]
