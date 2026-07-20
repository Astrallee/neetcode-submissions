class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_str = ""
        if len(strs)>=1:
            for index,item in enumerate(strs):
                strs_str += str(len(item))+"#"+item
            return strs_str 
        else :
            return ""  
    def decode(self, s: str) -> List[str]:
        strs_list = []
        i = 0
        while i <len(s):
            j = i
            # 找长度结束位置         
            while s[j] != "#":            
                j += 1
            length = int(s[i:j])
            i = j + 1
            item = s[i:i+length]
            strs_list.append(item)
            i += length
        return strs_list