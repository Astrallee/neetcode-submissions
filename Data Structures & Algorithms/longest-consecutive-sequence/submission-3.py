class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length =len(nums)
        if length <=1:
            return length 
        new_nums = sorted(nums)
        order_len = 1
        max_order_len = 1
        for index in range(1,length):
            if new_nums[index] == new_nums[index-1]+1:
                order_len +=1
                
            elif new_nums[index] == new_nums[index-1]:
                continue
            else:
                order_len = 1
            if order_len  >=max_order_len:
                max_order_len  = order_len 
        return max_order_len  