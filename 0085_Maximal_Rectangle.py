from typing import List


class Solution:
    """
    Use monotone stack.

    Similar as # 42, 84
    """

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largest_area(heights))

        return max_area

    def largest_area(self, heights):
        """
        Compute largest area
        :param heights:
        :return:
        """
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
