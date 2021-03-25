class Solution:
    def check(self, nums: List[int]) -> bool: 
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            arr = []
            for z in range(len(nums)):
                arr.append(nums[(z + i) % len(nums)])
            
            if arr == sorted_nums:
                return True
        
        return False