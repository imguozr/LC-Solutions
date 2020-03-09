# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
        https://github.com/labuladong/fucking-algorithm/blob/master/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/k%E4%B8%AA%E4%B8%80%E7%BB%84%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.md

        Split this problem into 2 parts:
            1. Reverse part of the linked list from a to b.
            2. Recursively solve problem.
    """

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        start, end = head, head
        for i in range(k):
            if end is None:
                return head
            end = end.next

        new_head = self.reverse(start, end)
        # end has reached the start of the next k-group
        start.next = self.reverseKGroup(end, k)
        return new_head

    def reverse(self, start, end):
        pre, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre
