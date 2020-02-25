class Solution:
    """
        Dynamic Programming.
    """

    def canJump_1(self, nums: list[int]) -> bool:
        """
            Brutal Force.
        """

        def helper(pos):
            if pos == len(nums) - 1:
                return True
            nxt_farthest = min(pos + nums[pos], len(nums) - 1)
            for i in range(pos + 1, nxt_farthest + 1):
                if helper(i):
                    return True
            return False

        return helper(0)

    def canJump_2(self, nums: list[int]) -> bool:
        """
            DP(Top-Down)
        """

        n = len(nums)
        dp = [0] * (n - 1) + [1]

        def helper(pos):
            if dp[pos] == 1:
                return True
            elif dp[pos] == -1:
                return False

            nxt_farthest = min(pos + nums[pos], n - 1)
            for nxt in range(pos + 1, nxt_farthest + 1):
                if helper(nxt):
                    dp[pos] = 1
                    return True
            dp[pos] = -1
            return False

        return helper(0)

    def canJump_3(self, nums: list[int]) -> bool:
        """
            DP(Bottom-up)
        """

        n = len(nums)
        dp = [0] * (n - 1) + [1]

        for i in range(n - 2, -1, -1):
            nxt_farthest = min(i + nums[i], n - 1)
            for j in range(i + 1, nxt_farthest + 1):
                if dp[j] == 1:
                    dp[i] = 1
                    break

        return dp[0] == 1

    def canJump_4(self, nums: list[int]) -> bool:
        """
            Greedy 1
        """
        end = len(nums) - 1
        for i in range(end, -1, -1):
            if i + nums[i] >= end:
                end = i
        return end == 0

    def canJump(self, nums: list[int]) -> bool:
        """
            Greedy 2
            1. If one element (start point) in the list is n, it means n elements after can be start points.
            2. Update farthest point with n elements.
            3. if can reach the end. return True. (If stops at middle, return False.)
        """

        end = 0
        for i in range(len(nums)):
            if i > end:
                return False
            end = max(end, i + nums[i])
        return True
