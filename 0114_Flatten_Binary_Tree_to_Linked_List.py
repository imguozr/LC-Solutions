# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(node):
            """
            :param node: root node
            :return: rightmost node
            """
            if not node:
                return None

            if not node.left and not node.right:
                return node

            left = helper(node.left)
            right = helper(node.right)

            if left:
                left.right = node.right
                node.right = node.left
                node.left = None

            return right if right else left

        helper(root)
