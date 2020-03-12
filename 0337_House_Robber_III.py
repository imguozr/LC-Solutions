# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        dp in tree form.
        https://leetcode.com/problems/house-robber-iii/discuss/79330/step-by-step-tackling-of-the-problem
    """

    def rob1(self, root: TreeNode) -> int:
        dic = {}

        def helper(root):
            if not root:
                return 0
            if root in dic:
                return dic[root]

            val = 0
            if root.left:
                val += helper(root.left.left) + helper(root.left.right)
            if root.right:
                val += helper(root.right.left) + helper(root.right.right)

            val = max(val + root.val, helper(root.left) + helper(root.right))
            dic[root] = val
            return val

        return helper(root)

    def rob2(self, root: TreeNode) -> int:
        """
            Reduce space complexity.
        """
        def helper(root):
            if not root:
                return [0, 0]

            left = helper(root.left)
            right = helper(root.right)
            res = [0] * 2

            # next level of root
            res[0] = max(left) + max(right)
            # root + next of next level of root
            res[1] = root.val + left[0] + right[0]

            return res

        res = helper(root)
        return max(res)
