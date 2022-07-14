'''
Reverse a linked list

Implement 2 ways
1. Iterative
2. Recursive
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Slow iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        p = head.next
        head.next = None

        while p:
            q = p.next
            p.next = head
            head = p
            p = q

        return head


# Fast iterative
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur

        return prev


# Recursive ~ Slower than iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def _reverse(prev, node):
            if not node:
                return prev

            n = node.next
            node.next = prev
            return _reverse(node, n)

        return _reverse(None, head)
