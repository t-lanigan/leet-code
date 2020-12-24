# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):  # Iterative
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev 
            prev = curr
            curr = nextTemp
        return prev