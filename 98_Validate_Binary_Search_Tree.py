class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        The first idea is to traverse the BST in-orderly.
        If the BST is valid, the generated list will be sorted already.
        Solution 1 and 2 traverse the BST recursively and iteratively.
        Also, we can apply dfs to check its validation.
        Solution 3 and 4 search recursively and iteratively.
    """

    def isValidBST_1(self, root: TreeNode) -> bool:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        tree = inorder(root)
        for i in range(len(tree) - 1):
            if tree[i] >= tree[i + 1]:
                return False
        return True

    def isValidBST_2(self, root: TreeNode) -> bool:
        stack, tmp = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.val <= tmp:
                return False
            tmp = root.val

            root = root.right
        return True

    def isValidBST_3(self, root: TreeNode) -> bool:
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not dfs(node.right, val, upper):
                return False
            if not dfs(node.left, lower, val):
                return False
            return True

        return dfs(root)

    def isValidBST_4(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            val = node.val
            if val <= lower or val >= upper:
                return False
            stack.append((node.right, val, upper))
            stack.append((node.left, lower, val))
        return True
