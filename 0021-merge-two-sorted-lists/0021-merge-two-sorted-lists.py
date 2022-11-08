# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3 = head =  ListNode()
        
        while list1 and list2:
            node = ListNode()
            
            if list1.val<list2.val:
                node.val = list1.val
                list1 = list1.next   
            else:
                node.val = list2.val
                list2 = list2.next
                
            list3.next = node
            list3 = node
            
        while list1:
            node = ListNode(list1.val)
            list3.next = node
            list3 = node
            list1 = list1.next
        
        while list2:
            node = ListNode(list2.val)
            list3.next = node
            list3 = node
            list2 = list2.next
            
        
        return head.next     