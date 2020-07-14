from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = defaultdict(int)
        for item in t:
            dic[item] += 1
        
        max_left, max_right = 0, len(s)
        target_number = len(t)
        start = 0
        
        for i in range(len(s)):
            if dic[s[i]] > 0:
                target_number -= 1
            dic[s[i]] -= 1
            if target_number == 0:
                while dic[s[start]] < 0:
                    dic[s[start]] += 1
                    start += 1
                if i-start+1 < max_right-max_left+1:
                    max_left, max_right = start, i
                dic[s[start]] += 1
                start += 1
                target_number += 1
        
        if max_right == len(s): return ''
        else: return s[max_left:max_right+1]