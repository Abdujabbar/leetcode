# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            m = (left + right) // 2
            r = guess(m)
            if r == 0:
                return m
            if r == -1:
                right = m - 1
            else:
                left = m + 1
        
        return -1
       