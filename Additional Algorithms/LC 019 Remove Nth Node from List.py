# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new_head = head
        length = 0
        while new_head is not None:
            length = length + 1
            new_head = new_head.next
        index_remove = length - n 
        
        dummy = ListNode(0)
        
        dummy.next = head
        first = dummy
        for i in range(length):
            if i == index_remove:
                first.next = first.next.next
            first = first.next
        return dummy.next
