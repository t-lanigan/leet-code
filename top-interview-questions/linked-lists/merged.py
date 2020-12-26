# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        ## Recursive solution  
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val <= l2.val:
            merged = l1
            merged.next = self.mergeTwoLists(l1.next, l2)
        else:
            merged = l2
            merged.next = self.mergeTwoLists(l1, l2.next)
            
        return merged
            