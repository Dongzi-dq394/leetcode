class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'*', '/', '+', '-'}
        while tokens:
            ele = tokens.pop(0)
            if ele not in op:
                stack.append(int(ele))
            else:
                p1 = stack.pop()
                p2 = stack.pop()
                if ele == '+':
                    stack.append(p1+p2)
                elif ele == '-':
                    stack.append(p2-p1)
                elif ele == '*':
                    stack.append(p1*p2)
                else:
                    stack.append(int(p2/p1))
            #print(stack)
        return stack[0]