class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def findMaxLength(start, end):
            cnt = defaultdict(int)

            for i in range(start, end):
                cnt[s[i]] += 1

            pivotIndex = -1

            for i in range(start, end):
                if cnt[s[i]] < k:
                    pivotIndex = i
                    break

            if pivotIndex == -1:
                return end - start

            return max(
                findMaxLength(start, pivotIndex),
                findMaxLength(pivotIndex + 1, end)
            )

        return findMaxLength(0, len(s))