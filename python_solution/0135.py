class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Solution from Solution: two-pass (28ms: 19.17%)
        l_to_r = [1]*len(ratings)
        r_to_l = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                l_to_r[i] = l_to_r[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                r_to_l[i] = r_to_l[i+1]+1
        res = 0
        for i in range(len(ratings)):
            res += max(l_to_r[i], r_to_l[i])
        return res