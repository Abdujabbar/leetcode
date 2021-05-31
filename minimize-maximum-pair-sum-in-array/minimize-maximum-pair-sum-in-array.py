from collections import Counter
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        best = 0
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            best = max(best, nums[left] + nums[right])
            left += 1
            right -= 1
        
        
        return best