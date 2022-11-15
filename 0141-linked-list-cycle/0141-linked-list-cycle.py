# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        p = head
        hashs = set()
        
        while p:
            if p in hashs: return True
            hashs.add(p)
            p = p.next
            
        return False 
    