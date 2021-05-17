class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = []
        count = 0
        
        
        for c in s:
            if c == '(':
                opens.append(c)
            else:
                if not opens:
                    count += 1
                else:
                    opens.pop()
        
        return count + len(opens)
        