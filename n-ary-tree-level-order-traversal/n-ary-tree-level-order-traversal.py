"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        ans = []
        
        while q:
            sz = len(q)
            row = []
            while sz:
                target = q.popleft()
                row.append(target.val)
                for child in target.children:
                    q.append(child)
                sz -= 1
            ans.append(row)
        
        return ans