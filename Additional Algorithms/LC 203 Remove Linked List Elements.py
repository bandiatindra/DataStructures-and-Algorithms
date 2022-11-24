# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Approach 1 - Sentoinel Node - Basically adding a dummy node (head or tail). But getting 2 passes. 
#         new_head = head
#         length = 0
#         while new_head is not None:
#             length = length + 1
#             new_head = new_head.next
        
#         dummy = ListNode(0)
#         dummy.next = head
#         first = dummy
        
        
        
#         for i in range(length):
#             if first.next.val == val:
#                 first.next = first.next.next
#             else:
#                 first = first.next
#         return dummy.next
    
        # Approach 2 - Working with current & previous nodes.
        dummy = ListNode(0)
        dummy.next = head
        curr, prev = head, dummy
        
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return dummy.next
        