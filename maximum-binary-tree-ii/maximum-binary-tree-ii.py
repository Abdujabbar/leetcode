# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        self.items = []
        def dfs(r:TreeNode):
            if not r:
                return
            dfs(r.left)
            self.items.append(r.val)
            dfs(r.right)
        
        dfs(root)
        
        self.items.append(val)
        print(self.items)
        def buildTree(nums):
            
            if not nums:
                return None
            max_value = max(nums)
            index = nums.index(max_value)
            left = nums[:index]
            right = nums[index + 1:]
            node = TreeNode(max_value)
            node.left = buildTree(left)
            node.right = buildTree(right)
            return node
        
        return buildTree(self.items)