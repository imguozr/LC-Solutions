import functools


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        Same thought as LC96, we can generate trees recursively.
        If the root of tree is i
        The left subtree has a sequence of [start ... i - 1]
        The right subtree has a sequence of [i + 1 ... end]

        Can use cache to improve performance.
    """

    def generateTrees(self, n: int) -> list[TreeNode]:
        if not n:
            return []
        return self.generate_subtrees(1, n)

    @functools.lru_cache(None)
    def generate_subtrees(self, start, end):
        res = []
        if end < start:
            return [None]

        for i in range(start, end + 1):
            # More concise than declare left/right list. Have same performance.
            for left in self.generate_subtrees(start, i - 1):
                for right in self.generate_subtrees(i + 1, end):
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
