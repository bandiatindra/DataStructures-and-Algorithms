# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # Created a hash and add the has value of each node. If the last node is pointing to an existing node then its hash will exist!) 
#         new_set = set()
        
#         while head is not None:
#             if head in new_set:
#                 return True
#             else:
#                 new_set.add (head)
#             head = head.next
#         # If current node becomes NULL then we have reached the end of linked list and its not cyclic. 
#         return False
    
    # Approach 2 - Floyd's Cycle Finding Algorithm  - If cyclic the nthe 2 pointers will meet each other, otherwise fast pointer will always reach the end first and will point to None. 
        if head is None:
            return False
    
        slow_pointer = head
        fast_pointer = head.next
        while slow_pointer!= fast_pointer:
            if fast_pointer is None or fast_pointer.next is None: 
                return False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return True
    