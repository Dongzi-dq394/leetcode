class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Solution 1: from Hint and Solution (60ms: 84.67%)
        res = set()
        left_num = right_num = 0
        for char in s:
            if char == '(':
                left_num += 1
            if char == ')':
                if left_num>0:
                    left_num -= 1
                else:
                    right_num += 1
        def dfs(left, right, l_rem, r_rem, index, cur_str):
            if index == len(s):
                if left==right and l_rem==0 and r_rem==0:
                    res.add(cur_str)
                    return
            else:
                if s[index] == '(':
                    if l_rem>0:
                        dfs(left, right, l_rem-1, r_rem, index+1, cur_str)
                    dfs(left+1, right, l_rem, r_rem, index+1, cur_str+'(')
                elif s[index] == ')':
                    if r_rem>0:
                        dfs(left, right, l_rem, r_rem-1, index+1, cur_str)
                    if left>right:
                        dfs(left, right+1, l_rem, r_rem, index+1, cur_str+')')
                    else:
                        return
                else:
                    dfs(left, right, l_rem, r_rem, index+1, cur_str+s[index])
        dfs(0, 0, left_num, right_num, 0, '')
        return list(res)