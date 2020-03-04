from typing import List


class Solution:
    """
        Boyer-Moore Majority Vote Algorithm. Like # 229.
    """

    def majorityElement(self, nums: List[int]) -> int:
        res, cnt = 0, 0
        for num in nums:
            if not cnt:
                res, cnt = num, 1
            elif num == res:
                cnt += 1
            else:
                cnt -= 1
        return res
