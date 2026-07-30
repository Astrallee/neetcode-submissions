class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        water = 0
        for index,item in enumerate(height):
            left_max = max(height[:index+1])
            right_max = max(height[index:])
            water = min(left_max,right_max)-height[index]
            total += water 
        return total 