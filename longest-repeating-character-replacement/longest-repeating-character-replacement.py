from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        max_letter_count = 0
        frequencies = defaultdict(int)
        left = 0
        for right in range(len(s)):
            frequencies[s[right]] += 1
            max_letter_count = max(max_letter_count, frequencies[s[right]])

            if (right - left + 1 - max_letter_count) > k:
                frequencies[s[left]] -= 1
                left += 1
            best = max(right - left + 1, best)

        return best