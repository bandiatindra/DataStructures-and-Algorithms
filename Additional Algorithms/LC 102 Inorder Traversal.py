# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections
        if root is None:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)
        while len(queue)!=0:
            qlen = len(queue)
            level = []
            
            
            for i in range(qlen):
                
                node = queue.popleft()
                if node is not None:
                    level.append(node.val)
               
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
         
            result.append(level)
        return result
        