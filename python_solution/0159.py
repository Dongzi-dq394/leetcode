class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Solution by myself: Hash Table + Two Pointers (44ms: 97.45%)
        res = slow = 0
        dic = {}
        for i, char in enumerate(s):
            if char not in dic:
                dic[char] = 1
                if len(dic)>2:
                    while dic[s[slow]]>1:
                        dic[s[slow]] -= 1
                        slow += 1
                    dic.pop(s[slow])
                    slow += 1
                else:
                    res = max(res, i-slow+1)
            else:
                dic[char] += 1
                res = max(res, i-slow+1)
        return res