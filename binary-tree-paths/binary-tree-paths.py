# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        def dfs(r: TreeNode, path):
            if not r:
                return
            
            if not r.left and not r.right:
                self.paths.append(path + [str(r.val)])
                return
            
            dfs(r.left, path + [str(r.val)])
            dfs(r.right, path + [str(r.val)])
        
        dfs(root, [])
        
        return ["->".join(x) for x in self.paths]