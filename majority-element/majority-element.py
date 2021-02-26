class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        sz = len(nums)
        while left < len(nums):
            right = left + 1
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            
            if right - left > sz // 2:
                return nums[left]
            left = right
            