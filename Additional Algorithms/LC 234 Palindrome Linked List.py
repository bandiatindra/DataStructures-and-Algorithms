# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Approach 1 - Put linked list into array and reverse the array. But not in O(1) space. 
        arr=[]
        
        while head is not None:
            arr.append(head.val)
            head = head.next
        
        return arr == arr[::-1]
    
        # Approach 2 -  O(1) space - Advanced. 
        # We will need to reverse the 2nd half of the Linked List. 
        
        
        