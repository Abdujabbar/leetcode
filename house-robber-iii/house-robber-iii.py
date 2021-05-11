from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        rob_saved = {}
        not_rob_saved = {}
        
        def dfs(r: TreeNode, parent_robbed):
            if not r:
                return 0
            
            if parent_robbed:
                if r in rob_saved:
                    return rob_saved[r]
                
                rob_saved[r] = dfs(r.left, False) + dfs(r.right, False)
                
                return rob_saved[r]
            else:
                if r in not_rob_saved:
                    return not_rob_saved[r]
                
                rob = r.val + dfs(r.left, True) + dfs(r.right, True)
                
                not_rob = dfs(r.left, False) + dfs(r.right, False)
                
                
                not_rob_saved[r] = max(rob, not_rob)
                return not_rob_saved[r] 
        
        return dfs(root, False)