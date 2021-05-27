from collections import defaultdict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 1:
            return 1
        mp = defaultdict(int)
        best = 0
        left = 0
        
        for right in range(len(tree)):
            mp[tree[right]] += 1
            
            if len(mp) == 2:
                best = max(right - left + 1, best)
            
            while len(mp) > 2:
                mp[tree[left]] -= 1
                if mp[tree[left]] == 0:
                    del mp[tree[left]]

                left += 1
                
        return max(best, right - left + 1)
            