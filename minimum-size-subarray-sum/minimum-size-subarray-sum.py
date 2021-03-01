class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = 0
        best = len(nums)
        left = 0
        for right in range(len(nums)):
            s += nums[right]
            while s >= target and left < len(nums):
                best = min(best, right - left + 1)
                s -= nums[left]
                left += 1
        if best == len(nums) and sum(nums) >= target:
            return len(nums)
        return best if best < len(nums) else 0 