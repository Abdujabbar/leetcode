# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.ans = []
        
        def dfs(r: TreeNode, seq, total):
            
            if r and not r.left and not r.right and total + r.val == targetSum:
                self.ans.append(seq + [r.val])
           
            if not r:
                return
            
            dfs(r.left, seq + [r.val], total + r.val)
            dfs(r.right, seq + [r.val], total + r.val)
        
        dfs(root, [], 0)
        
        return self.ans
            
        
        