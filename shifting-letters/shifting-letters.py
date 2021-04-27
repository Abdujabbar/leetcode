class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        right = len(shifts) - 2
        while right >= 0:
            shifts[right] += shifts[right + 1]
            right -= 1
        s = list(s)
        for i in range(len(shifts)):
            s[i] = chr((shifts[i] + (ord(s[i]) - ord('a'))) % 26 + ord('a'))
        
        return "".join(s)