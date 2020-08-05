class Solution:
    def decodeString(self, s: str) -> str:
        # Solution 1 by myself: (56ms: 6.79%)
        res = ''
        start = 0
        times = 0
        while start<len(s):
            while start<len(s) and (ord(s[start])<48 or ord(s[start])>57):
                res += s[start]
                start += 1
            while start<len(s) and 48<=ord(s[start])<=57:
                times = times*10+int(s[start])
                start += 1
            start += 1
            temp = start
            number = 0
            while start<len(s):
                if s[start] == '[':
                    number += 1
                if s[start] == ']':
                    number -= 1
                if number < 0:
                    break
                start += 1
            sub_res = self.decodeString(s[temp:start])
            for i in range(times):
                res += sub_res
            start += 1
            times = 0
        return res
        
        # Solution 2: Stack from discussion (44ms: 23.06%)
        # With stack, we can deal with [[[]]] case easily
        res = ''
        stack = []
        times = 0
        for char in s:
            if char.isdigit():
                times = times*10 + int(char)
            elif char == '[':
                stack.append(res)
                stack.append(times)
                res = ''
                times = 0
            elif char == ']':
                res *= stack.pop()
                res = stack.pop() + res
            else:
                res += char
        return res