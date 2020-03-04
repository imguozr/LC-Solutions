from typing import List


class Solution:
    def trap_1(self, height: List[int]) -> int:
        """
            Brutal Force. Think in columns.
            For each column, find the highest left and right wall.
            Mark the minimum of two max as valid wall.
            Compute water.

            Time Complexity: O(n^2)
            Space Complexity: O(1)
        """

        res = 0
        for i in range(1, len(height) - 1):
            max_left, max_right = 0, 0
            for j in range(i - 1, -1, -1):
                if height[j] > max_left:
                    max_left = height[j]
            for j in range(i + 1, len(height)):
                if height[j] > max_right:
                    max_right = height[j]
            valid_wall = min(max_left, max_right)
            if valid_wall > height[i]:
                res += valid_wall - height[i]
        return res

    def trap_2(self, height: List[int]) -> int:
        """
            Dynamic Programming. Use 2 lists to reduce time cost.
            Calculate highest left and right wall in the beginning.

            Time Complexity: O(n)
            Space Complexity: O(n)
        """

        res, n = 0, len(height)
        max_left, max_right = [0] * n, [0] * n
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        for i in range(1, n - 1):
            valid_wall = min(max_left[i], max_right[i])
            if valid_wall > height[i]:
                res += valid_wall - height[i]
        return res

    def trap_3(self, height: List[int]) -> int:
        """
            Two pointers. Use 2 integers to record highest left and right wall.
            Proof:
                We know max_left = max(max_left, height[left - 1]) and
                        max_right = max(max_right, height[right + 1])
                So, max_left <= height[left - 1]
                    max_right <= height[right + 1]
                If height[left - 1] < height[right + 1]:
                    max_left must < max_right
            So, we can get max_left and max_right in one pass.

            Time Complexity: O(n)
            Space Complexity: O(1)
        """

        res, n = 0, len(height)
        max_left, max_right = 0, 0
        left, right = 1, n - 2

        for i in range(1, n - 1):
            if height[left - 1] < height[right + 1]:
                max_left = max(max_left, height[left - 1])
                if max_left > height[left]:
                    res += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right + 1])
                if max_right > height[right]:
                    res += max_right - height[right]
                right -= 1
        return res

    def trap_4(self, height: List[int]) -> int:
        """
            Use stack to store the index of each wall.
            If current height <= stack peek height:
                current height -> stack
                current ++
            While stack not empty and current height > stack peek height
                pop
                Calculate water amount.
        """

        res, stack = 0, []
        idx = 0
        while idx < len(height):
            while stack and height[idx] > height[stack[-1]]:
                h = height[stack[-1]]
                stack.pop()
                if not stack:
                    break
                distance = idx - stack[-1] - 1
                valid_wall = min(height[idx], height[stack[-1]])
                res += distance * (valid_wall - h)
            stack.append(idx)
            idx += 1
        return res
