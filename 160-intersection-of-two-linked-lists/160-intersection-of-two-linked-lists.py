# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        hashS = set()
        
        a, b = headA, headB
        
        while a and b:
            
            if a in hashS:
                return a
            
            hashS.add(a)
            
            if b in hashS:
                return b
            hashS.add(b)
            
            a = a.next
            b = b.next
            
        
        while a:
            if a in hashS:
                return a
            hashS.add(a)
            a = a.next
            
        while b:
            if b in hashS:
                return b
            hashS.add(b)
            b = b.next
            
            
        return None
        