class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)
        if len_nums <=k:
            max_item = nums[0]
            for item in nums:
                max_item =max(max_item,item)
            return [max_item]
        
        left = 0
        max_lsit = []

        if k ==1:
            return nums
        else:
            right = k+left-1
        while right <=len_nums-1:
            max_num = nums[left]
            for num in nums[left:right+1]:
                max_num = max(max_num,num)
            max_lsit.append(max_num)
            
            right+=1
            left+=1
        return max_lsit