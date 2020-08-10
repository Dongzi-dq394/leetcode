class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Solution 1: Sort by length (36ms: 69.33%)
        res = ''
        if not strs: return res
        strs.sort(key = lambda x: len(x))
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res