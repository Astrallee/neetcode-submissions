class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index,item in enumerate(numbers):
            need = target - numbers[index]
            if need in seen:
                return [seen[need]+1,index+1]
            seen[item]=index