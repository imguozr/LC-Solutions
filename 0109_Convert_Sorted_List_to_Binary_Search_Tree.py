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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
            Use slow and fast pointers to find middle node of linked list.
        """
        def find_middle(node):
            prev, slow, fast = None, node, node
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow

        if not head:
            return None

        mid = find_middle(head)
        pivot = TreeNode(mid.val)

        if mid == head:
            return pivot

        pivot.left = self.sortedListToBST(head)
        pivot.right = self.sortedListToBST(mid.next)
        return pivot
