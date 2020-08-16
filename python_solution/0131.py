class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # New Solution: Backtracking (96ms: 49.28%)
        if not s: return [[]]
        res = []
        def backtracking(sub_ans, string, index):
            if index==len(s):
                if string==string[::-1]:
                    res.append(sub_ans+[string])
                return
            if string==string[::-1] and string:
                backtracking(sub_ans+[string], s[index], index+1)
            backtracking(sub_ans, string+s[index], index+1)
        backtracking([], '', 0)
        return res
        
        # New Solution 2: from discussion --> Memozation (68ms: 89.35%)
        # Much faster but will use more memory...
        dic = {} # To avoid the duplicate computing
        def helper(s):
            if not s:
                return [[]]
            if s in dic:
                return dic[s]
            res = []
            for i in range(1, len(s)+1):
                if s[:i]==s[:i][::-1]:
                    for sub_res in helper(s[i:]):
                        res.append([s[:i]]+sub_res)
            dic[s] = res # Important
            return res
        return helper(s)