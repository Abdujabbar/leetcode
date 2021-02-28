from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        for i in range(0, len(s2) - len(s1) + 1):
            c = Counter(s2[i:i+len(s1)])
            if c == cnt:
                return True
            
        return False