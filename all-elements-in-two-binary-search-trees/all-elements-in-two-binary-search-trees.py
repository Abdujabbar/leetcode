# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.items = []
        
        def dfs(r: TreeNode):
            if not r:
                return
            dfs(r.left)
            dfs(r.right)
            self.items.append(r.val)
        
        dfs(root1)
        dfs(root2)
        
        self.items.sort()
        
        return self.items
        