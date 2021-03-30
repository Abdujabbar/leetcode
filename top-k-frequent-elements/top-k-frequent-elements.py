from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        
        ans = []
        for item in sorted(mp.items(), key=lambda x: -x[1]):
            ans.append(item[0])
            if len(ans) >= k:
                break
        
        return ans
        