# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.depth = 10 ** 10
        def dfs(r: TreeNode, depth):
            if not r:
                return
            if not r.left and not r.right:
                self.depth = min(self.depth, depth)
                return
            
            if r.left:
                dfs(r.left, depth + 1)
            
            if r.right:
                dfs(r.right, depth + 1)
        
        dfs(root, 1)
        
        return self.depth