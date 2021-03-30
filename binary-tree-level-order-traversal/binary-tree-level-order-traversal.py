# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        
        while q:
            sz = len(q)
            row = []
            while sz:
                target = q.popleft()
                row.append(target.val)
                if target.left:
                    q.append(target.left)
                
                if target.right:
                    q.append(target.right)
                sz -= 1
            ans.append(row)
        
        return ans
                
        
        