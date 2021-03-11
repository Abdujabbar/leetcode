# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def addNode(r: TreeNode, value):
            if not r:
                return TreeNode(value)
            
            if r.val > value:
                r.left = addNode(r.left, value)
                
            if r.val < value:
                r.right = addNode(r.right, value)
                
            return r
        
        return addNode(root, val)