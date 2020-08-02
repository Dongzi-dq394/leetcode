class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, n in enumerate(s):
            if count[n] == 1:
                return i
        return -1