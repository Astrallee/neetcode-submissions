class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(numbers, target):
            result = []
            seen = set() 
            for index,item in enumerate(numbers):
                
                need = target - numbers[index]
                if need in seen:
                    pair = [need, item]
                    if pair not in result:
                        result.append(pair)
                seen.add(item)
            return result
        final_list = []
        new_nums = sorted(nums)
        seen =set()
        for index,item in enumerate(new_nums ):
            if item in seen :
                continue
            seen.add(item)

            pairs  = twoSum(new_nums [index+1:],-item )
            if pairs :
                for pair  in pairs:
                    final_list.append([item]+pair  )
        return final_list