class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        s1 = list(s1)
        s2 = list(s2)
        cnt = 0
        indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indices.append(i)
        
        if len(indices) != 2:
            return False
        
        s1[indices[0]], s1[indices[-1]] = s1[indices[-1]], s1[indices[0]]
        
        return s1 == s2
                