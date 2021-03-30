class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = defaultdict(int)
        for word in words:
            mp[word] += 1
        
        ans = []
        for item in sorted(mp.items(), key=lambda x: (-x[1], x[0])):
            ans.append(item[0])
            if len(ans) >= k:
                break
        
        return ans