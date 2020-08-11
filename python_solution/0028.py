class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # New Solution: one-pass (28ms: 88.96%)
        # if needle is empty, then return 0!
        if not needle: return 0
        if not haystack: return -1
        lh, ln = len(haystack), len(needle)
        for i in range(lh-ln+1):
            if haystack[i] == needle[0]:
                if haystack[i+1:i+ln] == needle[1:]:
                    return i
        return -1
        
        # Or, you can use: str.index(str) to find pos