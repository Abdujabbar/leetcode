# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSame(p: TreeNode, q: TreeNode):
            if not p and not q:
                return True
            
            if p and not q or not p and q:
                return False
            
            if p.val != q.val:
                return False
            
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        
        self.ans = False
        
        def dfs(r: TreeNode):
            if not r:
                return
            if isSame(r, subRoot) and not self.ans:
                self.ans = True
                return
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        
        return self.ans
            