class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = []
        
        for interval in intervals:
            if not ans:
                ans.append(interval)
            elif ans[-1][0] <= interval[0] <= ans[-1][1]:
                ans[-1][1] = max(interval[1], ans[-1][1])
            else:
                ans.append(interval)
                
        
        return ans