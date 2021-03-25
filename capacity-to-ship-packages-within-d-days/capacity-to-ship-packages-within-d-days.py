class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def isGood(m):
            days = 0
            total_weight = 0
            
            for i in range(len(weights)):
                if total_weight + weights[i] > m:
                    total_weight = 0
                    days += 1
                total_weight += weights[i]
            
            if total_weight > 0:
                days += 1
                total_weight = 0
                
            return days <= D
        
        
        left = min(weights)
        right = sum(weights)
        ans = sum(weights)
        max_weight = max(weights)
        while left <= right:
            m = (left + right) // 2
            res = isGood(m)
            if res and m >= max_weight:
                ans = min(ans, m)
                right = m - 1
            else:
                left = m + 1
        
        return ans
        
        