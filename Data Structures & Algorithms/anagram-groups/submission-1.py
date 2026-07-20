class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        for index,item in enumerate(strs):
            key_sorted = ''.join(sorted(item))
            if key_sorted not in new_dict:             
                new_dict[key_sorted ] = []
            new_dict[key_sorted].append(item)
        
        return list(new_dict.values())
     