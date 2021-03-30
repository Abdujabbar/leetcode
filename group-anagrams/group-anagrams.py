from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            ls = list(s)
            ls.sort()
            mp["".join(ls)].append(s)
        
        return mp.values()
        