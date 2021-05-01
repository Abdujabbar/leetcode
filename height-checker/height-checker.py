class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        
        counter = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                counter += 1
        
        
        return counter