from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    DFS.
    """

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def helper(node, remain_sum, path_nodes, path_list):
            if not node:
                return

            path_nodes.append(node.val)

            if remain_sum == node.val and not node.left and not node.right:
                path_list.append(path_nodes[:])
            else:
                helper(node.left, remain_sum - node.val, path_nodes, path_list)
                helper(node.right, remain_sum - node.val, path_nodes, path_list)

            path_nodes.pop()

        res = []
        helper(root, sum, [], res)
        return res
