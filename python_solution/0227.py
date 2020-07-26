class Solution:
    def calculate(self, s: str) -> int:
        # Solution 1: Use string split (124ms: 47.61%) --> my idea
        def cal(s):
            start = i = 0
            res = 1
            pre = '*'
            while i<len(s):
                if s[i] in {'*', '/'}:
                    if pre == '*':
                        res *= int(s[start:i])
                    if pre == '/':
                        res //= int(s[start:i])
                    pre = s[i]
                    start = i+1
                i += 1
            if pre == '*':
                res *= int(s[start:i])
            else:
                res //= int(s[start:i])
            return res
        s = s.replace(' ', '')
        res = 0
        for add in s.split('+'):
            print(add)
            all_neg = 0
            i = 0
            temp = 0
            for sub in add.split('-'):
                if sub=='':
                    all_neg = 1
                    continue
                if all_neg==0 and i==0:
                    temp += cal(sub)
                    i += 1
                    continue
                temp -= cal(sub)
            res += temp
        return res
        
        # Solution 2: Use stack (88ms: 83.60%) --> from discussion
        s = s.replace(' ', '') + '+'
        l = r = 0
        stack = []
        op = '+'
        while r < len(s):
            if s[r] in {'*', '/', '+', '-'}:
                temp = int(s[l:r])
                if op == '+':
                    stack.append(temp)
                elif op == '-':
                    stack.append(-temp)
                elif op == '*':
                    stack[-1] *= temp
                else:
                    if stack[-1] >= 0:
                        stack[-1] //= temp
                    else:
                        stack[-1] = -(abs(stack[-1]) // temp)
                op = s[r]
                l = r+1
            r += 1
        return sum(stack)