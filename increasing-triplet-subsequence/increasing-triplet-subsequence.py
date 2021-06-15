class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sub = []
        
        def binarySearch(nums, target):
            left = 0
            right = len(nums)
            
            while left < right:
                m = (left + right) // 2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    right = m
                else:
                    left = m + 1
            
            return left
        
        for num in nums:
            pos = binarySearch(sub, num)
            
            if not sub or pos >= len(sub):
                sub.append(num)
            else:
                sub[pos] = num
            
            if len(sub) == 3:
                is_valid = True
                for i in range(1, len(sub)):
                    if sub[i] < sub[i - 1]:
                        is_valid = False
                if is_valid:
                    return True
                sub = [num]
                
        return False