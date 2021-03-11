# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def dfs(r: TreeNode, target):
            if not r:
                return r
            
            if r.val == target:
                return r
            
            return dfs(r.left, target) or dfs(r.right, target)
        
        return dfs(root, val)