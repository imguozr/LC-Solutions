from collections import defaultdict
from typing import List


class Solution:
    """
    Use dict to store the appearance time of prefix sum.
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        count, prefix = 0, 0
        # prefix sum 0 has appeared 1 time.
        dic = defaultdict(int)
        dic[0] = 1
        for i in range(len(nums)):
            # compute prefix sum
            prefix += nums[i]
            # prefix - k in dic means exists sequence sum is k
            count += dic[prefix - k]
            # if prefix sum in dic, appearance time + 1, if not set it equals 0
            dic[prefix] = dic[prefix] + 1
        return count
