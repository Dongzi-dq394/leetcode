class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Solution by myself: Two Pointers + Sliding Window (68ms: 85.96%)
        res = 0
        start = end = 0
        dic = {}
        while end<len(s):
            if s[end] not in dic:
                dic[s[end]] = 1
                if len(dic)>k:
                    res = max(res, end-start)
                    while dic[s[start]]>1:
                        dic[s[start]] -= 1
                        start += 1
                    # Pop because we need to remove this item rather than set it to 0
                    dic.pop(s[start])
                    start += 1
            else:
                dic[s[end]] += 1
            end += 1
        res = max(res, end-start)
        return res