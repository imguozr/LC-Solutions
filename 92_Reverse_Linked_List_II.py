# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverse_n(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    def reverse_n(self, head, n):
        """
            Reverse the next n nodes in the linked list.
        """
        if n == 1:
            return head
        last = self.reverse_n(head.next, n - 1)
        succ = head.next.next
        head.next.next = head
        head.next = succ
        return last
