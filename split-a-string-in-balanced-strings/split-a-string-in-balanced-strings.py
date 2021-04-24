class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        counter = 0
        r = 0
        l = 0
        for c in s:
            if c == 'R':
                r += 1
            elif c == 'L':
                r -= 1
            
            if r == 0:
                counter += 1

        return counter