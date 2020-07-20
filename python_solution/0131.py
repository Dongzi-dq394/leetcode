class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return []
        res = []
        def judge(s):
            return s==s[::-1]
        def backtrack(string, start, one_res):
            if start >= len(s):
                if judge(string):
                    res.append(one_res+[string])
                return
            if string and judge(string):
                backtrack('', start, one_res+[string])
            backtrack(string+s[start], start+1, one_res)
        backtrack('', 0, [])
        return res