class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Solution from Solution: Stack + Defaultdict (32ms: 67.21%)
        stack = [defaultdict(int)]
        i, length = 0, len(formula)
        while i<length:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                temp = stack.pop()
                i += 1
                start = i
                while i<length and formula[i].isdigit():
                    i += 1
                times = int(formula[start:i]) if i>start else 1
                for key in temp:
                    stack[-1][key] += times * temp[key]
            else:
                start = i
                i += 1
                while i<length and 97<=ord(formula[i])<=122:
                    i += 1
                element = formula[start:i]
                start = i
                while i<length and formula[i].isdigit():
                    i += 1
                times = int(formula[start:i]) if i>start else 1
                stack[-1][element] += times
        res = ''
        dic = stack.pop()
        key_list = sorted(list(dic.keys()))
        for key in key_list:
            res += key
            if dic[key] > 1:
                res += str(dic[key])
        return res