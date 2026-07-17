class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_list = []
        for item in nums:
            if item in nums_list:
                return True
            else:
                nums_list.append(item)
        return False