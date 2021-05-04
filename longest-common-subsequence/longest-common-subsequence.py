def lcs(X, Y, m, n, dp):
	
	# base case
	if (m == 0 or n == 0):
		return 0

	# if the same state has already been
	# computed
	if (dp[m - 1][n - 1] != -1):
		return dp[m - 1][n - 1]

	# if equal, then we store the value of the
	# function call
	if (X[m - 1] == Y[n - 1]):

		# store it in arr to avoid further repetitive
		# work in future function calls
		dp[m - 1][n - 1] = 1 + lcs(X, Y, m - 1, n - 1, dp)

		return dp[m - 1][n - 1]

	else :

		# store it in arr to avoid further repetitive
		# work in future function calls
		dp[m - 1][n - 1] = max(lcs(X, Y, m, n - 1, dp),
							lcs(X, Y, m - 1, n, dp))

		return dp[m - 1][n - 1]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[-1 for i in range(1000)]
		for i in range(1000)]
        
        
        
        return lcs(text1, text2, len(text1), len(text2), dp)
       