# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Define two pointers fast and slow.
    Make fast move n steps, then move fast and slow together until fast reaches the end
    At this, time, slow is the previous node of n-th node from end.
    Do remove.
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            # head is n-th node from end
            # return head.next directly,
            # counting as remove head
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
