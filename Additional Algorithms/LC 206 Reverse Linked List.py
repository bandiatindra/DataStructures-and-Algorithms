# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1 - 2 Pointers (Iterative Approach) 
        curr = head
        prev  = None
        
        while curr is not None:
            temp = curr.next # Remember the next node. 
            curr.next = prev # Point current pointer to prev
            prev  = curr # Make prev to current
            curr = temp # Move to the next one in the list through the temp 
        return prev
    
        
        
        
        