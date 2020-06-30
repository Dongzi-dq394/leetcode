class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        length1 = len(haystack)
        length2 = len(needle)
        for i in range(length1-length2+1):
            if haystack[i] == needle[0]:
                if haystack[i+1:i+length2] == needle[1:]:
                    return i
        return -1
        
        # Or, you can use: str.index(str) to find pos