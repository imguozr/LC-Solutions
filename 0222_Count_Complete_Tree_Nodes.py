# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes1(self, root: TreeNode) -> int:
        return self.countNodes1(root.left) + self.countNodes1(root.right) + 1 if root else 0

    def countNodes2(self, root: TreeNode) -> int:

        def compute_depth(node):
            """
            Compute tree depth of all complete levels
            """
            depth = 0
            while node.left:
                node = node.left
                depth += 1
            return depth

        def exists(idx, depth, node):
            left, right = 0, 2 ** depth - 1
            for d in range(depth):
                pivot = (left + right) // 2
                if idx <= pivot:
                    node = node.left
                    right = pivot
                else:
                    node = node.right
                    left = pivot + 1
            return node is not None

        if not root:
            return 0

        depth = compute_depth(root)
        if not depth:
            return 1

        left, right = 1, 2 ** depth - 1
        while left <= right:
            pivot = (left + right) // 2
            if exists(pivot, depth, root):
                left = pivot + 1
            else:
                right = pivot - 1

        return left + 2 ** depth - 1
