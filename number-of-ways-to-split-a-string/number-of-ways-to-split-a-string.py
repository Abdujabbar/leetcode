m = 10**9 + 7

class Solution:
    def numWays(self, s: str) -> int:
        total = s.count('1')
        
        n = len(s)
        
        if total % 3 != 0:
            return 0
        
        if total == 0:
            return (((n - 1) * (n - 2)) // 2) % m
        
        f1 = 0
        f2 = 0
        
        t = 0
        for c in s:
            t += int(c)
            if t == (total // 3):
                f1 += 1
            
            if t == (total // 3) * 2:
                f2 += 1
        
        
        return (f1 * f2) % m