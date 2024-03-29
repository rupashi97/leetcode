# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root: return []
        queue = [root]
        res = []
        
        while queue:
            
            curLevel, size = [], len(queue)
            
            for i in range(size):             
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                            
                curLevel.append(node.val)
            
            res.append(curLevel)
            
        
        return res
                
            
            
            
        
        
        
                    