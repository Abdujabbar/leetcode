class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        
        ans = []
        for word in words:
            is_valid = True
            for c in word:
                if c not in allowed:
                    is_valid = False
                    break
            
            if is_valid:
                ans.append(word)
        
        return len(ans)