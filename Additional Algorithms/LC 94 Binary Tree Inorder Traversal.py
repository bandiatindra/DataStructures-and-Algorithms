# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return None
        
        #Recursive Algo
        res = []
        def inorder(root):
            
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        #inorder(root)
        #return res
        
        #Iterative algo
        
        new_res = []
        def iterative_inorder(root):
            cur = root
            
            st = []
            while cur is not None or len(st)!=0:
                while cur:
                    st.append(cur) #Keep on adding nodes to stack by traversing left
                    cur = cur.left
                cur = st.pop() #When there is no more left node, pop out the element from stack
                new_res.append(cur.val) #Then append this in the result 
                cur = cur.right # Navigate to the right and continue this loop
                
        iterative_inorder(root)
        return new_res
    
            
            
            
            
            
            
        
        