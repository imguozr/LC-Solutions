import bisect
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    idx = 0

    def bstFromPreorder1(self, preorder: List[int]) -> TreeNode:
        """
            Use lower and upper limits to track
        """
        def helper(lower=float('-inf'), upper=float('inf')):
            if self.idx == len(preorder):
                return None

            val = preorder[self.idx]
            if lower > val or val > upper:
                return None

            self.idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        return helper(0)

    def bstFromPreorder2(self, preorder: List[int]) -> TreeNode:
        """
            Binary Search
        """
        def helper(i, j):
            if i == j:
                return None

            root = TreeNode(preorder[i])
            # find the idx of next # > preorder[i]
            mid = bisect.bisect(preorder, preorder[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root

        return helper(0, len(preorder))
