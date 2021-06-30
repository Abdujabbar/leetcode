class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def helper(prefix_sums, firstLen, secondLen):
            best = 0
            current = 0
            for i in range(firstLen + secondLen, len(prefix_sums)):
                current = max(current, prefix_sums[i - firstLen] - prefix_sums[i - firstLen - secondLen])
                best = max(best, current + prefix_sums[i] - prefix_sums[i - firstLen])

            return best

        return max(helper(prefix, firstLen, secondLen), helper(prefix, secondLen, firstLen))
