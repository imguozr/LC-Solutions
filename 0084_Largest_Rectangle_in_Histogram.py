from typing import List


class Solution:
    """
    Use monotone stack. (When values of two sides determine value of middle)

    See # 42.
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack, res = [], 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                curr_height = heights[stack.pop()]
                while stack and curr_height == heights[stack[-1]]:
                    stack.pop()

                curr_width = i - stack[-1] - 1
                res = max(res, curr_height * curr_width)
            stack.append(i)

        return res
