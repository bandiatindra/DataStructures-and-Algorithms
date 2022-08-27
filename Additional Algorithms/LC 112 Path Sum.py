# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # Recursion
#         if root is None:
#             return False
#         sum = targetSum
        
#         sum = sum - root.val
#         if root.left is None and root.right is None:
#             if sum==0:
#                 return True
#             else:
#                 return False
                
        #return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
        # Iterative
        
        if root is None:
            return False

        stack = [(root,targetSum - root.val),]
        while stack:
            node, curr_sum = stack.pop()
            if node.left is None and node.right is None and curr_sum == 0:
                return True
            if node.right is not None:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left is not None:
                stack.append((node.left, curr_sum - node.left.val))
        return False
            
                  
            
                  
        
        
        
        
            