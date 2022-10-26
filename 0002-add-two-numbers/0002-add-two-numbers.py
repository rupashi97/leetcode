# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = l1
        p2 = l2
        
        res = None
        carry = 0
        
        while p1 and p2:
            s = p1.val + p2.val + carry
            val, carry = s%10,  s//10
            
            temp = ListNode(val, None)
            if not res:
                head = res = ListNode(val, None)
            else:
                res.next = ListNode(val, None)
                res = res.next
            
            p1 = p1.next
            p2 = p2.next
            
        
        while p1:
            s = p1.val + carry
            val, carry = s%10,  s//10
            temp = ListNode(val, None)
            res.next = temp
            res = temp
            p1 = p1.next
            
        while p2:
            s = p2.val + carry
            val, carry = s%10,  s//10
            temp = ListNode(val, None)
            res.next = temp
            res = temp
            p2 = p2.next
        
        if carry:
            temp = ListNode(carry, None)
            res.next =  temp
            res = temp
        
        
        return head
        