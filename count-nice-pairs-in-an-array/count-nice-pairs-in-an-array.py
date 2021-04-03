from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        memo = {}
        def rev(n):
            c = str(n)[::-1]
            return int(c)
        
        rev_nums = []
        counter = 0
        mp = {}
        for i in range(len(nums)):
            diff = nums[i] - rev(nums[i])
            if diff in mp:
                counter += mp[diff]
                mp[diff] += 1
            else:
                mp[diff] = 1
      
        return counter % (10 ** 9 + 7)