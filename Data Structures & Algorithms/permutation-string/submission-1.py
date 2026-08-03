class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:         
            return False
        count_s1 = {}     
        for char in s1:         
            count_s1[char] = count_s1.get(char, 0) + 1   
            
            
        window = {}     
        left = 0
        for right in range(len_s2):
            # 加入右边字符         
            window[s2[right]] = window.get(s2[right], 0) + 1
            
            # 保持窗口长度等于 s1长度         
            if right - left + 1 > len_s1:
                left_char = s2[left]             
                window[left_char] -= 1
                if window[left_char] == 0:                 
                    del window[left_char]
                left += 1 
            # 判断当前窗口是否满足排列         
            if window == count_s1:             
                return True
        return False