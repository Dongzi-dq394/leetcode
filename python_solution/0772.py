class Solution:
    def calculate(self, s: str) -> int:
        # Solution 1: Stack from the first question (36ms: 96.68%)
        s = s + '+'
        number = 0
        op = '+'
        stack = []
        for char in s:
            if char.isdigit():
                number = number*10 + int(char)
            elif char in '+-*/':
                if op=='+':
                    stack.append(number)
                elif op=='-':
                    stack.append(-number)
                elif op=='*':
                    temp = stack.pop()
                    stack.append(number*temp)
                else:
                    temp = stack.pop()
                    stack.append(int(temp/number))
                op = char
                number = 0
            elif char=='(':
                stack.append(op)
                stack.append('(')
                op = '+'
            elif char==')':
                if op=='+':
                    stack.append(number)
                elif op=='-':
                    stack.append(-number)
                elif op=='*':
                    temp = stack.pop()
                    stack.append(number*temp)
                else:
                    temp = stack.pop()
                    stack.append(int(temp/number))
                number = 0
                while stack and stack[-1]!='(':
                    number += stack.pop()
                stack.pop()
                op = stack.pop()
        return sum(stack)