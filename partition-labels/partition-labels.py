class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        left_set = set([S[0]])
        ans = []
        start = 0
        for end in range(1, len(S)):
            is_valid = True
            
            for j in range(end, len(S)):
                if S[j] in left_set:
                    is_valid = False
                    break
            
            if is_valid:
                left_set = set(S[end])
                if not ans:
                    ans.append(end)
                else:
                    ans.append(end - start)
                start = end
            else:
                left_set.add(S[end])
        ans.append(len(S) - start)
        return ans
            