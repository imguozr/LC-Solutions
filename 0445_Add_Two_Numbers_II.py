# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
        Because the order of vals in linked list is correct,
        should use 2 stacks to record vals in linked list.
        So when pop(), lower digits will come out first.

        We can insert nodes at the head of linked list.
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        res = dummy = ListNode(0)
        _sum = 0
        while stack1 or stack2 or _sum:
            _sum += (stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0)
            nxt = ListNode(_sum % 10)
            _sum //= 10
            # Insert at head
            nxt.next = dummy.next
            dummy.next = nxt
        return res.next
