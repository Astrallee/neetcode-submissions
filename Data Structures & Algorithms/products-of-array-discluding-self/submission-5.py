class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ## 先计算前缀积
        prefix = {}
        prefix[0]=1
        for index in range(1,length):
            prefix[index]=nums[index-1] * prefix[index-1]
        
        ## 计算后缀积
        suffix = {}
        suffix[length-1] =1
        for index in range(length-2,-1,-1):
            suffix[index] = nums[index+1] * suffix[index+1]
        output = []
        for i in range(0,length):
            output.append(prefix[i]*suffix[i]) 
        return output