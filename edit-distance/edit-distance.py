class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[-1 for i in range(501)] for j in range(max(n, m) + 1)]
        def minDistanceHelper(s1, s2, n, m, dp):
            if n == 0:
                return m
            
            if m == 0:
                return n
            
            if dp[n - 1][m - 1] != -1:
                return dp[n - 1][m - 1]
            
            if s1[n - 1] == s2[m - 1]:
                dp[n - 1][m - 1] = minDistanceHelper(s1, s2, n - 1, m - 1, dp)
                return dp[n - 1][m - 1]
            
            dp[n - 1][m - 1] = 1 + min(
                minDistanceHelper(s1, s2, n - 1, m, dp),
                minDistanceHelper(s1, s2, n, m - 1, dp),
                minDistanceHelper(s1, s2, n - 1, m - 1, dp)
            )
            
            return dp[n - 1][m - 1]
    
        return minDistanceHelper(word1, word2, len(word1), len(word2), dp)