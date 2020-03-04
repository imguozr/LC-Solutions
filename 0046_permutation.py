from typing import List


class Solution1:
    """
        Backtrack.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, [], res)
        return res

    def backtrack(self, nums, track, res):
        if len(track) == len(nums):
            # NOTICE: In python, variables are references.
            # If append track directly, Line 23 (pop) will erase all sub-lists.
            res.append(track[:])
            return

        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.backtrack(nums, track, res)
            track.pop()


class Solution2:
    """
        Generate directly.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms
