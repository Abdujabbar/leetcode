# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root or val > root.val:
            return TreeNode(val, root, None)
        
        node = root
        
        while node.right:
            if val > node.right.val:
                node.right = TreeNode(val, node.right, None)
                return root
            node = node.right
        
        node.right = TreeNode(val)
        
        return root