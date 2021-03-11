from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        if s == t:
            return t
        
        window = defaultdict(int)
        tWindow = defaultdict(int)
        for c in t:
            tWindow[c] += 1
        
        left, right = 0, 0
        required = len(tWindow)
        ans = float('inf'), None, None
        formed = 0
        while right < len(s):
            ch = s[right]
            window[ch] += 1
            
            if ch in tWindow and window[ch] == tWindow[ch]:
                formed += 1
            
            while left <= right and formed == required:
                ch = s[left]
                
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window[ch] -= 1
                if ch in tWindow and window[ch] < tWindow[ch]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]