class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                break
        
        left = 0
        right = len(row) - 1
        
        
        while left <= right:
            m = (left + right) // 2
            
            if row[m] == target:
                return True
            elif row[m] > target:
                right = m - 1
            else:
                left = m + 1
        
        
        return False