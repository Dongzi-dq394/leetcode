class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # New Solution: Backtracking from Solution (28ms: 84.53%)
        if not digits: return []
        mapping = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        res = []
        def backtracking(string, index):
            if index == len(digits):
                res.append(string)
                return
            else:
                for char in mapping[int(digits[index])-2]:
                    backtracking(string+char, index+1)
        backtracking('', 0)
        return res