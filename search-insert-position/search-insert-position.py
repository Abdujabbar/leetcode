class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            m = (left + right) // 2
            
            if nums[m] == target:
                return m
            if nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        
        
        return left