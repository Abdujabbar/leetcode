# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.ans = 0
        def inOrder(r: TreeNode):
            if not r:
                return
            
            inOrder(r.left)
            self.count += 1
            if self.count == k and r:
                self.ans = r.val 
            inOrder(r.right)
        
        inOrder(root)
        
        return self.ans