# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         
        if not head.next and n==1:
            return None
        
        slow, fast = head, head
        
        for i in range(n):
            if not fast.next:
                return head.next
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        
        return head
        