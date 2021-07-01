class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best = 0
        k = 1
        stack = []
        for num in nums:
            if num == 0:
                if k == 0:
                    while stack.pop(0) != 0: 
                        continue
                else:
                    k -= 1
            stack.append(num)
            best = max(len(stack), best)
        return best - 1