class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def count_s(s):
            count ={}
            for item in s:
                if count.get(item, 0) ==0:
                    count[item] = 1
                else:
                    count[item] += 1
            return count 
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        count_s1 = count_s(s1)
        
        left = 0
        for right in range(len_s1-1,len_s2):
            count_short = count_s(s2[left:right+1])
            if count_short == count_s1:
                return True
            else:
                left+=1
        
        return False