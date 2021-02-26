class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        a, b = nums[:2]
        left = 2
        for num in nums[2:]:
            if b != num:
                nums[left] = num
                left += 1
                a, b = b, a
                b = num
            elif b == num and a != num:
                nums[left] = num
                left += 1
                a, b = b, a
                b = num
        
        return left
                