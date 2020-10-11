class Solution:
    def confusingNumberII(self, N: int) -> int:
        # Solution from discussion: Backtracking (9568ms: 5.07%)
        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        res = 0
        def judge(num):
            new = 0
            for i, char in enumerate(str(num)):
                new += 10**i * mapping[int(char)]
            return new!=num
        def backtracking(cur_num):
            nonlocal res
            if judge(cur_num):
                res += 1
            for cand in [0,1,6,8,9]:
                new_num = cur_num*10+cand
                if new_num<=N:
                    backtracking(new_num)
        for start in [1,6,8,9]:
            backtracking(start)
        return res