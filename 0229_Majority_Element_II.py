from typing import List


class Solution:
    """
        We can use a Counter to solve such problem if not having limitations on O(1) space.
        Instead, we choose Boyer-Moore Majority Vote Algorithm.
        https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

        And because we have most 2 variables, we can use 2 counts and 2 candidates.
    """

    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]
