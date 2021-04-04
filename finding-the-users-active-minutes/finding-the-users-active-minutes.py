from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        active_minutes = defaultdict(set)
        for log in logs:
            user_id, minute = log
            active_minutes[user_id].add(minute)
        cnt = defaultdict(int)
        
        for k, v in active_minutes.items():
            cnt[len(v)] += 1
            
    
        for k, v in cnt.items():
            ans[k - 1] = v
        
        return ans