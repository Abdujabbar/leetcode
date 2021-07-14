from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        current_sum = 0
        left = 0
        counter = defaultdict(int)
        best = 0
        
        for right in range(len(nums)):
            right_num = nums[right]
            counter[right_num] += 1
            current_sum += right_num
            
            while counter[right_num] > 1:
                left_num = nums[left]
                counter[left_num] -= 1
                left += 1
                current_sum -= left_num
            
            best = max(best, current_sum)
        
        return best
            
        