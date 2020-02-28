class Solution:
    """
        DP.
        dp[i][*] = max(dp[i - 1][*], dp[i - 1][#] + nums[i - 1])
        the formula of *, # can be settled by math.
    """

    def maxSumDivThree_1(self, nums: list[int]) -> int:
        """
            Time Complexity: O(n)
            Space Complexity: O[3(n+1)] = O(n)
        """
        n = len(nums)
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][1] = dp[0][2] = float('-inf')

        for i in range(1, n + 1):
            if not nums[i - 1] % 3:
                dp[i][0] = dp[i - 1][0] + nums[i - 1]
                dp[i][1] = dp[i - 1][1] + nums[i - 1]
                dp[i][2] = dp[i - 1][2] + nums[i - 1]
            elif nums[i - 1] % 3 == 1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] + nums[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + nums[i - 1])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + nums[i - 1])
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + nums[i - 1])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][0] + nums[i - 1])

        return dp[-1][0]

    def maxSumDivThree_2(self, nums: list[int]) -> int:
        dp = [0, 0, 0]
        for num in nums:
            for i in dp[:]:
                dp[(num + i) % 3] = max(dp[(num + i) % 3], num + i)
        return dp[0]
