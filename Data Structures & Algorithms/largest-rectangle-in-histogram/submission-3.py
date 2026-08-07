class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []     
        max_area = 0
        
        ## 这个 0 是为了强制把剩余柱子全部弹出来计算。
        heights.append(0)
        
        for i,h in enumerate(heights):
            # 找到了右边 更矮的柱子下标
            while stack and h<heights[stack[-1]]:
                height = heights[stack.pop()]
                
                if stack:
                    width = i-stack[-1] -1
                else:
                    width = i
                max_area = max(max_area,height*width)
            stack.append(i)
        return max_area 