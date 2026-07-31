class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_length = 0
        head= 0
        for tail in range(len(s)):
            while s[tail] in window:
                window.remove(s[head])
                head+=1
            window.add(s[tail])
            max_length = max(max_length, tail-head+1)

        return max_length 