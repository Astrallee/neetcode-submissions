class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s +=char.lower()
        length = len(new_s)
        left = 0
        right = length-1
        while left<right:
            if new_s[left]==new_s[right]:
                left+=1
                right-=1
            else:
                return False
        return True