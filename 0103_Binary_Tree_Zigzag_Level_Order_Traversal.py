from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        BFS
    """

    def zigzagLevelOrder_1(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        res, queue = [], deque([root])
        level = 0
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2:
                tmp = tmp[::-1]
            res.append(tmp)
            level += 1
        return res

    def zigzagLevelOrder_2(self, root: TreeNode) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        res, queue = [], deque([root])
        level = 0
        while queue:
            res.append(deque([]))
            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2:
                    res[level].appendleft(node.val)
                else:
                    res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return res
