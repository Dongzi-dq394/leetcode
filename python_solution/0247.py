class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Solution by myself: Brute Force + Palindrome (160ms: 24.60%)
        if n==1: return ['0', '1', '8']
        ele = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        res = []
        for i in range(n//2):
            if i==0:
                res += ['1', '6', '8', '9']
            else:
                temp = []
                for sub_res in res:
                    for char in '01689':
                        temp.append(sub_res+char)
                res = temp
        if n&1:
            temp = []
            for sub_res in res:
                for char in '018':
                    temp.append(sub_res+char)
            res = temp
        for i in range(len(res)):
            for j in range(n//2-1, -1, -1):
                res[i] += ele[res[i][j]]
        return res
        
        # Solution from Discussion: Backtracking (104ms: 84.37%)
        # Very Tricky!
        mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        res = []
        def backtracking(left, right, l, r):
            if l>r:
                res.append(left+right)
                return
            if l==r:
                for char in '018':
                    res.append(left+char+right)
                return
            for char in mapping:
                if char=='0' and l==0:
                    continue
                backtracking(left+char, mapping[char]+right, l+1, r-1)
        backtracking('', '', 0, n-1)
        return res