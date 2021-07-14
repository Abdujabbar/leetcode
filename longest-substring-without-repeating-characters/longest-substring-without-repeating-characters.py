class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        counter = defaultdict(int)
        best = 0
        
        for right in range(len(s)):
            right_char = s[right]
            
            counter[right_char] += 1
            
            while counter[right_char] > 1:
                left_char = s[left]
                counter[left_char] -= 1
                left += 1
            
            best = max(best, right - left + 1)
        
        
        return best