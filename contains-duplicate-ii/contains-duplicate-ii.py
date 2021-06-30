class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        prev_map = {}
        
        for i in range(len(nums)):
            if nums[i] not in prev_map:
                prev_map[nums[i]] = i
            else:
                if i - prev_map[nums[i]] <= k:
                    return True
                prev_map[nums[i]] = i
        
        return False