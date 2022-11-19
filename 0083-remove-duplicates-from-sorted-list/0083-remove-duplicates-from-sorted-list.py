# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None
        curr = head
        p = curr.next
        
        while p:
            if curr.val == p.val:
                curr.next = p.next
            else:
                curr = p 
            
            p = p.next
                
        return head
     