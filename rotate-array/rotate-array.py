class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[(len(nums) + (len(nums) - k + i)) % len(nums)])
        
        for i in range(len(ans)):
            nums[i] = ans[i]