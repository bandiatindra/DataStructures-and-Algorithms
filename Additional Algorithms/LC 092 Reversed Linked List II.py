# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        prev = None
        curr = head
        index = 0
        # First move in the list till the left position before we need to reverse the list. We use prev and curr pointers
        while left >1:
            prev = curr
            curr = curr.next
            left= left-1
            right=right-1
        new_prev, tail = prev, curr
        
        # Then we follow the reversed LinkedList logic to reverse the section b/w left and right. 
        while right>0:
            temp = curr.next # Remember the next node. 
            curr.next = prev # Point current pointer to prev
            prev  = curr # Make prev to current
            curr = temp # Move to the next one in the list through the temp 
            right=right-1
        # Note we only make changes till the right bound. No changes are done to the list after that.
        
        # Lastly we need to join this section with the previous section. Basically we need to do 2 things - 
        # 1. Connect the end of previous section with the reversed list. 
        # 2. Connect the reversed list correctly with remainder of the list (this is the current position of pointer)
        if new_prev is not None:
            new_prev.next = prev
        else:
            head = prev
        tail.next = curr
        return head
                
            
            
            
           
                
                
           
        
        
