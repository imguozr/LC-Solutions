from typing import List


class Solution:
    """
        2 pointers.
    """

    def triangleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            lo, hi = 0, i - 1
            while lo < hi:
                if nums[hi] + nums[lo] > nums[i]:
                    # nums between hi and lo as lower # will all qualify.
                    res += hi - lo
                    hi -= 1
                else:
                    lo += 1
        return res
