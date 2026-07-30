class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(numbers,i,j,target):
            result = []
            while(i<j):
                if numbers[i]+numbers[j] ==target:
                    pair = [numbers[i],numbers[j]]
                    if pair not in result:
                        result.append(pair)
                    i += 1 
                    j -= 1
                elif numbers[i]+numbers[j] >target:
                    j=j-1
                else:
                    i = i+1
            return result 
        final_list = []
        new_nums = sorted(nums)
        
        length = len(new_nums)
        for index,item in enumerate(new_nums ):
            if index > 0 and new_nums [index] == new_nums [index-1]: 
                continue
            
            target = -item
            pairs= twoSum(new_nums ,index+1,length-1,target )
            if pairs:
                for pair  in pairs:
                    final_list.append([item]+pair  )
        return final_list 