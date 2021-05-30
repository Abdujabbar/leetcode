class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counter = 0
        
        for i in range(len(s) - 2):
            ss = set()
            for j in range(i, i + 3):
                ss.add(s[j])
            if len(ss) == 3:
                counter += 1
        
        
        return counter
                