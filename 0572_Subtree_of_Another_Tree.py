# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s:
            return False
        return self.is_sub(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_sub(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        return s.val == t.val and self.is_sub(s.left, t.left) and self.is_sub(s.right, t.right)
