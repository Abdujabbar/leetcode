# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def binarySearchTreeValidator(r, left, right):
            if not r:
                return True
            
            return r.val > left and \
                    r.val < right and \
                    binarySearchTreeValidator(r.left, left, r.val) and \
                    binarySearchTreeValidator(r.right, r.val, right)
        
        
        return binarySearchTreeValidator(root, -10 ** 20, 10 ** 20)
            
                    