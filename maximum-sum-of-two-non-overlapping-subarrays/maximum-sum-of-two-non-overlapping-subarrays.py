class Solution:
    def trail(self, A, a, b):
        # We want to find the largest value of sa, 
        # and then the corresponding sb that gives largest result
        
        sa = ba = sum(A[:a]) # sum from beggining
        sb = sum(A[a:b+a])   # sum right after "sa"
        
        best = ba+sb
        
        for i in range(b+a,len(A)):
            sa += A[i-b]- A[i-b-a] # Sum of sa
            sb += A[i]  - A[i-b] # Sum of sb
            
            ba = max( ba, sa ) # This will retain the best sa window
            
            best = max( best, ba+sb) # Next, we just have to find the largest sb with that best sa

        return best
    
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        max_LM_sum = self.trail(A,L,M) # when L is first, followed by M
        max_ML_sum = self.trail(A,M,L) # when M is first, followed by L
        return max(max_LM_sum, max_ML_sum)