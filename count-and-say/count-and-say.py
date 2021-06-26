class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        if n == 3:
            return "21"
        s = self.countAndSay(n - 1)
        ans = ""
        
        counter = 1
        for right in range(1, len(s)):
            if s[right] != s[right - 1]:
                ans += "{}{}".format(counter, s[right - 1])
                counter = 1
            else:
                counter += 1
        
        ans += "{}{}".format(counter, s[-1])
        return ans