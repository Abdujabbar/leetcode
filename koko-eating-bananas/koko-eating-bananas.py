class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isGood(m, piles, targetHour):
            hours = 0
            for pile in piles:
                hours += pile // m
                if pile % m != 0:
                    hours += 1
            
            return hours <= targetHour
        
        left = 0
        right = 10 ** 10
        
        while right > left + 1:
            m = (left + right) // 2
            if isGood(m, piles, h):
                right = m
            else:
                left = m
        
        
        return right