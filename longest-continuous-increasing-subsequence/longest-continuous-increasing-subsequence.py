class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        best = 0
        nums.append(-10 ** 9)
        for right in range(1, len(nums)):
            if nums[right] <= nums[right - 1]:
                best = max(right - left, best)
                left = right
        
        return best