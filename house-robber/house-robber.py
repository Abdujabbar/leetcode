class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        ans = [
            nums[0],
            nums[1],
            nums[0] + nums[2]
        ]
        
        for i in range(3, len(nums)):
            ans.append(max(nums[i] + ans[i - 2], nums[i] + ans[i - 3]))
        
        
        return max(ans)