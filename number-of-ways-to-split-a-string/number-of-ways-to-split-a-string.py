m = 10**9 + 7

class Solution:
    def numWays(self, s: str) -> int:
        pf = list(accumulate(int(c) for c in s))
        cnt = Counter(pf)
        n  = pf[-1]
        
        if n % 3:
            return 0
    
        if n == 0:
            return ((len(s)-1)*(len(s)-2)//2)%m

        c = 0
        for p in pf[:-1]:
            if p*2 == n-p:
                c += cnt[n-p]

        return c%m