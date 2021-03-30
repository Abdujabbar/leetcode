# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sums_map = defaultdict(int)
        def dfs(r: TreeNode, depth):
            if not r:
                return
            
            dfs(r.left, depth + 1)
            self.sums_map[depth] += r.val
            dfs(r.right, depth + 1)
        
        dfs(root, 0)
        max_index = 0
        
        for k, c in self.sums_map.items():
            if max_index < k:
                max_index = k
        
        return self.sums_map[max_index]
        
        