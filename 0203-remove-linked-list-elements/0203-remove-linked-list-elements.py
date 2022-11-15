# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head: return head
        
        while head and head.val==val:
            head = head.next
            
        prev = ListNode(-1)
        cur = head
            
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur 
            cur = cur.next
            
            
        return head if not None else []