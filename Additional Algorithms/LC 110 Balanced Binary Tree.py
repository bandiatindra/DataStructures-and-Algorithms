# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def height(self, root: Optional[TreeNode]):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height,right_height) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        # Check ifheight(Left tree) - height(right tree) <=1 And also the left and right tree are also balanced recursively
        
        if abs(self.height( root.left) - self.height( root.right)) <= 1 \
        and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
    