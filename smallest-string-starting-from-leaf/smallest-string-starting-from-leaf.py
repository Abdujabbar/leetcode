# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        self.strs = []
        def dfs(r: TreeNode, sequence):
            if not r:
                return
            
            dfs(r.left, alphabet[r.val] + sequence)
            dfs(r.right, alphabet[r.val] + sequence)
            
            if not r.left and not r.right:
                self.strs.append(alphabet[r.val] + sequence)
            
           
        
        dfs(root, "")
        
        self.strs.sort()
        
        return self.strs[0]
        