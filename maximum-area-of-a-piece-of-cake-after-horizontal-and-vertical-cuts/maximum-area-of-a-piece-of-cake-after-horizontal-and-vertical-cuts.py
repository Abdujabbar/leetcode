class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontals = []
        verticals = []
        
        for i in range(1, len(horizontalCuts)):
            horizontals.append(horizontalCuts[i] - horizontalCuts[i - 1])    
        
        for i in range(1, len(verticalCuts)):
            verticals.append(verticalCuts[i] - verticalCuts[i - 1])    
        
        
        return (max(horizontals) * max(verticals)) % (10 ** 9 + 7)