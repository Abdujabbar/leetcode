class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        best = 0
        left = 0
        while left < len(arr):
            right = left
            if right + 1 < len(arr) and arr[right] < arr[right + 1]:
                
                while right + 1 < len(arr) and arr[right] < arr[right + 1]:
                    right += 1
                    
                if right + 1 < len(arr) and arr[right] > arr[right + 1]:
                    
                    while right + 1 < len(arr) and arr[right] > arr[right + 1]:
                        right += 1
                    best = max(right - left + 1, best)
            left = max(left + 1, right)
        
        return best