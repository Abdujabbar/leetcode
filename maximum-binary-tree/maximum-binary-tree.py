# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def solver(nums):
            if not nums:
                return None
            mx = max(nums)
            index = nums.index(mx)
            left = nums[:index]
            right = nums[index + 1:]
            node = TreeNode(mx)
            node.left = solver(left)
            node.right = solver(right)
            return node
        
        return solver(nums)
            