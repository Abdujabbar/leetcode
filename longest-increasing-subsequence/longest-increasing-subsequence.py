import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        def binarySearch(nums, target):
            left = 0
            right = len(nums)
            
            while left < right:
                m = (left + right) // 2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    right = m
                else:
                    left = m + 1
            
            return left
        
        for num in nums:
            pos = binarySearch(sub, num)
            
            if not sub or pos >= len(sub):
                sub.append(num)
            else:
                sub[pos] = num

        return len(sub)