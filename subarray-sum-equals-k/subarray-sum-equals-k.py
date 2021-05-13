from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = {0: 1}
        s = 0
        
        for num in nums:
            s += num
            
            if s - k in mp.keys():
                ans += mp[s - k]
            
            if s not in mp:
                mp[s] = 1
            else:
                mp[s] += 1
            
        return ans