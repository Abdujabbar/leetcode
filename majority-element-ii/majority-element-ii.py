class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        left = 0
        sz = len(nums)
        ans = []
        while left < len(nums):
            right = left + 1
            while right < len(nums) and nums[right] == nums[left]:
                right += 1
            
            if right - left > sz // 3:
                ans.append(nums[left])
            
            left = right
        
        return ans