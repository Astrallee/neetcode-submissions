class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left=0 
        right=len(heights)-1
        while left<right:
            area =  (right-left)*min(heights[left],heights[right])
            if heights[left]<heights[right]:
                left = left+1
            else:
                right = right-1 
            max_area = max(max_area ,area)  
        return  max_area 