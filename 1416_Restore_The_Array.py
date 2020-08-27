class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i, max(1, i - 9) - 1, -1):
                st = s[j - 1:i]
                if st[0] == '0':
                    continue

                val = int(st)
                if not val:
                    continue
                if val <= k:
                    dp[i] = (dp[i] % mod + dp[j - 1] % mod) % mod
                else:
                    break
        return dp[-1]
