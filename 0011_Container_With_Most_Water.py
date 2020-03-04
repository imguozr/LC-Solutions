from typing import List


class Solution:
    """
        Two pointers.
        Set two pointers at start and end respectively, move the shorter one to the center.
        Record the maximum area, return it when two pointers coincide.
    """

    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights) < 2:
            return 0

        res = 0
        left, right = 0, len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            if area > res:
                res = area
            if height == heights[left]:
                left += 1
            else:
                right -= 1
        return res
