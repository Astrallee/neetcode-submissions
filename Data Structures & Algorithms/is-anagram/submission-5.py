class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        result_t = {}
        result_s = {}
        for char1 in s:
            result_t[char1] = result_t.get(char1 , 0) + 1
        for char2 in t:
            result_s[char2] = result_s.get(char2, 0) + 1
            
        for key , value in result_t.items():
            if value != result_s.get(key,0):
                return False
        return True