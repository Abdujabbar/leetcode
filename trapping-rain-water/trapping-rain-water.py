class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left_max = []
        right_max = []
        n = len(height) - 1
        for i in range(len(height)):
            if not left_max:
                left_max.append(height[i])
            else:
                left_max.append(max(left_max[-1], height[i]))
        
        for i in reversed(range(len(height))):
            if not right_max:
                right_max.append(height[i])
            else:
                right_max.append(max(height[i], right_max[-1]))
        right_max = right_max[::-1]
        
        for i in range(len(height)):
            water_with_min_height = min(left_max[i], right_max[i])
            water = water_with_min_height - height[i]
            total_water += water
        
        return total_water