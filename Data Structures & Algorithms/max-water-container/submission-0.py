class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        length_list = len(heights)
        for index,item in enumerate(heights):
            i = index+1
            while i<=length_list -1:
                length = i-index
                heigth = min(heights[i],item)
                area = length * heigth
                max_area = max(max_area ,area)
                i = i+1
        return max_area 