class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        DP
        """
        
        if len(s3) != len(s1) + len(s2):
            return False

        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[-1][-1]

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        """
        DFS
        """

        if len(s3) != len(s1) + len(s2):
            return False

        m, n, l = len(s1), len(s2), len(s3)
        stack, seen = [(0, 0)], {(0, 0)}
        while stack:
            x, y = stack.pop()
            if x + y == l:
                return True
            if x + 1 <= m and s1[x] == s3[x + y] and (x + 1, y) not in seen:
                stack.append((x + 1, y))
                seen.add((x + 1, y))
            if y + 1 <= n and s2[y] == s3[x + y] and (x, y + 1) not in seen:
                stack.append((x, y + 1))
                seen.add((x, y + 1))
        return False
