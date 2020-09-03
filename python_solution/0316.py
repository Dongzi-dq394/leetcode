class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Solution 1 from discussion: Stack + Hash Table (44ms: 54.26%)
        last = {}
        for i, char in enumerate(s):
            last[char] = i
        stack = []
        for i in range(len(s)):
            if s[i] in stack:
                continue
            while stack and stack[-1]>s[i] and last[stack[-1]]>i:
                stack.pop()
            stack.append(s[i])
        return ''.join(x for x in stack)