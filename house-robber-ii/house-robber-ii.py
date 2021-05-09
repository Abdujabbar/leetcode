class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        def helper(arr):
            if len(arr) < 3:
                return max(arr)
            
            ans = [
                arr[0],
                arr[1],
                arr[0] + arr[2]
            ]
            
            for i in range(3, len(arr)):
                ans.append(max(arr[i] + ans[i - 2], arr[i] + ans[i - 3]))
            
            return max(ans)
        
        return max(helper(nums[1:]), helper(nums[:-1]))