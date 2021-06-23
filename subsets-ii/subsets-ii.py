class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = set()
        
        power = 2 ** len(nums)
        
        for i in range(power):
            variation = []
            for j in range(len(nums)):
                mask = 1 << j
                if i & mask:
                    variation.append(nums[j])
            
            subsets.add(tuple(sorted(variation)))
        
        return [list(x) for x in subsets]