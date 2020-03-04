from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        BFS.
    """

    def levelOrder_1(self, root: TreeNode) -> List[List[int]]:
        """
            Solve recursively.
        """

        def helper(node, level, result):
            if not node:
                return
            if len(result) == level:
                result.append([])

            result[level].append(node.val)
            if node.left:
                helper(node.left, level + 1, result)
            if node.right:
                helper(node.right, level + 1, result)

        if not root:
            return []
        res = []
        helper(root, 0, res)
        return res

    def levelOrder_2(self, root: TreeNode) -> List[List[int]]:
        """
            Solve iteratively by using queue.
        """
        from collections import deque
        if not root:
            return []
        res, queue = [], deque([root])
        level = 0
        while queue:
            res.append([])
            for i in range(len(queue)):
                node = queue.popleft()
                res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return res

    def levelOrder_3(self, root: TreeNode) -> List[List[int]]:
        """
            Solve iteratively by using stack.
        """
        if not root:
            return []
        res, stack = [], [(root, 0)]
        while stack:
            # NOTICE: Time complexity of stack.pop(0) is O(n)
            node, level = stack.pop(0)
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return res
