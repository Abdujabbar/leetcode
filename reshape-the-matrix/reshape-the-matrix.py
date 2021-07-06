class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(nums) * len(nums[0]):
            return nums
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, c)) for _ in range(r)]