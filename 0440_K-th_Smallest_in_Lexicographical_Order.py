class Solution:
    """
        Intuition: Calculate # of integers between prefix and prefix + 1. (Same level children in the de-nary tree.)
        # > k means the target starts with prefix.
        # <= k means the target doesn't start w/ prefix.

        3 key sub-problem:
        1. How to calculate # of all sub-integers w/ some prefix?
        2. If the target is under the current prefix?
            prefix *= 10
        3. If the target is not under the current prefix?
            prefix += 1
    """

    def findKthNumber(self, n: int, k: int) -> int:
        res = 1
        # 1 is already counted.
        k -= 1
        while k > 0:
            # Number of numbers start with res
            cnt = self.count_number(n, res)
            # Target starts with res.
            if cnt > k:
                res *= 10
                k -= 1
            else:
                res += 1
                k -= cnt
        return res

    def count_number(self, n, prefix):
        """
            Calculate # of integers start with prefix.
        """
        curr, nxt = prefix, prefix + 1
        cnt = 0
        while curr <= n:
            # If nxt is chosen, you add steps of the full amount of that layer of curr, 10/100/1000...
            # However, if n is chosen, you need to count the first step of curr in.
            cnt += min(n + 1, nxt) - curr
            curr *= 10
            nxt *= 10
        return cnt
