class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
        
        return len(nums) - 1 if nums[-1] > nums[0] else 0