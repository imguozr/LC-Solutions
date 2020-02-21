class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle_1(self, head: ListNode) -> bool:
        """
            Hash set.
        """
        node_set = set()
        while head:
            if head in node_set:
                return True
            else:
                node_set.add(head)
            head = head.next
        return False

    def hasCycle_2(self, head: ListNode) -> bool:
        """
            Two pointers.
        """
        if not head or not head.next:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
