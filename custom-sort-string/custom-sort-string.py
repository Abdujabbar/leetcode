from collections import Counter
class Solution:
    def customSortString(self, order: str, in_str: str) -> str:
        cnt = Counter(in_str)
        
        result = ""
        
        for c in order:
            if c in cnt:
                result += (cnt[c] * c)
                cnt.pop(c)
        
        for k, v in cnt.items():
            result += (k * v)
        
        return result
        
        