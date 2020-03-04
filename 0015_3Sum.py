from typing import List


class Solution:
    """
        Intuition: Iterate every number in nums,
        use the number as a target to find two other numbers which make total zero
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # Last two numbers have been considered.
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            # Jump over same number.
            if i and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
