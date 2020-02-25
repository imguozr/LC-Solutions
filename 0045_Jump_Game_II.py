class Solution:
    """
        Greedy.
    """

    def jump(self, nums: list[int]) -> int:
        end, farthest, steps = 0, 0, 0
        for i in range(len(nums) - 1):
            # farthest position can reach
            farthest = max(farthest, nums[i] + i)
            if i == end:
                # update boundary
                end = farthest
                steps += 1
        return steps
