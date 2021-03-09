# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, root)
        def dfs(r, h):
            if not r:
                return
            if h == d - 1:
                leftNode = r.left
                rightNode = r.right
                r.left = TreeNode(v)
                r.right = TreeNode(v)
                r.left.left = leftNode
                r.right.right = rightNode
            else:
                dfs(r.left, h + 1)
                dfs(r.right, h + 1)
        
        dfs(root, 1)
        return root
