class Solution:
    def smallestSubsequence(self, text: str) -> str:
        dic = {char:i for i, char in enumerate(text)}
        used = {}
        stack = []
        for i in range(len(text)):
            if text[i] in used:
                continue
            while stack and stack[-1]>text[i] and dic[stack[-1]]>i:
                temp = stack.pop()
                used.pop(temp)
            stack.append(text[i])
            used[text[i]] = True
        return ''.join(x for x in stack)