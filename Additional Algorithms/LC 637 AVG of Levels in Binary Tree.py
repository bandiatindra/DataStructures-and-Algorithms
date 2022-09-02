# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result = []
        queue = collections.deque()
        queue.append(root)
        while len(queue)!=0:
            qlen = len(queue)
            level_sum = 0
            
            
            for i in range(qlen):
                
                node = queue.popleft()
                
                level_sum = level_sum + node.val
               
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
         
            result.append(round((level_sum / qlen),5))
        return result
                
            
            
            

                


                