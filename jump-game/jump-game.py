class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        @lru_cache(None)
        def dfs(current):
            if current + nums[current] >= len(nums) - 1:
                return True
            
            next_index = current + nums[current]
            
            while current < next_index:
                current += 1
                ans = dfs(current)
                if ans:
                    return True
            
            return False
        
        return dfs(0)