class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        
        while left < len(arr):
            right = left + 1
            while right < len(arr) and arr[right] > arr[right - 1]:
                right += 1
            
            if right > left + 1:
                return right - 1
            
            left += 1
            
        
        return -1