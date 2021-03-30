# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0
        
        def dfs(r: TreeNode):
            if not r:
                return
            
            if low <= r.val <= high:
                self.ans += r.val
            
            # if r.val < low:
            dfs(r.left)
            
            # if r.val > high:
            dfs(r.right)
        
        dfs(root)
        
        return self.ans