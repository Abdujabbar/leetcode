"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([root])
        
        
        while queue:
            prev = None
            sz = len(queue)
            while sz:
                
                target = queue.popleft()
                                
                if target.left:
                    queue.append(target.left)
                    
                if target.right:
                    queue.append(target.right)
                
                if prev:
                    prev.next = target
                
                prev = target
                
                sz -= 1
        
        return root