class Solution:
    def calculate(self, s: str) -> int:
        # Solution 1 from Solution: Basic Stack (124ms: 51.36%)
        ele = []
        number = 0
        flag = False
        for char in s:
            if char.isdigit():
                number = number*10 + int(char)
                flag = True
            elif char!=' ':
                if flag:
                    ele.append(number)
                    number = 0
                    flag = False
                ele.append(char)
        if flag:
            ele.append(number)
        stack = []
        def helper(stack):
            res = stack.pop() if stack else 0
            while stack and stack[-1]!=')':
                op = stack.pop()
                if op=='+':
                    res += stack.pop()
                else:
                    res -= stack.pop()
            if stack:
                stack.pop()
            return res
        for i in range(len(ele)-1, -1, -1):
            if ele[i]!='(':
                stack.append(ele[i])
            else:
                temp = helper(stack)
                stack.append(temp)
        return helper(stack)
        
        # Solution 2 from discussion: Simpler Stack (76ms: 87.89%)
        s = s+'+'
        res = 0
        number = 0
        sign = 1
        stack = []
        for char in s:
            if char.isdigit():
                number = number*10 + int(char)
            elif char in {'+', '-'}:
                res += number * sign
                number = 0
                sign = 1 if char=='+' else -1
            elif char=='(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif char==')':
                res += sign*number
                number = 0
                temp = stack.pop()
                res = stack.pop()+res*temp
        return res