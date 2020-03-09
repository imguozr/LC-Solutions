# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:
        """
            Recursively.
        """
        if not head or not head.next:
            return head

        nxt = head.next
        head.next = self.swapPairs1(head.next.next)
        nxt.next = head
        return nxt

    def swapPairs(self, head: ListNode) -> ListNode:
        """
            Iteratively.
        """

        if not head or not head.next:
            return head

        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            first = pre.next
            second = first.next
            nxt = second.next

            first.next = nxt
            second.next = first
            pre.next = second

            pre = first

        return dummy.next