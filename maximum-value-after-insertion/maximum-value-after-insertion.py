class Solution:
    def maxValue(self, n: str, x: int) -> str:
        
        index = 0
        if n[0] == "-":
            index += 1
        if index < 1:
            while index < len(n) and int(n[index]) >= x:
                index += 1
        else:
            while index < len(n) and int(n[index]) <= x:
                index += 1

        return n[:index] + str(x) + n[index:]

        
        
       