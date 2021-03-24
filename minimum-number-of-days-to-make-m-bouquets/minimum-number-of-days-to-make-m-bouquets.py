class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int: 
        
        if len(bloomDay) < m*k:
            return -1 
        
        def isGood(day, bloomDays, target, k):
            count = 0
            for bloom in bloomDays:
                if bloom <= day:
                    count += 1
                    if count == k:
                        target -= 1
                        count = 0
                else:
                    count = 0
            return target <= 0

        left = min(bloomDay)
        right = max(bloomDay)
        ans = right
        while left <= right:
            middle = (left + right) // 2
            isGoodValue = isGood(middle, bloomDay, m, k)
            
            if isGoodValue:
                ans = min(ans, middle)
                right = middle - 1
            else:
                left = middle + 1
        
        return ans