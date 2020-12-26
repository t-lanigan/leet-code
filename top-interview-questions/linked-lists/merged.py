# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
  
        # A dummy node to store the result 
        merged = ListNode(0) 

        # Tail stores the last node 
        tail = merged 
        while True: 

            # If any of the list gets completely empty 
            # directly join all the elements of the other list 
            if l1 is None: 
                tail.next = l2 
                break
            if l2 is None: 
                tail.next = l1 
                break

            # Compare the data of the lists and whichever is smaller is 
            # appended to the last of the merged list and the head is changed 
            if l1.val <= l2.val: 
                tail.next = l1 
                l1 = l1.next
            else: 
                tail.next = l2 
                l2 = l2.next

            # Advance the tail 
            tail = tail.next

        # Returns the head of the merged list 
        return merged.next