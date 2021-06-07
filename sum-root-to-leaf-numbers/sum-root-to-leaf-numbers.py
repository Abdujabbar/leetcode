# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0
        
        def helper(r: TreeNode, path):
            if not r:
                return
            
            if not r.left and not r.right:
                self.total += int(path + str(r.val))
            
            # path += str(r.val)
            helper(r.left, path + str(r.val))
            helper(r.right, path + str(r.val))
        
        helper(root, "")
        
        return self.total