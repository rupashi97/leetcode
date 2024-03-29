'''
Merging two sorted linked lists in ascending order
Used merge sort logic
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my solution
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:

        list3 = prevNode = ListNode()

        while list1 and list2:

            newNode = ListNode()
            prevNode.next = newNode

            if list1.val <= list2.val:
                newNode.val = list1.val
                list1 = list1.next

            else:
                newNode.val = list2.val
                list2 = list2.next

            prevNode = newNode

        while list1:
            newNode = ListNode(list1.val)
            prevNode.next = newNode
            list1 = list1.next
            prevNode = newNode

        while list2:
            newNode = ListNode(list2.val)
            prevNode.next = newNode
            list2 = list2.next
            prevNode = newNode

        return list3.next


# discussion solution
class Solution2:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
