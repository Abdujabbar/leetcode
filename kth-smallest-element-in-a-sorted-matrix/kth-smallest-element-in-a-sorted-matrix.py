class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for row in matrix:
            arr += row
        
        arr.sort()
        return arr[k - 1]