class Solution:
    """
    DP.
    """

    def isScramble1(self, s1: str, s2: str) -> bool:
        """
        DP.
        :param s1:
        :param s2:
        :return:
        """
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True

        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                for j in range(n - l + 1):
                    for k in range(1, l):
                        if dp[i][j][k] and dp[i + k][j + k][l - k]:
                            dp[i][j][l] = True
                            break
                        if dp[i][j + l - k][k] and dp[i + k][j][l - k]:
                            dp[i][j][l] = True
                            break

        return dp[0][0][n]

    def isScramble2(self, s1: str, s2: str) -> bool:
        """
        Recursively dp.
        """

        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble2(s1[:i], s2[:i]) and self.isScramble2(s1[i:], s2[i:]) or \
                    (self.isScramble2(s1[:i], s2[-i:]) and self.isScramble2(s1[i:], s2[:-i])):
                return True

        return False
