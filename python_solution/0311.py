class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ha, wa = len(A), len(A[0])
        hb, wb = len(B), len(B[0])
        dic_a = {}
        for i in range(ha):
            dic_a[i] = {}
            for j in range(wa):
                if A[i][j]!=0:
                    dic_a[i][j] = A[i][j]
        dic_b = {}
        for j in range(wb):
            dic_b[j] = {}
            for i in range(hb):
                if B[i][j]!=0:
                    dic_b[j][i] = B[i][j]
        res = [[0 for _ in range(wb)] for _ in range(ha)]
        for i in range(ha):
            for j in range(wb):
                temp = 0
                for key in dic_a[i]:
                    if key in dic_b[j]:
                        temp += dic_a[i][key]*dic_b[j][key]
                res[i][j] = temp
        return res