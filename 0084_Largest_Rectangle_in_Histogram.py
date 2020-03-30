from typing import List


class Solution:
    """
    Use monotone stack. (When values of two sides determine value of middle)
    Rule (increasing stack):
        If new element is larger than top, push it in
        If new element is smaller than top, pop elements out
            until top is less than new element.

    See # 42.
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add guard elements, avoid 2 scenarios:
        # 1. stack is empty when pop;
        # 2. stack is not empty after iteration.
        # The left 0 will keep stack not empty
        # because it's smaller than any of the elements
        # The right 0 will make all elements out of stack
        # because it's smaller than any of the elements
        heights = [0] + heights + [0]
        stack, res = [], 0

        # Here comes the new element
        for i in range(len(heights)):
            # new element is less than top
            while stack and heights[stack[-1]] > heights[i]:
                # pop top out as current height
                curr_height = heights[stack.pop()]
                # there exists same value
                while stack and curr_height == heights[stack[-1]]:
                    stack.pop()

                # now the top is the left boundary of the maximum rectangle
                curr_width = i - stack[-1] - 1
                # update maximum area
                res = max(res, curr_height * curr_width)
            # new element is bigger than top, push it in
            stack.append(i)

        return res
