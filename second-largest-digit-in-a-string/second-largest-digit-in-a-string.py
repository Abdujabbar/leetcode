class Solution:
    def secondHighest(self, s: str) -> int:
        nums = []
        for c in s:
            if c.isdigit():
                nums.append(int(c))
        
        nums = list(set(nums))
        nums.sort()
        if len(nums) >= 2:
            return nums[-2]
        
        return -1