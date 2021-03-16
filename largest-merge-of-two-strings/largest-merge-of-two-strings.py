class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        merge = ""
        word1 = list(word1)
        word2 = list(word2)
        while left < len(word1) or right < len(word2):
            if left < len(word1) and right < len(word2):
                if word1[left] > word2[right]:
                    merge += word1[left]
                    left += 1
                elif word2[right] > word1[left]:
                    merge += word2[right]
                    right += 1
                else:
                    if word1[left:] > word2[right:]:
                        merge += word1[left]
                        left += 1
                    else:
                        merge += word2[right]
                        right += 1
            elif left < len(word1):
                merge += word1[left]
                left += 1
            else:
                merge += word2[right]
                right += 1
        
        return merge