# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        Like # 572.
    """

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        return self.is_sub(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def is_sub(self, head, root):
        if not head:
            return True
        if not root:
            return False
        if head.val != root.val:
            return False
        return self.is_sub(head.next, root.left) or self.is_sub(head.next, root.right)
