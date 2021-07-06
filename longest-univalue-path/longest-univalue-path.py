# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(r:TreeNode):
            if not r:
                return 0
            
            left = dfs(r.left)
            right = dfs(r.right)
            
            leftCounter = 0
            rightCounter = 0
            
            if r.left and r.left.val == r.val:
                leftCounter += left + 1
            
            if r.right and r.right.val == r.val:
                rightCounter += right + 1
            
            self.ans = max(self.ans, leftCounter + rightCounter)
            return max(leftCounter, rightCounter)
        
        dfs(root)
        
        return self.ans
            
            
            

            