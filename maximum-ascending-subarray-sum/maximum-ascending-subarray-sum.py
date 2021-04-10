class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        best = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                s += nums[i]
            else:
                best = max(best, s)
                s = nums[i]
        best = max(s, best)
        return best