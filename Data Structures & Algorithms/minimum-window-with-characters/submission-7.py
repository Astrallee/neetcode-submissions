class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_t = len(t)
        len_s = len(s)

        if len_s < len_t:
            return ""
        # 对t进行统计
        count_t = {}
        for item in t:
            count_t[item]=count_t.get(item,0)+1

        
        left = 0
        need = len_t
        window_char_count = {}
        res = ""
        for right in range(len_s):
            item = s[right]
            window_char_count[item] = window_char_count.get(item,0)+1
            # 这个数在t里 而且s中的数是小于等于t里面的  就是找到了  找到就继续找
            if item in count_t and window_char_count[item]<=count_t[item]:
                need =need -1
            ## 找找找 一直到找完了
            while need==0:
                # 看看能不能找个更短的  先把找到的保存下
                if not res or (right-left+1) <len(res):
                    res = s[left:right+1]

                # 从s窗口的左边开始删
                left_char = s[left]
                window_char_count[left_char] -=1

                if left_char in count_t and window_char_count[left_char]<count_t[left_char]:
                    need = need+1
                left += 1
        return res


