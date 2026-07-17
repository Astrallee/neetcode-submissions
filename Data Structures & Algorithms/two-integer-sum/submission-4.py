class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(0,len(nums)):
            value = target - nums[index]
            if value in nums[index+1:]:
                second_index = nums[index+1:].index(value) + index+1
                return [index,second_index]