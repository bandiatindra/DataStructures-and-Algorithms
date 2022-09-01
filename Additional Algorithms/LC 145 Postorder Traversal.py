# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return None
        res = []
        def postorder(root):
            
            if root is None:
                return
            postorder(root.left)
            
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res
    
    