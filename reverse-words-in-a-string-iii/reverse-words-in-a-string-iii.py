class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        s += " "
        start = 0
        for i, c in enumerate(s):
            if c == " ":
                ans += s[start:i][::-1]
                ans += " "
                start = i + 1
        
        
        return ans.rstrip(" ")
                