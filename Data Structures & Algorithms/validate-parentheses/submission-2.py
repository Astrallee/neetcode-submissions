class Solution:
    def isValid(self, s: str) -> bool:
        len_s = len(s)
    
        stack_list = []
        
        for index in range(len_s):
            if s[index] in "({[":
                stack_list.append(s[index])
            else:
                if not stack_list:               
                    return False
                    
                char_bracket = stack_list.pop()
                if s[index] == ')' and char_bracket !="(":
                    return False
                if s[index] == '}' and char_bracket !="{":
                    return False
                if s[index] == ']' and char_bracket !="[":
                    return False
        return len(stack_list) == 0